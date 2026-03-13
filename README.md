# Local RAG Assistant 
 
A local Retrieval-Augmented Generation (RAG) assistant built with Python and Ollama that allows querying PDFs using a local language model. 
 
## Features 
- Load and process PDF documents 
- Split documents into manageable chunks 
- Generate embeddings for semantic search 
- Store embeddings in a vector database 
- Query documents using a local LLM (Mistral) 
 
## Tech Stack 
- Python 
- Ollama 
- Mistral 
- ChromaDB 
- PyMuPDF 
 
## Architecture 
PDF -> Chunking -> Embeddings -> Vector Database -> Retrieval -> Mistral -> Answer 
 
## Setup 
Install dependencies: 
pip install -r requirements.txt 
 
Run the application: 
python app.py 
 
## Project Goal 
This project demonstrates how to build a local Retrieval-Augmented Generation pipeline using Python and a locally hosted LLM. 
