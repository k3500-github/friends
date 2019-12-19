from django.shortcuts import render

# Create your views here.
def all(request):
    friends = ['nischal', 'kritika', 'shashank', 'ayush',]
    d = {
        'names':  friends
    }
    return render(request,'friend_app/all.html',d)

def best(request):
    friends = ['anjita','diksha','ram','shyam']
    d= {
        'names':friends
    }
    return render(request,'friend_app/best.html',d)