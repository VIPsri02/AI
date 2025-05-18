import pandas as pd
from db_connect import engine

def run_and_format(sql):
    try:
        df = pd.read_sql(sql, engine)
        if df.empty:
            return "No results found."
        return df.to_markdown(index=False)
    except Exception as e:
        return f"Error executing SQL: {e}"