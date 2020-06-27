from django.shortcuts import render
from django.utils import timezone
from .models import Post

"""
In the render function we have one parameter request (everything we receive from the user via the Internet) 
and another giving the template file ('blog/post_list.html'). 
The last parameter, {}, is a place in which we can add some things for the template to use: {'posts': posts}
posts is the name of our query set
"""
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

