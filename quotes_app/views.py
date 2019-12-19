from django.shortcuts import render

# Create your views here.

def allbest(request):
    quotes= ['there is nothing','life is beautiful',]
    d = {
        'names':  quotes
    }
    return render(request,'quotes_app/all.html',d)
def features(request):
    quotes= ['nothing is imposssible','life is beautiful',]
    d = {
        'names':  quotes
    }
    return render(request,'quotes_app/features.html',d)