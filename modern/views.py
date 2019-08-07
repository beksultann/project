from django.shortcuts import render


def base(request):
    return render(request, 'modern/base.html')


def about(request):
    return render(request, 'modern/about.html')


def contact(request):
    return render(request, 'modern/contact.html')


def news(request):
    return render(request, 'modern/news.html')

def forum(request):
    return  render(request, 'modern/forum.html')
