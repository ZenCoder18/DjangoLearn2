from django.test import TestCase, SimpleTestCase
from django.urls import reverse

class HomepageTests(SimpleTestCase):
    def test_url_available(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
    
    def test_url_available_by_name(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)

    def test_template_used(self):
        response = self.client.get(reverse("home"))
        self.assertTemplateUsed("home.html")
    
    def test_template_content_used(self):
        response = self.client.get(reverse("home"))
        self.assertContains(response, "<h1>Home Page</h1>")

class AboutpageTests(SimpleTestCase):
    def testAbout(self):
        response = self.client.get("/about/")
        self.assertEqual(response.status_code, 200)