from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from typing import TypedDict, Annotated, Optional, Literal

load_dotenv()

model = ChatGoogleGenerativeAI(model='gemini-2.5-flash')

#schema (defined format for review)
class review(TypedDict):
    # annotated means normal type + some extra note/instruction attached to it.
    key_themes: Annotated[list[str], "Write down all the key themes discussed in the review in a list"]
    summary: Annotated[str, "A brief summary of the review"]
    sentiment: Annotated[Literal["pos", "neg"], "Return sentiment of the review either negative, positive or neutral"]
    pros: Annotated[Optional[list[str]], "Write down all the pros inside a list"]
    cons: Annotated[Optional[list[str]], "Write down all the cons inside a list"]
    name: Annotated[Optional[str], "Write the name of the reviewer"]

structured_model = model.with_structured_output(review)

result = structured_model.invoke("""The hardware is great, but the software feels bloated. There are too many pre-installed apps that i cant remove. Also, the ui looks outdated compared to other brands. Hoping for a software update to fix this. Review by Harshit Raj""")

print(result['name'])