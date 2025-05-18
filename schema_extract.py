from sqlalchemy import inspect
from db_connect import engine

inspector = inspect(engine)
schema_info = {}
for table in inspector.get_table_names():
    columns = inspector.get_columns(table)
    schema_info[table] = [col['name'] for col in columns]