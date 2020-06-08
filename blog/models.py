from django.db import models
from django.contrib.auth.models import User
#from ckeditor.fields import RichTextField #富文本编辑器

from ckeditor_uploader.fields import RichTextUploadingField  #支持图片上传
#数据模型
class BlogType(models.Model):
    type_name = models.CharField(max_length=15)
    def __str__(self):
        return self.type_name
class Blog(models.Model):
    title = models.CharField(max_length=50)
    blog_type = models.ForeignKey(BlogType,on_delete=models.DO_NOTHING)
    #content = models.TextField()
    #content = RichTextField()  #使用富文本编辑器
    content = RichTextUploadingField()
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING)

    read_num = models.PositiveIntegerField(default=0, editable=False)  #18 阅读篇数计数

    created_time = models.DateTimeField(auto_now_add=True)
    last_updated_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "<Blog: %s>" % self.title
    class Meta:
    #分页排序
        ordering = ['-created_time'] #倒序排列博客列表
class Readnum(models.Model):#阅读计数字段
    read_nm = models.IntegerField(default=0)
    #blog = models.ForeignKey(Blog,on_delete=models.DO_NOTHING) #外键 一对多或者多对多
    blog = models.OneToOneField(Blog, on_delete=models.DO_NOTHING) #一对一
