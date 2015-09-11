from django.shortcuts import render_to_response
from django.http import HttpResponse
# Create your views here.
def home(request):
	'''
	file = open("myapp/templates/index.html")
	data = file.read()
	file.close()
	'''
	file = open("myapp/string.txt","w")
	string = file.write("")
	file.close()
	#return HttpResponse(data)
	return render_to_response('index.html', {'add':""})

def result(request):
	data = []
	file = open("myapp/string.txt","r")
	string = file.read()
	file.close()
	add = string
	for i in range(10):
		tmp = "v" + str(i)
		if request.GET.has_key(tmp):
			add += str(i)
	if request.GET.has_key("vd"):
		add += "/"
	if request.GET.has_key("vm"):
		add += "*"
	if request.GET.has_key("vc"):
		add += "-"
	if request.GET.has_key("vp"):
		add += "+"
	if request.GET.has_key("vpo"):
		add = ""
	if request.GET.has_key("ve"):
		add = str(eval(add))
	file2 = open("myapp/string.txt","w")
	file2.write(add)
	file2.close()
	return render_to_response('index.html', {'add':add})