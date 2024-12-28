import logging
import os

from dotenv import load_dotenv
from langchain_community.vectorstores import Pinecone

from src.helper import load_pdf, text_split, download_hugging_face_embeddings

logging.basicConfig(level=logging.INFO, format="[%(asctime)s]: %(message)s:")

load_dotenv()

PINECONE_API_KEY = os.environ.get("PINECONE_API_KEY")
PINECONE_API_ENV = os.environ.get("PINECONE_API_ENV")
PINECONE_HOST = os.environ.get("PINECONE_HOST")
PINECONE_INDEX_NAME = os.environ.get("PINECONE_INDEX_NAME")

extracted_data = load_pdf("data/")
logging.info("Data loaded from Pdf files")

text_chunks = text_split(extracted_data)
logging.info("Chunks created from the corpus")

embeddings = download_hugging_face_embeddings(
    model_id="model/models--sentence-transformers--all-MiniLM-L6-v2/snapshots/fa97f6e7cb1a59073dff9e6b13e2715cf7475ac9"
)
logging.info("Embeddings Model loaded")

# # Creating Embeddings for Each of The Text Chunks & storing
docsearch = Pinecone.from_texts(
    [t.page_content for t in text_chunks], embeddings, index_name=PINECONE_INDEX_NAME
)

logging.info(
    "Embeddings created for Each of The Text Chunks & Stored into Pinecone Index"
)
