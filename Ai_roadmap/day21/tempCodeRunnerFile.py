from langchain_groq import ChatGroq
import os
from dotenv import load_dotenv
import chromadb

client = chromadb.PersistentClient(path="chroma_storage")
collection = client.get_or_create_collection(name="Atomic_habits")

def ask_question(question):
    
    chunks = collection.query(
        query_texts=[question],
        n_results=3
    )
    prompt = "Use the following context to answer the question accurately. If the answer is not in the context, say 'I don't know'.\n\ncontext: "
    doc , metadata = chunks["documents"][0],chunks['metadatas'][0]
    for i in doc:
        prompt += i.replace("\t"," ")
    page_no = ""
    for i in metadata:
        page_no += str(i['page_no'])+","
    return f"{prompt}\nquestion: {question}",page_no

load_dotenv()
api_key = os.getenv("GROQ")

llm = ChatGroq(
    model = "llama-3.3-70b-versatile",
    api_key=api_key,
    temperature=0.2
)
prompt , page_no = ask_question("What is an habit?")
results = llm.invoke(prompt)
print(results.content,f"page no's: {page_no}",sep="\n")