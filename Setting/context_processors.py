from django.db.models import Count, Q
from django.db.models.functions.datetime import TruncMonth, TruncYear

from App.models import Category, Tag, Post


def common(request):
    context = {
        'categories': Category.objects.annotate(
            num_posts=Count('post', filter=Q(post__is_public=True))),
        'tags': Tag.objects.annotate(
            num_posts=Count('post', filter=Q(post__is_public=True))),
        'history': Post.objects.values('created_at__date')\
            .annotate(count=Count('id', filter=Q(is_public=True))).values('created_at__date', 'count').order_by('created_at__date')
    }
    return context