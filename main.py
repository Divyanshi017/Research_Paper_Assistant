import os
import warnings

# Suppress Hugging Face download progress bars and info logs
os.environ["HF_HUB_DISABLE_SYMLINKS_WARNING"] = "1"
os.environ["TRANSFORMERS_VERBOSITY"] = "error"
os.environ["HF_HUB_DISABLE_PROGRESS_BARS"] = "1"

# Suppress Python warnings
warnings.filterwarnings("ignore")
from pypdf import PdfReader
from sentence_transformers import SentenceTransformer
import numpy as np
import faiss
from dotenv import load_dotenv
import os
from groq import Groq

from chunkers import create_chunks
from embeddings import create_embeddings
from vector_store import create_index
from retriever import retrieve_chunks
from llm import generate_answer

pdf_path = "papers/RAG.pdf"
reader= PdfReader(pdf_path)
text=""
for pages in reader.pages:
    page_text= pages.extract_text()
    if page_text:
        text += page_text+ "\n"

chunks= create_chunks(text)
embeddings= create_embeddings(chunks)
index= create_index(embeddings)

print("Number of chunks: ", len(chunks))
print("Embeddings shape: ", embeddings.shape)
print("FAISS index size: ", index.ntotal)

model= SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")
question= input("\nAsk a question about the paper: ")
retrieved_chunks, distances= retrieve_chunks(question, model, index, chunks)

print("\nRetrieved chunks: ")

for i, chunk in enumerate(retrieved_chunks):
    print("\n  Chunks", i+1, "   ")
    print(chunk)

answer= generate_answer(question, retrieved_chunks)
print("\nAnswers: ")
print(answer)