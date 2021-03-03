from io import StringIO
from django.core.management import call_command
from django.test import TestCase
from django.urls import reverse


class SingleViewTestCase(TestCase):
    def setUp(self):
        out = StringIO()
        call_command('ingest', 'works_metadata.csv',  stdout=out)
    url = reverse("home")

    def test_user_can_see_the_reconciled_records(self):
        response = self.client.get(self.url)
        self.assertContains(response, "Edward")
