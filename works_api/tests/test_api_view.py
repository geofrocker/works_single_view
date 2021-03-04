from io import StringIO
from django.core.management import call_command
from django.test import TestCase
from django.urls import reverse


class ApiViewTestCase(TestCase):
    def setUp(self):
        out = StringIO()
        call_command('ingest', 'works_metadata.csv',  stdout=out)

    def test_user_can_get_a_record_by_iswc(self):
        url = reverse("api_view", args=["T9204649558"])
        response = self.client.get(url)
        self.assertContains(response, "Edward")

    def test_404_unavailable_record(self):
        url = reverse("api_view", args=["XXXXXXX"])
        response = self.client.get(url)
        self.assertEquals(response.status_code, 404)
