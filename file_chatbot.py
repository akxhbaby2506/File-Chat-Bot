import streamlit as st  # UI Interface
from sentence_transformers import SentenceTransformer  # Inbuilt Pretrained modal for generating embeddings with Unlimited Access
from PyPDF2 import PdfReader  # For reading PDF files
from langchain.text_splitter import RecursiveCharacterTextSplitter # For splitting the text into chunks
from langchain.vectorstores import FAISS # For creating a vector store
from langchain_community.embeddings import HuggingFaceEmbeddings # For generating embeddings
from transformers import pipeline # For generating answer


modal = SentenceTransformer('all-MiniLM-L6-v2')  # Used for generating embeddings
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200) # For splitting the text into chunks
embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2") # For generating embeddings
qa_pipeline = pipeline("question-answering", model="deepset/roberta-base-squad2") # For generating answer

st.set_page_config(page_title="Files Chatboy", page_icon=":shark:")
st.title("🦾File's ka Chatboy")

st.markdown("Upload your PDF and you can ask questions related to the file content")

# Sidebar for file upload

with st.sidebar:

    st.title("Upload your documents here")
    file = st.file_uploader("Upload your PDF file here", type="pdf" , help="Please upload a PDF file to get started")

if file:
    with st.spinner("Processing your file..."):
        text = ""
        pdf_reader = PdfReader(file)
        for page in pdf_reader.pages:
            text += page.extract_text()

        # st.write(text)

    with st.spinner('Processing your text...'):
        #Splitting Text into chunks
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000, 
            chunk_overlap=150,
            length_function=len,
            separators=["\n\n", "\n", " ", ""]
            )
        
        chunks = text_splitter.split_text(text)
        # st.write(chunks)

    with st.spinner('Creating vector store...'):
        #Creating a Vector Store using faiss
        vector_store = FAISS.from_texts(chunks, embeddings)
        st.write("Vector store created successfully!")
        # st.write(vector_store)

    # Help User to ask Question   
    user_ques = st.text_input("Ask your Question here ")

    if user_ques:
        # Get relevant chunks
        match = vector_store.similarity_search(user_ques)
        
        # Combine relevant chunks into context
        context = " ".join([doc.page_content for doc in match])
        
        # Generate answer using question-answering pipeline
        answer = qa_pipeline(question=user_ques, context=context)
        st.write("Answer:", answer['answer'])
                   

st.markdown("---")
st.markdown("Made with ❤️ by Akash")
