<<<<<<< HEAD
from events.models import Message

def unread_message_count(request):
    if request.user.is_authenticated:
        count = Message.objects.filter(receiver=request.user, is_read=False).count()
        return {'unread_message_count': count}
    return {'unread_message_count': 0}
=======
from events.models import Message

def unread_message_count(request):
    if request.user.is_authenticated:
        count = Message.objects.filter(receiver=request.user, is_read=False).count()
        return {'unread_message_count': count}
    return {'unread_message_count': 0}
>>>>>>> ce9b6cf0d7419a255b6a02052dd9479b3d9629be
