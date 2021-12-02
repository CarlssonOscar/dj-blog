from django.shortcuts import render
from django.views import generic
from .models import Post


class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    # Means paginate just means separate into pages.  
    # By setting paginate_by to six, we're limiting the  number of
    #  posts that can appear on the front page, if there are more
    #  than six then Django  will automatically add page navigation
    paginate_by = 6