# Files Chatboy 🦾

Welcome to **Files Chatboy** – an intelligent question-answering system for your PDF documents. This tool allows you to upload a PDF file, process its content, and interact with it by asking questions related to the file. It's built using Streamlit, Sentence Transformers, Langchain, and HuggingFace.

---

## Features

- Upload a PDF file and extract its content.
- The content is split into chunks and processed using embeddings.
- You can ask questions related to the file, and the model will provide relevant answers.
- The system uses a combination of pre-trained models (Sentence-BERT for embeddings and HuggingFace's Roberta-based Q&A model) to generate accurate answers.
- Built with a user-friendly interface powered by Streamlit.

---

## Requirements

To get started, you will need to install the following dependencies:

- `streamlit` – For creating the user interface.
- `sentence-transformers` – For generating embeddings for document chunks.
- `PyPDF2` – For reading PDF files.
- `langchain` – For handling text splitting and vector stores.
- `langchain_community` – For HuggingFace embeddings integration.
- `transformers` – For question answering.

To install these dependencies, you can use the following command:

```bash
pip install streamlit sentence-transformers PyPDF2 langchain langchain_community transformers
```

## How It Works

1. Upload PDF: Users can upload a PDF file using the Streamlit file uploader.

2. Text Extraction: The content of the PDF is extracted page by page.

3. Text Splitting: The extracted text is split into smaller chunks using the RecursiveCharacterTextSplitter from Langchain.

4. Vector Store Creation: The text chunks are converted into embeddings, stored in a vector store using FAISS.

5. Question Answering: Users can ask questions, and the system will search for the most relevant chunks using similarity search and provide answers using a question-answering pipeline powered by HuggingFace.

---

## Usage

1. Clone the repository or download the source code.

2. Install the dependencies (mentioned above).

3. Run the Streamlit application:

``` bash
streamlit run app.py

```

4. Open the application in your browser (usually at http://localhost:8501).

5. Upload a PDF file.

6. Ask any question related to the document, and get your answer instantly.

---

## Code Overview
- UI (Streamlit): The application uses Streamlit for the front-end interface, where users can upload their PDFs and ask questions.

- PDF Text Extraction (PyPDF2): The content of the uploaded PDF is extracted page by page.

- Text Processing (Langchain): The text is split into chunks for efficient similarity searching.

- Embeddings (Sentence-Transformers & HuggingFace): Embeddings are generated for the text chunks, which are stored in a FAISS vector store.

- Q&A Model (HuggingFace): The question-answering pipeline uses a pre-trained RoBERTa model to provide answers based on the relevant document context.

## Customization
- Chunk Size: You can modify the chunk_size and chunk_overlap parameters in the RecursiveCharacterTextSplitter to adjust how the text is split.

- Embeddings Model: The embeddings are generated using the sentence-transformers/all-MiniLM-L6-v2 model. You can change this to any other suitable model.

- Q&A Model: The default model for answering questions is deepset/roberta-base-squad2. You can replace it with any other model of your choice from HuggingFace.

---

## Example
### Once the application is running:

1. Upload a PDF document, e.g., a research paper.

2. Ask questions such as:

    - "What is the main objective of the study?"

    - "Can you explain the methodology?"

    - "What are the results of the experiment?"

The application will process the document and generate answers based on its content.

## Contributing
If you'd like to contribute to this project, feel free to fork the repository, make changes, and create a pull request. Contributions are always welcome!

## Acknowledgments
- Streamlit for providing a simple and powerful interface for building applications.

- Sentence-Transformers for pre-trained models used for embedding generation.

- PyPDF2 for extracting text from PDF files.

- Langchain for its utilities for text processing and vector stores.

- HuggingFace for providing state-of-the-art models for question answering.

