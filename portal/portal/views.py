from django.shortcuts import render

def page_not_found_view(request):
	return render(request, template_name="error/404.html", status=404)

def forbidden_view(request):
	return render(request, template_name="error/403.html", status=500)