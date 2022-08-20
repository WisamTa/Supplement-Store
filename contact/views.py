from django.shortcuts import render
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings
from django.contrib import messages


from .forms import ContactForm


def contact(request):
    """
    A view that renders contact page
    """
    cust_email = request.POST.get('contact_email')

    if request.method == 'POST':
        contact_form = {
            'name': request.POST.get('name'),
            'email': request.POST.get('contact_email'),
            'contact_as': request.POST.get('contact_as'),
            'message': request.POST.get('message')
            }
        subject = render_to_string(
            'contact/contact_emails/contact_email_subject.txt',
            {'contact': contact_form}
        )
        body = render_to_string(
            'contact/contact_emails/contact_email_body.txt',
            {'contact': contact_form}
        )
        send_mail(
            subject,
            body,
            cust_email,
            [settings.DEFAULT_FROM_EMAIL]
        )
        messages.success(request, 'Your message was sent to us!')

    form = ContactForm

    context = {
        'form': form
    }

    return render(request, 'contact/contact.html', context)
