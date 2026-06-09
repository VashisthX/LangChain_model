from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate

load_dotenv()

model = ChatGoogleGenerativeAI(model='gemini-2.0-flash')


template1 = PromptTemplate(
    template='Give 3 fact about {topic} \n',
    input_variables=['topic']
)

template2 = PromptTemplate(
    template='write a 5 line summary on the following text. /n  {text}',
    input_variables=['text']
)

prompt1 = template1.invoke({'topic':'black hole'})
result1 = model.invoke(prompt1)

prompt2 = template2.invoke({'text':result1.content})
result2 = model.invoke(prompt2)

print(result2.content)
