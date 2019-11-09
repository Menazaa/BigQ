from django import forms
from django.core.mail import send_mail
import logging


logger = logging.getLogger(__name__)


class ContactForm (forms.Form):
    name = forms.CharField(label='Name', max_length=200, required=True)
    email = forms.EmailField(label='Email', required=True)
    message = forms.CharField(label='Message', max_length=2000, widget=forms.Textarea, required=True)

    def send_mail(self):
        logger.info("Sending email to customer service")
        message = "From {0} \nEmail: {1} \nMessage:\n   {2}".format(
            self.cleaned_data['name'],
            self.cleaned_data['email'],
            self.cleaned_data['message']
        )
        send_mail(
            "Site message",
            message,
            "site@BigQ.domain",
            ["customerservice@booktime.domain"],
            fail_silently=False,
        )
