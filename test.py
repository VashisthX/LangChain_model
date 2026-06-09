from dotenv import load_dotenv
from huggingface_hub import whoami
import os

load_dotenv()

token = os.getenv("HUGGINGFACEHUB_API_TOKEN")

print("Token loaded:", token is not None)
print("First chars:", token[:10] if token else None)

print(whoami(token=token))