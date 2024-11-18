#  myapp/models.py
import uuid
from cassandra.cqlengine import columns
from django_cassandra_engine.models import DjangoCassandraModel


class Volcano(DjangoCassandraModel):
    volcano_id = columns.UUID(primary_key=True, default=uuid.uuid4)
    height = columns.Integer(index=True)
    created_at = columns.DateTime()
    name = columns.Text(required=False)
    description = columns.Text(required=False)
    country = columns.Text(required=False)

