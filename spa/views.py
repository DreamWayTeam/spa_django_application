from django.conf import settings
from django.shortcuts import render


def index_page(request):
    context = {
        'title': settings.SITE_TITLE,
        'logo': settings.LOGO_TILE
    }
    return render(request, 'pages/index.html', context)


def contact_page(request):
    context = {
        'title': settings.SITE_TITLE
    }
    return render(request, 'pages/contact.html', context)


def about_page(request):
    context = {
        'title': settings.SITE_TITLE
    }
    return render(request, 'pages/about.html', context)


def portfolio_page(request):
    context = {
        'title': settings.SITE_TITLE
    }
    return render(request, 'pages/portfolio.html', context)


def services_page(request):
    context = {
        'title': settings.SITE_TITLE
    }
    return render(request, 'pages/services.html', context)
