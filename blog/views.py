from django.shortcuts import render, get_object_or_404
from .models import Blog, BlogType
from  django.core.paginator import Paginator #分页器


from comment.models import Comment  #引入模板
from comment.forms import CommentForm   #添加评论的 form表单
from django.contrib.contenttypes.models import ContentType
def blog_list(request):
    blogs_all_list = Blog.objects.all()
    paginator = Paginator(blogs_all_list, 2)  # 每10页进行分页
    page_num = request.GET.get('page', 1)  # 获取url的页码参数（GET请求）
    page_of_blogs = paginator.get_page(page_num)


    context = {}
    #context['blogs'] = blogs_all_list
    context['page_of_blogs'] = page_of_blogs
    context['blog_types'] = BlogType.objects.all()
    return render(request,'blog/blog_list.html', context)


def blog_detail(request,blog_pk):
    blog=get_object_or_404(Blog,pk=blog_pk)

    # 渲染评论模板
    blog_content_type = ContentType.objects.get_for_model(blog)
    comments = Comment.objects.filter(content_type=blog_content_type, object_id=blog.pk)

    if not request.COOKIES.get('blog_%s_read' % blog_pk):  #如果cookiet有记录则表示被记录过（被阅读过），没有值则表示没有被记录，所以执行阅读加1
        blog.read_num+=1   #统计阅读的次数 阅读后自动加1
        blog.save()

    context = {}
    context['previous_blog'] = Blog.objects.filter(created_time__gt=blog.created_time).last()
    context['next_blog'] = Blog.objects.filter(created_time__lt=blog.created_time).first()
    context['blog'] = get_object_or_404(Blog, pk=blog_pk)
    ####实例化评论模板
    context['comments'] = comments
    context['comment_form'] = CommentForm(initial={'content_type': blog_content_type.model, 'object_id': blog_pk})

    response= render(request,'blog/blog_detail.html',context)   #响应
    response.set_cookie('blog_%s_read' % blog_pk, 'true') #cookie 记录阅读次数 并在指定时间内同一个用户阅读不再计数
    return  response



def blogs_with_type(request,blog_type_pk):
    context = {}
    blog_type = get_object_or_404(BlogType, pk=blog_type_pk)
    context['blogs'] = Blog.objects.filter(blog_type=blog_type)
    context['blog_type']=blog_type
    return render(request,"blog/blogs_with_type.html",context)