from django.contrib.auth import get_user_model
from django import template 
from django.utils.html import format_html 
from django.utils.safestring import mark_safe
from blog.models import Post

register = template.Library()

@register.simple_tag(takes_context=True)
def author_details(context):
    
    request = context['request']
    current_user = request.user
    post = context["post"]
    author = post.author
    
    if not isinstance(author , get_user_model()):
        return ""
    
    if author == current_user:
        return format_html('<strong>me</strong>')
    
    elif author.first_name and author.last_name :
        name = f'{author.first_name} {author.last_name}'
    else :
        name = author.username
        
    if author.email:
        # email = escape(author.email)
        prefix = format_html('<a href="mailto:{}">',author.email)
        suffix = format_html("</a>")
    else :
        prefix = ""
        suffix = ""
        
    return format_html('{} {} {}',prefix,name,suffix)


@register.simple_tag()
def row(extra_classes=""):
    
    return format_html('<div class="row" {}>', extra_classes)
    
    
@register.simple_tag()
def endrow():
    
    return format_html("</div>")

@register.inclusion_tag('blog/post-list.html')
def recent_posts(post):
    posts = Post.objects.exclude(pk=post.pk) [:5]
    return {'title':"Recent Posts" , 'posts':posts}


@register.simple_tag()
def col(extra_classes=""):
    return format_html('<div class="col" {}>', extra_classes)

@register.simple_tag()
def endcol():
    return format_html("</div>")