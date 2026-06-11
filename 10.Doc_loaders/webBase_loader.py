from langchain_community.document_loaders import WebBaseLoader
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(model='gemini-2.5-flash')

parser = StrOutputParser()

prompt = PromptTemplate(
    template='Answer the following question \n {question} from the text - \n {text}',
    input_variables=['question', 'text']
)

url = 'https://www.cricbuzz.com/live-cricket-scores/156091/engw-vs-indw-11th-match-icc-womens-t20-world-cup-warm-up-matches-2026'

loader = WebBaseLoader(url)

docs = loader.load()

chain = prompt | model | parser

result = chain.invoke({'question':'who won the match india or england', 'text':docs[0].page_content})

print(result)