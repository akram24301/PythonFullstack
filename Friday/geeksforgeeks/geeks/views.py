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

