from django.test import TestCase
from django.urls import reverse
from main import forms

class TestPage(TestCase):
    def test_home_page(self):
        respose = self.client.get(reverse('home'))
        self.assertEqual(respose.status_code,200)
        self.assertTemplateUsed(respose, 'home.html')
        self.assertContains(respose, 'BigQ')

    def test_about_us_page(self):
        respose = self.client.get(reverse('about_us'))
        self.assertEqual(respose.status_code, 200)
        self.assertTemplateUsed(respose, 'about_us.html')
        self.assertContains(respose, 'BigQ')

    def test_contact_us_page_works(self):
        response = self.client.get(reverse("contact_us"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'contact_form.html')
        self.assertContains(response, 'BigQ')
        self.assertIsInstance(
        response.context["form"], forms.ContactForm
    )

