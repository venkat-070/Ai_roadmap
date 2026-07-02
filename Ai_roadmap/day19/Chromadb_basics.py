import chromadb as ch

client = ch.PersistentClient(path="./chroma_storage")
collection = client.get_or_create_collection(name="My_collection")

collection.add(
    documents=[
        "Refund requests must be made within 30 days of purchase.",
        "Shipping takes 5-7 business days for standard delivery.",
        "Contact our support team at support@example.com for help.",
        "Products can be returned in original packaging only.",
        "Express shipping is available for an additional fee."
    ],
    ids=["doc1", "doc2", "doc3", "doc4", "doc5"]
)

results = collection.query(
    query_texts=["How do I send a product back?"],
    n_results=2
)
print(results['documents'])
print(results['distances'])