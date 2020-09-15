from django.shortcuts import render
def intro(req):
	return render(req,"myapp/intro.html")
# Create your views here.
