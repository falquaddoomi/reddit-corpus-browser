from django.http import HttpResponseRedirect
from django.shortcuts import render

from interface.corpus_models import Subreddits, CommentsAbridged, SubredditTopics

def users(request):
    # grab the top 100 significant subreddits
    ctx = {
        'users': CommentsAbridged.objects
                          .order_by('-postcount')[:100]
    }

    return render(request, template_name="views/subreddits.html", context=ctx)
