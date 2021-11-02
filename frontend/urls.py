from django.urls import path
from .views import IndexTemplateView, ContactTemplateView, ServiceTemplateView

urlpatterns = [
    path('', IndexTemplateView.as_view(), name='home'),
    path('contact/', ContactTemplateView.as_view(), name='contact'),
    path('service/', ServiceTemplateView.as_view(), name='service'),
]