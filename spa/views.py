from django.conf import settings
from django.shortcuts import render

BASE_CONTEXT = {
        'title': settings.SITE_TITLE,
        'logo': settings.LOGO_TILE
    }


def index_page(request):
    context = BASE_CONTEXT.copy()
    return render(request, 'pages/index.html', context)


def contact_page(request):
    context = BASE_CONTEXT.copy()
    return render(request, 'pages/contact.html', context)


def about_page(request):
    context = BASE_CONTEXT.copy()
    return render(request, 'pages/about.html', context)


def portfolio_page(request):
    context = BASE_CONTEXT.copy()
    return render(request, 'pages/portfolio.html', context)


def services_page(request):
    context = BASE_CONTEXT.copy()
    return render(request, 'pages/services.html', context)
