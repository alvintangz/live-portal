from django.shortcuts import render

def page_not_found(request):
	return render(template_name="error/404.html", status=404)

def forbidden(request):
	return render(template_name="error/403.html", status=403)