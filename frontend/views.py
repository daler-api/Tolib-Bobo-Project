from django.views.generic import *

# Create your views here.
from core.models import Service


class IndexTemplateView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['services'] = Service.objects.all()
        return context


class ContactTemplateView(TemplateView):
    template_name = 'contact-us.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['services'] = Service.objects.all()
        return context


class ServiceTemplateView(TemplateView):
    template_name = 'service.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        service_id = self.request.GET.get('service_id')
        context['services'] = Service.objects.all()
        if service_id:
            context['service'] = Service.objects.get(id=service_id)
        return context