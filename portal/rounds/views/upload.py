from rounds.models import Round, AcceptedRoundFile, Submission
from django.views.generic import View
from django.shortcuts import render, redirect
from portal.functions import hashid_decode
from rounds.forms import RoundUploadForm
from rounds.constants.filetypes import FILETYPES

class UploadRoundsView(View):
	template_name = "rounds/upload.html"

	def get(self, request, encoded):
		context = dict()
		decoded = hashid_decode(encoded)
		if decoded:
			current_round = Round.objects.get(pk=decoded)
			submissions = Submission.objects.all().filter(
				asc_team=request.user.delegate.team).filter(
				asc_round_file__asc_round=current_round).order_by('latest'
				).order_by('-submitted_at')
			accepted_files = AcceptedRoundFile.objects.all().filter(
				asc_round=current_round)
			context["encoded_url"] = encoded
			
			if current_round.visible:
				context["round"] = current_round
				context["submissions"] = submissions
				if current_round.active and accepted_files:
					context["form"] = RoundUploadForm(instance=current_round,
						team=request.user.delegate.team)
		return render(request, self.template_name, context)

	def post(self, request, encoded):
		context = dict()
		decoded = hashid_decode(encoded)
		if decoded:
			current_round = Round.objects.get(pk=decoded)
			submissions = Submission.objects.all().filter(
				asc_team=request.user.delegate.team).filter(
				asc_round_file__asc_round=current_round).order_by('latest'
				).order_by('-submitted_at')
			accepted_files = AcceptedRoundFile.objects.all().filter(
				asc_round=current_round)
			context["encoded_url"] = encoded
			
			if current_round.visible:
				context["round"] = current_round
				context["submissions"] = submissions
				if current_round.active and accepted_files:
					context["form"] = RoundUploadForm(request.POST,
						request.FILES,
						instance=current_round,
						team=request.user.delegate.team)
					if context["form"].is_valid():
						context["form"].save(team=request.user.delegate.team,
							user_id=request.user.pk)
						return redirect('rounds-upload-success',
							encoded=encoded)
		return render(request, self.template_name, context)