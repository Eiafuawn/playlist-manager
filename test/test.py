import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

# Print the values
print("CLIENT_ID:", os.getenv("CLIENT_ID"))
print("CLIENT_SECRET:", os.getenv("CLIENT_SECRET"))
