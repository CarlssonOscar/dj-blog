from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Post


class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by("-created_on")
    template_name = "index.html"
    paginate_by = 6
    # Means paginate just means separate into pages.
    # By setting paginate_by to six, we're limiting the  number of
    #  posts that can appear on the front page, if there are more
    #  than six then Django  will automatically add page navigation

class PostDetail(View):

    def get(self, request, slug, *args, **kwargs):
        # First, we'll filter all of our posts so that
        # we  only have the active ones with status set to one.
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by(created_on)
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True
        
        return render (
            request,
            'post_detail.html',
            {
                'post': post,
                'comments': comments,
                'liked': liked
            }
        )
