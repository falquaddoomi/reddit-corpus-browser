from django.conf.urls import url
from django.views.generic import RedirectView

from interface.views import subreddit_views

urlpatterns = [
    url(r'^$', RedirectView.as_view(url='/subreddits/')),
    url(r'^subreddits/$', subreddit_views.subreddits, name='subreddits'),
    url(r'^subreddits/(?P<subreddit>.+)/topics/$', subreddit_views.topics, name='sub_topics'),
    url(r'^subreddits/(?P<subreddit>.+)/topics/(?P<topic_id>.+)/posts/$', subreddit_views.topic_posts, name='sub_topic_thread'),

    # session manipulating methods
    url(r'^options/sort_order/$', subreddit_views.change_sorting, name='change_sorting'),
    url(r'^options/topic_sort_order/$', subreddit_views.change_topic_sorting, name='change_topic_sorting'),
]
