from django.shortcuts import render, HttpResponse
from django.urls import reverse_lazy
from . import models
from django.views import generic
from django.contrib.messages.views import SuccessMessageMixin
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import send_mail
from django.views.generic.edit import FormView

# Create your views here.
def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def destinations(request):
    all_destinations = models.Destination.objects.all()
    return render(request, 'destinations.html', {'destinations': all_destinations})

def opinions(request):
    all_opinions = models.Opinions.objects.all()
    return render(request, 'opinions.html', {'opinions': all_opinions})

class DestinationDetailView(generic.DetailView):
    template_name = 'destination_detail.html'
    model = models.Destination
    context_object_name = 'destination'


class CruiseDetailView(generic.DetailView):
    template_name='cruise_detail.html'
    model = models.Cruise
    context_object_name = 'cruise'

class InfoRequestCreate(SuccessMessageMixin, generic.CreateView):
    template_name = 'info_request_create.html'
    model = models.InfoRequest
    fields = ['name', 'email', 'cruise', 'notes']
    success_url = reverse_lazy('index')
    success_message = 'Thank you, %(name)s! We will email you when we have more information about %(cruise)s!'

    def form_valid(self, form):
        # Call the parent class's form_valid() method to save the form data
        response = super().form_valid(form)

        # Send an email to the provided email address
        subject = 'Thank you for your information request'
        message = f'Thank you, {form.cleaned_data["name"]}! We will email you when we have more information about {form.cleaned_data["cruise"]}!'
        from_email = 'grupo8.relecloud@hotmail.com'  # Set your email address
        recipient_list = [form.cleaned_data['email']]
        
        send_mail(subject, message, from_email, recipient_list)

        # Return the original response
        return response

@method_decorator(csrf_exempt, name='dispatch')
class DestinationCreateView(generic.CreateView):
    model = models.Destination
    template_name = 'destination_form.html'
    fields = ['name', 'description']

@method_decorator(csrf_exempt, name='dispatch')
class DestinationUpdateView(generic.UpdateView):
    model = models.Destination
    template_name = 'destination_form.html'
    fields = ['name', 'description']

@method_decorator(csrf_exempt, name='dispatch')
class DestinationDeleteView(generic.DeleteView):
    model = models.Destination
    template_name = 'destination_confirm_delete.html'
    success_url = reverse_lazy('destinations')