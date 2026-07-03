import chromadb

def chunking(text, chunk_size, overlap):
    chunks = []
    for i in range(0,chunk_size,overlap):
        chunk = text[i:i+chunk_size-overlap]
        if chunk.strip():
            chunks.append(chunk)
    return chunks
text = """
Section 1: Refund Policy
Customers can request a refund within 30 days of purchase. 
Refunds are processed within 5-7 business days. 
The refund will be credited to the original payment method.
Items must be unused and in original condition for refund eligibility.

Section 2: Shipping Policy
Standard shipping takes 5-7 business days.
Express shipping is available and takes 1-2 business days.
Shipping is free for orders above 500 rupees.
International shipping is currently not available.

Section 3: Contact Information
Our support team is available Monday to Friday, 9am to 6pm.
You can reach us at support@example.com.
For urgent queries, call us at 1800-123-456.
Our office is located in Bangalore, Karnataka.
"""
small_chunks = chunking(text,chunk_size=100,overlap=20)

print("Number of chunks: ",len(small_chunks))
print("Chunks:-")
for i,chunk in enumerate(small_chunks):
    print(f"chunk-{i+1}:{chunk}")

client = chromadb.PersistentClient(path="./chroma_storage")

small_collection = client.get_or_create_collection(name="small_chunks")

small_collection.add(
    documents=small_chunks,
    ids = [f"chunks {i}" for i in range(len(small_chunks))],
    
)

results = small_collection.query(
    query_texts=["What is the refund processing time?"],
    n_results= 2
)

print("-------- Small chunks ----------")
for doc,dist in zip(results['documents'][0],results['distances'][0]):
    print(f"Document:{doc}\ndistance:{dist}\n\n")

client1 = chromadb.PersistentClient(path="./chroma_storage")
large_collection = client1.get_or_create_collection(name="Large_collection")

large_chunks = chunking(text,chunk_size=300,overlap=50)
print("number of chunks: ",len(large_chunks))

for i in large_chunks:
    print(i)

large_collection.add(
    documents=large_chunks,
    ids=[f"chunk{i}" for i in range(len(large_chunks))]
)

results1 = large_collection.query(
    query_texts=["What is the refund processing time?"],
    n_results=2
)

print("-------- Large chunks ----------")
for docs,dis in zip(results1['documents'][0],results1['distances'][0]):
    print(f"Document:{docs}\ndistance:{dis}\n\n")