from django.shortcuts import render
from django.http import JsonResponse
from .models import Message

# Submit Message
def submit_message(request):
    if request.method == 'POST':
        sender = request.POST.get('sender')
        recipient = request.POST.get('recipient')
        content = request.POST.get('content')
        message = Message(sender=sender, recipient=recipient, content=content)
        message.save()
        return JsonResponse({'status': 'Message saved successfully'})
    
    return render(request, 'submit_message.html')

# Get Messages
def get_messages(request):
    if request.method == 'GET':
        sender = request.GET.get('sender')
        messages = Message.objects.filter(sender=sender).order_by('-timestamp')[:20]
        data = [
            {
                'sender': msg.sender,
                'recipient': msg.recipient,
                'content': msg.content,
                'timestamp': msg.timestamp
            } for msg in messages
        ]
        return JsonResponse({'messages': data})
