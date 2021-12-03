from . import views
from django.urls import path


urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    # 'blank' = homepage
    path('<slug:slug>/',  views.PostDetail.as_view(), name='post_detail'),
    # slug 1 = path converter, info i bokmärke path converter
    # slug 2 = keyword, matches the slug parameter in get method
    # of PostDetail class in 
    # blog/views.py. Tha's how we link them together.
]