from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
import chromadb

splitter = RecursiveCharacterTextSplitter(chunk_size=500,chunk_overlap=100)
loader = PyPDFLoader(r"C:\\Users\\Public\\Downloads\\Atomic-Habits-.pdf")

pages = loader.load()
chunks = splitter.split_documents(pages)

client = chromadb.PersistentClient(path="./chroma_storage")
collection = client.get_or_create_collection(name="Atomic_habits")

collection.add(
    documents=[chunk.page_content for chunk in chunks],
    ids=[f"chunk_{i}" for i in range(len(chunks))],
    metadatas=[{'page_no':chunk.metadata['page'],'source':chunk.metadata['source']} for chunk in chunks]
)
results = collection.query(
    query_texts=["How do habits form in the brain?"],
    n_results=2
)

for doc,metadata,dist in zip(results['documents'][0],results['metadatas'][0],results['distances'][0]):
    print(f"page no:{metadata['page_no']}")
    print(f"Distances: {dist:.4f}")
    print(f"documents:{doc[:200].replace('\t'," ")}")


