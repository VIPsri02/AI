import ollama

def generate_sql(prompt, schema_context, chat_history):
    system_prompt = (
        "You are an expert SQL assistant. "
        "The database is SQLite. "
        "Given the following database schema:\n"
        f"{schema_context}\n"
        "And the conversation so far:\n"
        f"{chat_history}\n"
        "Generate an exact SQL query for the user's request. Only output the SQL query."
    )
    response = ollama.chat(
        model='llama3',
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": prompt}
        ]
    )
    return response['message']['content'].strip()