from django.db import models


class Contributor(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return '%s' % (self.name)


class WorksMetadata(models.Model):
    iswc = models.CharField(max_length=200, unique=True)
    title = models.CharField(max_length=200)
    contributors = models.ManyToManyField(Contributor, blank=True)

    class Meta:
        verbose_name_plural = 'Works Metadata'

    def __str__(self):
        return '%s  %s' % (self.iswc, self.title)
