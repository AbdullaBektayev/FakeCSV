from celery import shared_task
from .serializers import SchemaDetailSerializer
from .models import Schemas
from django.utils.timezone import now
import csv


def get_data(schema_id):
    schema = Schemas.objects.get(id=schema_id)
    schema.DateModified = now()
    schema.save()
    schema = SchemaDetailSerializer(schema)
    return schema.data


def get_choices_and_date(schema):
    choice_dict = {
        'Comma (,)': ',',
        'Semicolon (;)': ';',
        'Double-quote (")': '"',
        "Single-quote (')": "'",
    }

    schema_date_modified = schema['DateModified']
    delimiter = choice_dict.get(schema['Delimiter'], ',')
    quotechar = choice_dict.get(schema['QuoteChar'], '"')

    return delimiter, quotechar, schema_date_modified


def dump_data_creater(column_type, col_from, col_to):
    return {
        'FullName': 'John Wick',
        'Job': 'Killer',
        'Email': 'John.Wick@gmail.com',
        'Text': 'Cool '*col_to,
        'Integer': (col_to - col_from)/2
    }.get(column_type, 'Unknown')


def prepare_column_data(schema):
    column_data = schema['column']
    column_data.sort(key=lambda column: column['Order'])
    column_name = [column['Name'] for column in column_data]
    column_type = [column['Type'] for column in column_data]
    column_from = [column['From'] for column in column_data]
    column_to = [column['To'] for column in column_data]

    prepared_data = [
        column_name,
        column_type,
        column_from,
        column_to,
    ]

    return prepared_data


@shared_task(name='create_csv')
def create_csv_task(schema_id, row_num):
    schema = get_data(schema_id)
    column_name, column_type, column_from, column_to = prepare_column_data(
        schema
    )
    delimiter, quotechar, schema_date_modified = get_choices_and_date(schema)

    file_name = f'{schema_id}_{schema_date_modified}.csv'

    with open(f'media/{file_name}', 'w') as f:
        writer = csv.writer(
            f,
            delimiter=delimiter,
            quotechar=quotechar,
            quoting=csv.QUOTE_NONNUMERIC
        )
        writer.writerow(column_name)
        for row in range(row_num):
            writer_row = []
            for idx, col_type in enumerate(column_type):
                writer_row.append(
                    dump_data_creater(
                        column_type=col_type,
                        col_from=column_from[idx],
                        col_to=column_to[idx]
                    )
                )
            writer.writerow(writer_row)

    return file_name, schema_date_modified
