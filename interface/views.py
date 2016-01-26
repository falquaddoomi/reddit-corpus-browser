from django.http import HttpResponseRedirect
from django.shortcuts import render

from interface.corpus_models import Subreddits, CommentsAbridged
from interface.languagetools import ling_coordination


def subreddits(request):
    # grab the top 100 significant subreddits
    ctx = {
        'subreddits': Subreddits.objects
                          .order_by('-postcount')[:100]
    }

    return render(request, template_name="views/subreddits.html", context=ctx)


def topics(request, subreddit):
    topic_sort_order = request.session.get('topic_sort_order', '-created_utc')

    ctx = {
        'chosen_subreddit': Subreddits.objects.get(subreddit=subreddit),
        'topics': CommentsAbridged.objects
                      .filter(subreddit=subreddit)
                      .order_by(topic_sort_order)
                      .values_list('link_id', flat=True)[:100]
    }

    return render(request, template_name="views/subreddits.html", context=ctx)


def topic_posts(request, subreddit, topic_id):
    topic_sort_order = request.session.get('topic_sort_order', '-created_utc')
    sort_order = request.session.get('sort_order', '-score')

    post_set = CommentsAbridged.objects \
        .filter(subreddit=subreddit, link_id=topic_id) \
        .order_by(sort_order)

    tops = treeify(post_set, add_liwc=request.session.get('enable_liwc', True))

    ctx = {
        'chosen_subreddit': Subreddits.objects.get(subreddit=subreddit),
        'topics': CommentsAbridged.objects
                      .filter(subreddit=subreddit)
                      .order_by(topic_sort_order)
                      .values_list('link_id', flat=True)[:100],
        'chosen_topic': CommentsAbridged.objects
            .filter(subreddit=subreddit, link_id=topic_id).order_by('created_utc')[0],
        'posts': post_set,
        'root_posts': tops
    }

    return render(request, template_name="views/subreddits.html", context=ctx)


def change_sorting(request):
    request.session['sort_order'] = request.POST.get('sort_order', '-score')
    request.session['enable_liwc'] = 'enable_liwc' in request.POST
    return HttpResponseRedirect(request.POST['next'])


def change_topic_sorting(request):
    request.session['topic_sort_order'] = request.POST.get('topic_sort_order', 'created_utc')
    return HttpResponseRedirect(request.POST['next'])


# ==============================================================================================================
# === miscellaneous utilities, e.g. tree creation
# ==============================================================================================================

def treeify(post_set, add_liwc=True, build_turns=True):
    """
    Takes in a post_set of CommentsAbridged models and processes them into a tree in-memory.
    :param build_turns: create LIWC fractions for each conversational turn; requires LIWC to be enabled
    :param add_liwc: inserts the LIWC analysis for each post into the post metadata
    :param post_set: a QuerySet of CommentsAbridged models
    :return: a list of root comment entities that contain each post as a 'payload', and the child posts in 'children'
    """
    nodes = {}
    tops = []

    for post in post_set:
        liwc_data = dict(ling_coordination.get_matches(post.body)) if add_liwc else None
        nodes[post.name] = {'payload': post, 'liwc': liwc_data, 'children': [], 'depth': 1}

    for post in post_set:
        if post.parent_id in nodes:
            nodes[post.parent_id]['children'].append(nodes[post.name])
        else:
            tops.append(nodes[post.name])

    # traverse each root to find the conversational turns
    if add_liwc and build_turns:
        for top in tops:
            top['turns'] = []

            def add_kids(cur, depth):
                top['turns'].append({'first': nodes[cur['payload'].parent_id], 'second': cur})
                cur['depth'] = depth
                for curkid in cur['children']:
                    add_kids(curkid, depth+1)

            for kid in top['children']:
                add_kids(kid, top['depth']+1)

    return tops
