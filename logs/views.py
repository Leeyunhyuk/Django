from django.shortcuts import render
from .models import LogEntry

def log_list(request):
    logs = LogEntry.objects.all()
    return render(request, 'logs/log_list.html', {'logs': logs})
