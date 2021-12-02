from . import views
from django.urls import path


urlpatterns = [
    # 'blank' = homepage
    path('', views.PostList.as_view(), name='home')
]