from langchain_community.retrievers import WikipediaRetriever

retriever = WikipediaRetriever(
    # kitne result chaiye 
    top_k_results=2,
    #which language
    lang='en'
)

query = "India"

docs = retriever.invoke(query)

print(docs)

