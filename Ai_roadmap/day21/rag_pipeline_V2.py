from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader
import chromadb
from langchain_groq import ChatGroq
import os 
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("GROQ")
llm = ChatGroq(
    model= "llama-3.3-70b-versatile",
    api_key=api_key,
    temperature=0.3)
client = chromadb.PersistentClient(path="chroma_storage")

def process_pdf(pdf_path,name):
    
    existing = [c.name for c in client.list_collections()]
    if name in existing:
        collection = client.get_or_create_collection(name=name)
        return collection.count()
    # Load, chunk, embed, store in ChromaDB
    splitter = RecursiveCharacterTextSplitter(chunk_size=500,chunk_overlap=100)
    loader = PyPDFLoader(pdf_path)

    pages = loader.load()
    chunks = splitter.split_documents(pages)
    
    collection = client.get_or_create_collection(name=name)
    collection.add(
        documents=[chunk.page_content for chunk in chunks],
        ids = [f"chunk_{i+1}" for i in range(len(chunks))],
        metadatas=[{"Page_no":chunk.metadata['page'],'source':chunk.metadata['source']} for chunk in chunks]
    )
    return len(chunks)

    # Returns: number of chunks stored

def ask_question(question,collection_name):
    collection = client.get_or_create_collection(collection_name)
    results = collection.query(
        query_texts= [question],
        n_results= 3
    )
    prompt = "Use the following context to answer the question accurately. If the answer is not in the context, say 'I don't know'.\n\nContext: "
    prompt += "".join(results['documents'][0])
    prompt += f"\nquestion: {question}"
    metadata = results["metadatas"][0]
    page_no = [m['Page_no'] for m in metadata]

    output = llm.invoke(prompt)
    return output , page_no

print(process_pdf(r"c:\\Users\\Public\\Downloads\\Atomic-Habits-.pdf","Atomic_habits"))
answer, pages = ask_question("What is a habit?", "Atomic_habits")
print(answer.content)
print("Pages:", pages)