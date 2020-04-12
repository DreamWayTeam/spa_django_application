from django.urls import path
from .views import index_page, contact_page, about_page, portfolio_page, services_page

app_name = 'spa'

urlpatterns = [
    path('', index_page, name='index'),
    path('contact/', contact_page, name='contact'),
    path('about/', about_page, name='about'),
    path('portfolio/', portfolio_page, name='portfolio'),
    path('services/', services_page, name='services'),
]
