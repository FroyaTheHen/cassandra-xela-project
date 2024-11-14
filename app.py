from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider


auth_provider = PlainTextAuthProvider(username="cassandra", password="cassandra")
cluster = Cluster(auth_provider=auth_provider, protocol_version=3, contact_points=['0.0.0.0'], port=9042)
session = cluster.connect()
q = """CREATE KEYSPACE IF NOT EXISTS xela_keyspace
WITH replication = {
    'class': 'SimpleStrategy', 
    'replication_factor': 1
};"""
session.execute(q)
cluster.shutdown()
