import os

from dotenv import load_dotenv
from groq import Groq


load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))


def generate_answer(question, retrieved_chunks):

    context = "\n\n".join(retrieved_chunks)

    prompt = f"""You are a research paper assistant. Answer the user's question using only the information provided in the context below.

Context:
{context}

Question:
{question}

If the answer cannot be found in the context,
say that the information was not found in the paper.

Give a clear and simple answer.
"""

    response = client.chat.completions.create(model="llama-3.1-8b-instant",messages=[{"role": "user","content": prompt}],temperature=0)
    return response.choices[0].message.content