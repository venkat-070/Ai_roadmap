import chromadb as ch

client = ch.PersistentClient(path="./chroma_storage")
collection = client.get_or_create_collection(name="My_collection")

print(collection.count())

