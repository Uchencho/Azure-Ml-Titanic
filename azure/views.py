from django.shortcuts import render
from .forms import PredictForm

# Create your views here.
def homepage(request):
    if request.method == "GET":
        form = PredictForm()
        return render(request, 'azure/home.html', {'form':form})
    else:
        form = PredictForm()