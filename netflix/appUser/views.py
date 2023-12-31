from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages
from django.contrib.auth.models import User
from .models import *
import random

def subscribeUser(request):
    if request.method == "POST":
        submit = request.POST.get("submit")
        if submit == "subscribeButton":
            request.user.userinfo.subscribe = True
            request.user.userinfo.save()
            messages.success(request,"Aboneliğiniz başarıyla oluşturuldu")
            return redirect("profileUser")
    context = {}
    return render(request,'subscribe.html',context)
    
def profileUser(request):
    profile_list = Profile.objects.filter(user = request.user)
    if request.method == "POST":
        submit = request.POST.get("submit") #buttonu burada çekiyoruz
        
        if submit == "profileLogin":
            pid = request.POST.get("id")
            profile = get_object_or_404(Profile,id=pid)    
            profile_list.update(loginp = False) # profillerin hepsinden çıkış yaptırtıyo
            # for i in profile_list: # yukarıdaki update metoduyla aynı çalışır
            #     i.loginp =False
            #     i.save()
            profile.loginp = True # tıklanan profilin girişini yapıyor
            profile.save()
            return redirect("netflix")
    #Profil Ekleme Start !!!!!!!!!!!!!
        if submit == "profileCreate":
            if len(profile_list) < 4:
                pname = request.POST.get("pname")
                image = request.FILES.get("image")
                
                if pname.strip(" ") == "" or profile_list.filter(name = pname).exists():
                    messages.warning(request, "Profile adını giriniz yada değiştiriniz")
                    return redirect("profileUser")
                
                profile = Profile(name = pname,image = image, user = request.user) # request.user girişli kullanıcıyı verir!!!!!
                if image is None:
                    profile.image = "profile/smile-icon.jpg"
                profile.save()
            else:
                messages.warning(request,"Maximum profil sayısına ulaştınız")
        #Profile Düzenleme Start    
        elif submit == "profileChange":
            pname2 = request.POST.get("pname2")
            image2 = request.FILES.get("image2")
            pid = request.POST.get("id")
            
            if pname2.strip(" ") == "" or profile_list.filter(name = pname2).exists():
                messages.warning(request, "Profile adını giriniz yada değiştiriniz")
                return redirect("profileUser")
            
            profile2 = profile_list.get(id=pid)
            profile2.name = pname2
            if image2 is not None:
                profile2.image = image2
            profile2.save()
        #Profile Düzenleme Start    
        #Profile Silme Start    
        elif submit == "profileDelete":
            pid = request.POST.get("id")
            profile = get_object_or_404(Profile, id = pid)
            profile.delete()
        #Profile Silme End
    #Profil Ekleme End !!!!!!!!!!!!!
        return redirect("profileUser")
    context = {
        "profile_list" :profile_list,
    }
    return render(request,'browse.html',context)

# def deleteProfileUser(request,id):
#     # profile = Profile.objects.filter(id=id).first() #hatasız çekme işlemi yapar
#     profile = get_object_or_404(Profile,id=id) # get ile aynıdır çekemediği durumda 404 sayfasına yönlendirir !!!!!
#     profile.delete()
#     return redirect("profileUser")

def accountUser(request):
    profile = Profile.objects.filter(loginp=True,user=request.user).first()
    user = User.objects.filter(username = request.user).first()

    # request.user.check_password()
    # user.check_password() password doğrulama

    if request.method == "POST":
        submit = request.POST.get("submit")
        
        if submit == "subscribeUnfollow":
            user.userinfo.subscribe = False
            user.userinfo.save()
            messages.warning(request,"Üyeliğiniz iptal edildi!!!")
            return redirect('subscribeUser')
        
        
        elif submit == "passwordUpdate":
            password = request.POST.get("password")
            password1 = request.POST.get("password1")
            password2 = request.POST.get("password2")

            if user.check_password(password) and password1 == password2:
                user.userinfo.password = password1
                user.userinfo.save()

                user.set_password(password1)
                user.save()
                return redirect('loginUser')
            else:
                messages.warning(request,"Şifreniz yanlış veya yeni şifreler aynı değil!!!")
        elif submit == "telUpdate":
            tel = request.POST.get("tel")
            password = request.POST.get("password")

            if user.check_password(password):
                user.userinfo.tel = tel
                user.userinfo.save()
            else:
                messages.warning(request,"Şifre yanlış!!")
        elif submit == "emailUpdate":
            email = request.POST.get("email")
            password = request.POST.get("password")
            
            #1. Yöntem
            email_bool = True
            if User.objects.filter(email = email).exists(): #filter ile gelen bir değer varsa True yoksa False
                email_bool = False
                messages.warning(request,"Bu email zaten kullanılıyor")

            if user.check_password(password):
                if email_bool:
                    user.email = email
                    user.save()
            else:
                messages.warning(request,"Şifre yanlış!!!")
            #2. Yöntem   
            # if user.check_password(password): # kullanıcıdan alınan password doğruysa True döndürür
            #     if not User.objects.filter(email=email).exists():
            #         user.email = email
            #         user.save()
            #     else:
            #         messages.warning(request,"Bu email zaten kullanılıyor!!!")
            # else:
            #     messages.warning(request,"Şifreniz yanlış!!!")
        return redirect("accountUser")
                
        
    context = {
        "profile":profile,
    }
    return render(request,'hesap.html',context)

def loginUser(request):
    context = {}
    if request.method == "POST":
        print(request.POST)
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(username=username,password=password) # kullanıcı varsa kullanıcı adını yoksa None değeri döndürür
        
        if user is not None:  # === if user != None 
            login(request,user)
            if user.userinfo.subscribe:
                return redirect("profileUser")
            return redirect('subscribeUser')
        else:
            # context.update({"hata":"Kullanıcı adı veya şifre yanlış!"})
            messages.warning(request,"Kullanıcı adı veya şifre yanlış!")
            return redirect('loginUser')
    
    return render(request,'login.html',context)

def registerUser(request):
    context = {}
    #kullanıcı önerme eklenecek
    if request.method == "POST":
        fname = request.POST.get("fname")
        lname = request.POST.get("lname")
        email = request.POST.get("email")
        username = request.POST.get("username")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")

        password_bool = email_bool = username_bool = True
        
        if password1 != password2 :
            password_bool = False
            messages.warning(request,"Şifreler aynı değil!")
            
        if User.objects.filter(email = email).exists(): #exists list içerisinde obje varsa True yoksa False döndürür
            email = False
            messages.warning(request,"Bu email zaten kullanılıyor!")

        if User.objects.filter(username = username).exists(): #exists liste içerisi boşsa None döndürür
            username_bool = False
            
            infolist = []
            i=0
            
            while i<20:
                usernew = username
                i += 1
                if len(infolist) >= 3:
                    break
                
                lettercount = random.choice([1,2,3])
                for j in range(lettercount):
                    letterRandom = random.randint(0,9) #0-9 adarsı rastgele sayı verir
                    usernew += str(letterRandom)

                
                if (usernew not in infolist) and (not User.objects.filter(username=usernew).exists()):
                    infolist.append(usernew)
                    messages.info(request, usernew)
                    
            messages.warning(request,"Kullanıcı adı veya şifre yanlış!")           

        if password_bool and email_bool and username_bool:
            user = User.objects.create_user(first_name = fname,last_name = lname,email = email,username=username,password=password1) # obje oluştur
            user.save() #objeyi yani kullanıcıyı kaydet

            userinfo = Userinfo(user = user,password = password1)
            userinfo.save()
        
            return redirect("loginUser")
        
        
    return render(request,'register.html',context)

def logoutUser(request):
    logout(request)
    return redirect("indexPage")