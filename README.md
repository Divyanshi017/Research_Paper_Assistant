# Research Paper Assistant

A simple RAG-based application that allows you to upload a research paper and ask questions about it.

Instead of manually searching through a long paper, you can ask a question and the system retrieves the relevant parts of the paper and uses an LLM to generate an answer.

## How It Works

The project follows a basic RAG pipeline:

```mermaid
flowchart LR
    A[Research Paper] --> B[Chunking]
    B --> C[Embeddings]
    C --> D[Vector Store]
    D --> E[Retriever]
    E --> F[LLM]
    F --> G[Answer]
```

The main steps are:

1. The research paper is loaded and split into smaller chunks.
2. Embeddings are created for the chunks.
3. The embeddings are stored in a vector store.
4. When a question is asked, relevant chunks are retrieved.
5. The retrieved context is passed to the LLM.
6. The LLM generates the final answer.

## Project Structure

```text
Research_Paper_Assistant/
│
├── papers/
│   └── Research papers
│
├── chunkers.py
├── embeddings.py
├── llm.py
├── main.py
├── retriever.py
├── vector_store.py
├── requirements.txt
└── .gitignore
```

### Files

- `main.py` - Runs the main application.
- `chunkers.py` - Handles splitting the research paper into chunks.
- `embeddings.py` - Creates embeddings for the document chunks.
- `vector_store.py` - Stores and manages the generated vectors.
- `retriever.py` - Retrieves relevant chunks based on the user's question.
- `llm.py` - Handles the LLM and generates the final response.
- `papers/` - Contains the research papers used by the application.
- `requirements.txt` - Contains the required Python libraries.
- `.gitignore` - Contains files and folders that should not be pushed to GitHub.

## Tech Stack

- Python
- LangChain
- FAISS
- Embeddings
- LLM

## Setup

### 1. Clone the repository

```bash
git clone <your-repository-url>
cd Research_Paper_Assistant
```

### 2. Install the dependencies

```bash
pip install -r requirements.txt
```

### 3. Add your API key

Create a `.env` file and add the API key required by your LLM provider.

```text
API_KEY=your_api_key_here
```

Make sure the `.env` file is not uploaded to GitHub.

## Run the Project

Run the main file:

```bash
python main.py
```

Upload or use a research paper from the `papers` folder and ask questions about its content.

## Example

You can ask questions such as:

> What is the main idea of this paper?

> What problem does the paper solve?

> What methodology was used?

> What are the main findings?

The system retrieves the relevant information from the paper and uses it to generate an answer.

## Limitations

- The quality of the answer depends on the retrieved chunks.
- Poor chunking can affect the results.
- Complex PDFs may not be processed perfectly.
- The LLM can still generate incorrect information.

## Future Improvements

- Add support for multiple papers
- Add source and page citations
- Improve retrieval accuracy
- Add reranking
- Add conversation history
- Add RAG evaluation

