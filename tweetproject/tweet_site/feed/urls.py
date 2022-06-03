from django.urls import path
from .import views
from .views import TweetListView,TweetCreateView

urlpatterns = [
    path('',TweetListView.as_view(), name = 'home'),
    path('home/',TweetListView.as_view(), name = 'home'),
    path('create/',TweetCreateView.as_view(), name = 'tweetcreate'),
]