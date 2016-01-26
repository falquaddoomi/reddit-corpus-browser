from django.conf.urls import url
from django.views.generic import RedirectView

from . import views

urlpatterns = [
    url(r'^$', RedirectView.as_view(url='/subreddits/')),
    url(r'^subreddits/$', views.subreddits, name='subreddits'),
    url(r'^subreddits/(?P<subreddit>.+)/topics/$', views.topics, name='sub_topics'),
    url(r'^subreddits/(?P<subreddit>.+)/topics/(?P<topic_id>.+)/posts/$', views.topic_posts, name='sub_topic_thread'),

    # session manipulating methods
    url(r'^options/sort_order/$', views.change_sorting, name='change_sorting'),
    url(r'^options/topic_sort_order/$', views.change_topic_sorting, name='change_topic_sorting'),
]
