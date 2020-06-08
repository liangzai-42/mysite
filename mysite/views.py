from django.shortcuts import render,redirect
from django.contrib import auth
from  django.urls import reverse #反向解析
from .forms import LoginForm
from  .forms import RegForm
from django.contrib.auth.models import User
def home(request):
    context = {},
    return render(request,'home.html')

def login(request):
    # username=request.POST.get('username','')
    # password= request.POST.get('password', '')
    # user = auth.authenticate(request, username=username, password=password)
    # referer=request.META.get('HTTP_REFERER',reverse('home')) #反向解析路径
    # if user is not None:
    #     auth.login(request, user)
    #     #return redirect('/')  #重定向 登录成功就跳转到首页
    #     return redirect(referer)
    # else:
    #     return render(request,'error.html', {'message': '用户名或密码不正确'}) #没有则跳转到错误页面错误页面

    #提交数据操作
    # if request.method == 'GET':
    #     return render(request, 'login.html',{})
    if request.method == 'POST':
        login_form = LoginForm(request.POST) #得到了提交的数据
        if login_form.is_valid():   #判断是否有效
            username = login_form.cleaned_data['username'] #cleaned_data 为包含字段信息的字典
            password = login_form.cleaned_data['password']
            user = auth.authenticate(username=username, password=password)  #检查是否正确
            if user is not None:
                auth.login(request,user)
                #return redirect('/')  #重定向 登录成功就跳转到首页
                return redirect(request.GET.get('form',reverse('home')))
            else:
                login_form.add_error(None,'用户名或者密码不正确')
                context={}
                context['login_form'] = login_form
                return render(request, 'login.html',context)
        else:
            pass
    else:
        login_form = LoginForm()
        context = {}
        context['login_form'] = login_form
        return render(request, 'login.html', context)

#用户注册
def register(request):
    if request.method == 'POST':
        reg_form = RegForm(request.POST)
        if reg_form.is_valid():
            username = reg_form.cleaned_data['username']
            email = reg_form.cleaned_data['email']
            password = reg_form.cleaned_data['password']
            # 创建用户
            user = User.objects.create_user(username, email, password)
            user.save()
            # 登录用户
            user = auth.authenticate(username=username, password=password)
            auth.login(request, user)
            return redirect(request.GET.get('from', reverse('home')))
    else:
        reg_form = RegForm()

    context = {}
    context['reg_form'] = reg_form
    return render(request, 'register.html', context)





