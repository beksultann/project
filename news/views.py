from django.shortcuts import render

from .models import New


def newss(request):
    news = New.objects.all()
    context = {
        'news': news,
    }
    return render(request, 'modern/news.html', context)
