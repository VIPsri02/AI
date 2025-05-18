from schema_extract import schema_info
from rag_pipeline import retrieve_schema
from llm_query import generate_sql
from run_sql import run_and_format
from session_memory import SessionMemory

def main():
    memory = SessionMemory()
    print("Welcome to the AI SQL Agent! Type 'exit' to quit.\n")
    while True:
        user_prompt = input("Ask your question: ")
        if user_prompt.strip().lower() == 'exit':
            break
        schema_context = retrieve_schema(user_prompt, schema_info)
        chat_history = memory.get()
        sql_query = generate_sql(user_prompt, schema_context, chat_history)
        print("\nGenerated SQL:\n", sql_query)
        result = run_and_format(sql_query)
        print("\nResult:\n", result)
        memory.add(user_prompt, result)
        print("\n---\n")

if __name__ == "__main__":
    main()