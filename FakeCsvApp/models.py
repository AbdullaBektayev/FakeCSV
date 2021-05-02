from django.db import models
from django.conf import settings
from django.urls import reverse
from datetime import datetime


class Schemas(models.Model):
    Comma = 'Comma'
    Space = 'Space'

    Apostrophe = 'Apostrophe'
    QuotationMarks = 'Quotation Marks'

    ColumnSeparatorChoices = (
        (Comma, 'Comma'),
        (Space, 'Space'),
    )

    StringCharChoices = (
        (Apostrophe, 'Apostrophe'),
        (QuotationMarks, 'Quotation Marks'),
    )

    User = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )

    Name = models.CharField(max_length=50)

    ColumnSeparator = models.CharField(
        choices=ColumnSeparatorChoices,
        default=Comma,
        max_length=50,
    )

    StringChar = models.CharField(
        choices=StringCharChoices,
        default=QuotationMarks,
        max_length=50,
    )

    DateModified = models.DateTimeField(
        default=datetime.now()
    )

    def __str__(self):
        return str(self.Name)

    def get_url(self):
        return reverse('schema_detail', kwargs={'pk': self.id})

    class Meta:
        verbose_name = 'Schema'
        verbose_name_plural = 'Schemas'


class Columns(models.Model):
    FullName = 'FullName'
    Job = 'Job'
    Email = 'Email'
    Text = 'Text'
    Integer = 'Integer'

    TypeChoices = (
        (FullName, 'FullName'),
        (Job, 'Job'),
        (Email, 'Email'),
        (Text, 'Text'),
        (Integer, 'Integer'),
    )

    Name = models.CharField(max_length=30)
    Type = models.CharField(
        choices=TypeChoices,
        default=FullName,
        max_length=30,
    )
    From = models.IntegerField(default=None, blank=True)
    To = models.IntegerField(default=None, blank=True)
    Order = models.IntegerField(default=0)
    Schema = models.ForeignKey(
        Schemas,
        verbose_name='schema',
        related_name='column',
        on_delete=models.CASCADE,
        default=0,
    )

    def __str__(self):
        return str(self.Name)

    class Meta:
        verbose_name = 'Column'
        verbose_name_plural = 'Columns'
