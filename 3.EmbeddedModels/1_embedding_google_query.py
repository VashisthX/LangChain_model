from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embedded = GoogleGenerativeAIEmbeddings(model='models/gemini-embedding-001', dimensions=10)

result = embedded.embed_query("Delhi is the capital of India")

print(str(result))