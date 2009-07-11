from django.http import HttpResponseRedirect
from ragendja.template import render_to_response


def main(request):
	return render_to_response(request, 'tabs.html', {})

def style(request):
	return render_to_response(request, 'style.css', {})

def tabbedjs(request):
	return render_to_response(request, 'tabbed.js', {})

def home(request):
	return render_to_response(request, 'home.html', {})


