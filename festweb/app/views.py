from django.shortcuts import render

# Create your views here.
def sample(request):
    hello="hello world"
    context={
    "hey" : hello ,

    }
    return render(request,"sample.html",context)
