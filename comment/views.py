from django.shortcuts import render
# 引入 UserRegisterForm 表单类
from  django.urls import reverse
from django.shortcuts import render,redirect,HttpResponse
from django.contrib import auth
from comment import models
from django.http import JsonResponse

from .models import Comment
from .forms import CommentForm
from django.contrib.contenttypes.models import ContentType


def update_comment(request):
    user = request.user
    text = request.POST.get('text','')
    content_type = request.POST.get('content_type','')
    object_id = int(request.POST.get('object_id',''))

    model_class = ContentType.objects.get(model=content_type).model_class()
    model_obj = model_class.objects.get(pk=object_id)

    comment = Comment()
    comment.user = request.user
    comment.text = text
    comment.content_object = model_obj
    comment.save()
    referer = request.META.get('HTTP_REFERER', reverse('home'))
    return redirect(referer)  #评论成功后重定向返回原来的路径