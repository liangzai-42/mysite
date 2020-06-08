from django.contrib import admin
from django.urls import include,path
#from blog.views import blog_list
from blog.views import blog_list
from blog.views import blog_detail
from blog.views import blogs_with_type
from django.conf import  settings
from django.conf.urls.static import static
#from comment.views import page
#from  comment.views import  post_comment
from . import  views
from comment.views import update_comment
urlpatterns = [
    path('', views.home,name='home'),
    path('blog/', blog_list, name='blog_list'),
    path('admin/',admin.site.urls),
    path('blog/<int:blog_pk>',blog_detail, name="blog_detail"),
    path('blog/type/<int:blog_type_pk>', blogs_with_type, name="blogs_with_type"),
    path('ckeditor', include('ckeditor_uploader.urls')),
    path('login/',views.login,name="login"),#用户登录
    #path('comment/',page, name='comment'),
    path('register/',views.register, name='register'),
    path('comment/update_comment', update_comment, name='update_comment')
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)