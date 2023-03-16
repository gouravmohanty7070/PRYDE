
from django.urls import path
from .views import forumPage, addComment, knowMore, blogPage, youMatter, chatBot, conversation

urlpatterns = [
    path('forum/', forumPage, name="forumPage"),
    path('addComment/', addComment),
    path('knowmore/', knowMore),
    path('blogs/', blogPage, name='blogPage'),
    path('youMatter/', youMatter, name='youMatter'),
    path('prydebot/', chatBot),
    path('conversation/', conversation, name='conversation'),
    # path('videoCall/', videoCall)
]

