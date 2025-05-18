def retrieve_schema(prompt, schema_info):
    relevant = []
    for table, cols in schema_info.items():
        if table.lower() in prompt.lower() or any(col.lower() in prompt.lower() for col in cols):
            relevant.append(f"Table: {table}, Columns: {', '.join(cols)}")
    return "\n".join(relevant) if relevant else str(schema_info)