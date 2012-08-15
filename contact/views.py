# Create your views here.
from django.shortcuts import render_to_response
from contact.models import ContactForm
from django.core.mail import send_mail
from django.http import HttpResponseRedirect

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            send_mail(
                cd['subject'],
                cd['message'],
                cd.get('email', 'whayutin@redhat.com'),
                ['whayutin@redhat.com'],
            )
            return HttpResponseRedirect('/contact/thanks/')
    else:
        form = ContactForm(
                           initial={'subject': 'I love your site!'}
                )
    return render_to_response('contact_form.html', {'form': form})
