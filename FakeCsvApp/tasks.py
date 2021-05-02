from celery import shared_task
from .serializers import SchemaDetailSerializer
from .models import Schemas
from datetime import datetime
import csv


def dump_data_creater(column_type, col_from, col_to):
    return {
        'FullName': 'John Wick',
        'Job': 'Killer',
        'Email': 'John.Wick@gmail.com',
        'Text': 'Cool '*col_to,
        'Integer': (col_to - col_from)/2
    }.get(column_type, lambda: 'Unknown')()


def prepare_data(schema_id):
    schema = Schemas.objects.get(id=schema_id)
    schema_date_modified = schema.data()['DateModified']
    column_data = SchemaDetailSerializer(schema).data()['column']
    column_data.sort(key=lambda column: column['order'])

    column_name = [column['Name'] for column in column_data]
    column_type = [column['Type'] for column in column_data]
    column_from = [column['From'] for column in column_data]
    column_to = [column['To'] for column in column_data]

    prepared_data = [
        column_name,
        column_type,
        column_from,
        column_to,
        schema_date_modified
    ]

    return prepared_data


@shared_task(name='create_csv')
def create_csv(schema_id, row_num):
    column_name, column_type, column_from, column_to, schema_date_modified = prepare_data(schema_id)
    file_name = f'../media/{schema_id}_{datetime.today()}.csv'

    with open(file_name, 'w', newline='') as f:
        writer = csv.writer(f)
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
            writer.writerow(column_name)
