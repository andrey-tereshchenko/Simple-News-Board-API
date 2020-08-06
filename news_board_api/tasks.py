from __future__ import absolute_import, unicode_literals

from celery import shared_task

from news_board_api.models import Post


@shared_task
def reset_all_user_upvote_task():
    posts = Post.objects.all()
    for post in posts:
        post.user_upvote.clear()
    print('All posts upvote had been reset')
