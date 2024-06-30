from django.shortcuts import render
from django. http import HttpResponse
# relative import of forms
from .models import GeeksModel
from .forms import GeeksForm

# Create your views here.
def home(request):
    return HttpResponse("Good Evening")

def create_view(request):
	# dictionary for initial data with 
	# field names as keys
	context ={}

	# add the dictionary during initialization
	form = GeeksForm(request.POST or None)
	if form.is_valid():
		form.save()
		
	context['form']= form
	return render(request, "create_view.html", context)




from django.shortcuts import render
# relative import of forms
from .models import GeeksModel

def list_view(request):
	# dictionary for initial data with 
	# field names as keys
	context ={}

	# add the dictionary during initialization
	context["dataset"] = GeeksModel.objects.all()
		
	return render(request, "list_view.html", context)



# pass id attribute from urls
def detail_view(request, id):
    # dictionary for initial data with 
    # field names as keys
    context ={}
 
    # add the dictionary during initialization
    context["data"] = GeeksModel.objects.get(id = id)
         
    return render(request, "detail_view.html", context)




from django.shortcuts import (get_object_or_404,
                              render,
                              HttpResponseRedirect)
# update view for details
def update_view(request, id):
    # dictionary for initial data with 
    # field names as keys
    context ={}
 
    # fetch the object related to passed id
    obj = get_object_or_404(GeeksModel, id = id)
 
    # pass the object as instance in form
    form = GeeksForm(request.POST or None, instance = obj)
 
    # save the data from the form and
    # redirect to detail_view
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/geeks/"+id+'/')
 
    # add form dictionary to context
    context["form"] = form
 
    return render(request, "update_view.html", context)



# delete view for details
def delete_view(request, id):
	# dictionary for initial data with 
	# field names as keys
	context ={}

	# fetch the object related to passed id
	obj = get_object_or_404(GeeksModel, id = id)


	if request.method =="POST":
		# delete object
		obj.delete()
		# after deleting redirect to 
		# home page
		return HttpResponseRedirect("/geeks/list_view/")
	return render(request, "delete_view.html", context)

