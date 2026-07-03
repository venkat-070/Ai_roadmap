from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
splitter = RecursiveCharacterTextSplitter(chunk_size = 500,chunk_overlap=100 )
loader = PyPDFLoader(r"C:\\Users\\Public\\Downloads\\Atomic-Habits-.pdf")

pages = loader.load()

chunks = splitter.split_documents(pages)

print("Number of pages: ",len(pages))
print("First page content review")
print(len(pages[0].page_content))
print(len(pages[1].page_content))
print(len(pages[5].page_content))
print(len(pages[10].page_content))
print("Page metadata: ")
print(pages[0].metadata)


print("Total chunks:",len(chunks))

for chunk in chunks:
    if chunk.page_content.strip():
        print(chunk.page_content)
        print("\nMetadata:", chunk.metadata)
        break
