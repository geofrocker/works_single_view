import csv
from django.db.models import Q
from django.core.management.base import BaseCommand, CommandError

from works.models import (
    WorksMetadata,
    Contributor
)


class Command(BaseCommand):
    help = 'Matching and reconcile metadata'

    def add_arguments(self, parser):
        parser.add_argument('paths', nargs='+', type=str)

    def handle(self, *args, **options):
        for path in options['paths']:
            with open(path) as f:
                reader = csv.reader(f)
                next(reader, None)
                for row in reader:
                    input_contributors_names = row[1].split("|")
                    _create_missing_contributors(input_contributors_names)
                    db_contributors = Contributor.objects.filter(
                        name__in=input_contributors_names)
                    input_title = row[0]
                    input_iswc = row[2]
                    try:
                        metadata = WorksMetadata.objects.get(
                            Q(iswc=input_iswc) | Q(title__in=input_contributors_names))
                        metadata.contributors.add(*db_contributors)
                    except WorksMetadata.DoesNotExist:
                        if input_iswc or input_title in input_contributors_names:
                            instance = WorksMetadata.objects.create(
                                title=input_title,
                                iswc=input_iswc,
                            )
                            instance.contributors.set(db_contributors)
            self.stdout.write(self.style.SUCCESS(
                'Successfully matched and reconciled metadata'))


def _create_missing_contributors(names):
    for name in names:
        obj, created = Contributor.objects.get_or_create(
            name=name, defaults={'name': name})
