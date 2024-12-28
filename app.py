import logging
import os

from dotenv import load_dotenv
from flask import Flask, render_template, request
from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate
from langchain_community.llms import CTransformers
from langchain_community.vectorstores import Pinecone
from pyngrok import ngrok

from src.helper import download_hugging_face_embeddings
from src.prompt import *

logging.basicConfig(level=logging.INFO, format="[%(asctime)s]: %(message)s:")

app = Flask(__name__)

load_dotenv()

PINECONE_API_KEY = os.environ.get("PINECONE_API_KEY")
PINECONE_INDEX_NAME = os.environ.get("PINECONE_INDEX_NAME")

embeddings = download_hugging_face_embeddings()

# Loading the index
docsearch = Pinecone.from_existing_index(PINECONE_INDEX_NAME, embeddings)

PROMPT = PromptTemplate(
    template=prompt_template, input_variables=["context", "question"]
)

chain_type_kwargs = {"prompt": PROMPT}

llm = CTransformers(
    model="model/llama-2-7b-chat.ggmlv3.q4_0.bin",
    model_type="llama",
    config={"max_new_tokens": 512, "temperature": 0.8},
)

ret_qa = RetrievalQA.from_chain_type(
    llm=llm,
    chain_type="stuff",
    retriever=docsearch.as_retriever(search_kwargs={"k": 2}),
    return_source_documents=True,
    chain_type_kwargs=chain_type_kwargs,
)


@app.route("/")
def index():
    return render_template("chat.html")


@app.route("/get", methods=["GET", "POST"])
def chat():
    input_msg = request.form["msg"]
    print(input_msg)
    result = ret_qa({"query": input_msg})
    print("Response : ", result["result"])
    return str(result["result"])


if __name__ == "__main__":
    ngrok_tunnel = ngrok.connect("https://localhost:8080")
    app.run(host="0.0.0.0", port=8080)
