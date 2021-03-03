from io import StringIO
from django.core.management import call_command
from django.test import TestCase

from ..management.commands.ingest import SUCCESS_TEXT
from works.models import (
    Contributor,
    WorksMetadata
)


class IngestTestCase(TestCase):
    def test_command_output(self):
        out = StringIO()
        call_command('ingest', 'works_metadata.csv', stdout=out)
        self.assertIn(SUCCESS_TEXT, out.getvalue())

    def test_no_duplicate_metadata(self):
        out = StringIO()
        call_command('ingest', "works_metadata.csv", stdout=out)
        initial_record_count = WorksMetadata.objects.all().count()
        call_command('ingest', "works_metadata.csv", stdout=out)
        final_record_count = WorksMetadata.objects.all().count()
        self.assertEquals(initial_record_count, final_record_count)

    def test_no_duplicate_contributors(self):
        out = StringIO()
        call_command('ingest', "works_metadata.csv", stdout=out)
        initial_record_count = Contributor.objects.all().count()
        call_command('ingest', "works_metadata.csv", stdout=out)
        final_record_count = Contributor.objects.all().count()
        self.assertEquals(initial_record_count, final_record_count)

