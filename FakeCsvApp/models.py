from django.db import models
from django.conf import settings


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

    def __str__(self):
        return str(self.Name)

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
    From = models.IntegerField(default=None)
    To = models.IntegerField(default=None)
    Order = models.IntegerField(unique=True)
    Schemas = models.ForeignKey(
        Schemas,
        verbose_name='Schemas',
        related_name='Columns',
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return str(self.Name)

    class Meta:
        verbose_name = 'Column'
        verbose_name_plural = 'Columns'
