# BookXpert RAG Assignment

## Overview

This project implements a Retrieval-Augmented Generation (RAG) system using Python, ChromaDB, and Google Gemini. The system ingests multiple PDF documents, generates embeddings, stores them in a vector database, and answers user questions using only retrieved document context.

## Architecture

PDF Documents → Text Extraction → Chunking → Embeddings → ChromaDB

User Query → Query Embedding → Similarity Search → Context Retrieval → Gemini → Answer + Citations

## Tech Stack

* Python 3.11
* ChromaDB
* Google Gemini API
* PyPDF2
* python-dotenv

## Chunking Strategy

* Chunk Size: 1000 characters
* Overlap: 200 characters
* Recursive text splitting approach

## Embedding Model

* Gemini Embedding Model
* Vector Dimension: 3072

## Vector Database

* ChromaDB
* Persistent local storage

## Features

* Multi-document PDF ingestion
* Semantic search
* Source citations
* Interactive CLI querying
* Hallucination reduction through context grounding

## Installation

```bash
pip install -r requirements.txt
```

Create a `.env` file:

```env
GOOGLE_API_KEY=your_api_key_here
```

Run ingestion:

```bash
python src/ingest.py
```

Run query interface:

```bash
python src/query.py
```

## Example Queries

* What are microservices?
* What is trustworthy AI?
* What are the AWS Well-Architected pillars?

## Limitations

* PDF text extraction quality depends on document structure.
* No OCR support for scanned PDFs.
* Retrieval quality depends on chunking configuration.
