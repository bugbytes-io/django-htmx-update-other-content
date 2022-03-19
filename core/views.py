from django.shortcuts import render

# Create your views here.
def event_detail(request, pk):
    context = {}
    return render(request, 'core/subscribe.html', context)