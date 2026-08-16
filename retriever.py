import numpy as np

def retrieve_chunks(question, model, index, chunks, top_k=3):
    question_embeddings= model.encode([question])
    question_embeddings= np.array(question_embeddings).astype("float32")
    distances,indices= index.search(question_embeddings, top_k)
    retrieved_chunks=[]

    for i in indices[0]:
        retrieved_chunks.append(chunks[i])

    return retrieved_chunks, distances