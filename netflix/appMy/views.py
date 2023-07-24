from django.shortcuts import render,get_object_or_404
from appUser.models import *
from appMy.models import *
# Create your views here.
def indexPage(request):
    context = {}
    return render(request,'index.html',context)

# def netflixPage(request,id):
#     profile = get_object_or_404(Profile,id=id)
#     context = {
#         "profile": profile,
#     }
#     return render(request,'browse-index.html',context)

def netflix(request): # form loginp = true yönlendirmeli
    profile = Profile.objects.filter(loginp = True,user = request.user).first()
    category = Category.objects.all()
    cards = Card.objects.all()
    context = {
        "profile": profile,
        "category":category,
        "cards" : cards,
    }
    return render(request,'browse-index.html',context)

def netflixType(request,catetitle = None):
    profile = Profile.objects.filter(loginp = True,user = request.user).first()
    category = Category.objects.all()
    type = Type.objects.all()
    
    
    if catetitle is None:
        cards = Card.objects.all()
    else:
        cards = Card.objects.filter(category__catetitle = catetitle)

        
        
        
    context = {
        "profile": profile,
        "category":category,
        "cards" : cards,
        "type": type,
        }
    return render(request,'netflix-type.html',context)