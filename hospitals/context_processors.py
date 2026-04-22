from .models import Contact


def unread_queries(request):
    """Make unread query count available in all admin templates."""
    if request.user.is_authenticated and request.user.is_staff:
        return {'unread_query_count': Contact.objects.filter(is_read=False).count()}
    return {}
