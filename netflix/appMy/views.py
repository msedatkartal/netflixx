from django.shortcuts import render,get_object_or_404,redirect
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
    card = Card.objects.all()

    if request.method == "POST":
        cardId = request.POST.get("listLike")
        cards = Card.objects.filter(id=int(cardId)).first()
        print("caard:", cardId)
        print(cards.like)
        if cards.like == False:
            cards.like =True
            cards.save()
        else:
            cards.like =False
            cards.save()
        
        return redirect('netflix')
        
        

    context = {
        "profile": profile,
        "category":category,
        "card" : card,
    }
    return render(request,'browse-index.html',context)

def netflixType(request,catetitle = None):
    profile = Profile.objects.filter(loginp = True,user = request.user).first()
    category = Category.objects.all()
    cards = Card.objects.all()
    type = Type.objects.all()
    # aksiyon di<i
    ogeler = {}
    
    for tip in type:
        movies = Card.objects.filter(type=tip, category__catetitle=catetitle) 
        if movies.__len__():
            for movie in movies:
                ogeler[tip.catetype] = movies
    
    if request.method == "POST":
        cardId = request.POST.get("listLike")
        cards = Card.objects.filter(id=int(cardId)).first()
        print("caard:", cardId)
        print(cards.like)
        if cards.like == False:
            cards.like =True
            cards.save()
        else:
            cards.like =False
            cards.save()
        
        return redirect('netflix')
            

    context = {
        "profile": profile,
        "category":category,
        "cards" : cards,
        "type": type,
        "dinamik_yapi": ogeler.items()
        }
    return render(request,'netflix-type.html',context)

def Favori(request):
    profile = Profile.objects.filter(loginp = True,user = request.user).first()
    category = Category.objects.all()
    card = Card.objects.all()
    type = Type.objects.all()
    
    ogeler = {}
    for tip in type:
        movies = Card.objects.filter(type=tip, like = True)
        if movies.__len__():
            for movie in movies:
                ogeler[tip.catetype] = movies
    
    if request.method == "POST":
        cardId = request.POST.get("listLike")
        cards = Card.objects.filter(id=int(cardId)).first()
        print("caard:", cardId)
        print(cards.like)
        if cards.like == False:
            cards.like =True
            cards.save()
        else:
            cards.like =False
            cards.save()
        
        return redirect('favori')
    context = {
        "profile": profile,
        "category":category,
        "card" : card,
        "type": type,
        "dinamik_yapi": ogeler.items()
    }
    return render(request,'favori.html',context)