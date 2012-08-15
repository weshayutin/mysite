from django.shortcuts import redirect, render
from django.core.mail import mail_admins
from ajaxContact.models import ContactForm
from django.conf import settings

def contact_form(request):
    if request.POST:
        form = ContactForm(request.POST)
        if form.is_valid():
            message = "From: %s <%s>\r\nSubject:%s\r\nMessage:\r\n%s\r\n" % (
                form.cleaned_data['name'],
                form.cleaned_data['email'],
                form.cleaned_data['subject'],
                form.cleaned_data['message'],
                #form.cleaned_data.get('email', 'whayutin@redhat.com'), ['whayutin@redhat.com']
            )
            mail_admins('Contact form', message, fail_silently=False)
            if request.is_ajax():
                if getattr(settings, 'DEBUG', False): # only if DEBUG=True
                    import time
                    time.sleep(5) # delay AJAX response for 5 seconds
                return render(request, 'contact/thanks.html')
            else:
                return redirect('contact/thanks.html')
    else:
        form = ContactForm()

    return render(request, 'contact/form.html', {'form':form})
