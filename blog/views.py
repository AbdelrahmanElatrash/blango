from django.shortcuts import render, get_object_or_404, redirect
from blog.models import Post 
from django.utils import timezone
from blog.forms import CommentForm
# Create your views here.



def index(request):
    posts = Post.objects.filter(published_at__lte=timezone.now())
    return render(request,'blog/index.html', {'posts' : posts})


def post_detail(request,slug):
    post = get_object_or_404( Post, slug=slug)
    
    if request.user.is_active :
        if request.method == 'POST':
            # if method post handel form data
            comment_form = CommentForm(request.POST)   # create comment instance
            if comment_form.is_valid() : # check if form data is valid
                # save the form without saving in data base using commit=False (sesion with DB not close) , instead it will return it
                comment = comment_form.save(commit=False)
                # add another attribute content_object and creater
                comment.content_object = post # the current Post being viewed
                comment.creater = request.user  # the current logged in user
                
                comment.save() 
                
                # redirect back to the current Post(this essentially just refreshes the page)
                return redirect(request.path_info)
             
        
        # if method is not post return blank form
        else :
            comment_form = CommentForm()
    # if user not active dont show form
    else :
        comment_form = None
    
    # adjust the render call to include the comment_formvariable
    return render(request,'blog/post-detail.html', {'post':post , 'comment_form': comment_form})
    
