def create_chunks (text, chunk_size=1000):
    chunks=[]
    for i in range(0, len(text), chunk_size):
        chunk= text[i:i+chunk_size]
        if chunk.strip():
            chunks.append(chunk)

    return chunks