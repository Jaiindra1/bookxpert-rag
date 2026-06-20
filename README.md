# BookXpert RAG Assignment

## Overview

This project implements a Retrieval-Augmented Generation (RAG) system using Python, ChromaDB, and Google Gemini.

The system ingests multiple PDF documents, converts them into searchable vector embeddings, stores them in ChromaDB, retrieves relevant chunks based on user questions, and generates grounded answers using Gemini.

## Architecture

```text
PDF Documents
      ↓
Text Extraction
      ↓
Chunking
      ↓
Vector Embeddings
      ↓
ChromaDB Storage

User Question
      ↓
Similarity Search
      ↓
Relevant Chunks
      ↓
Gemini
      ↓
Answer + Citations
```

## Tech Stack

* Python 3.11
* Google Gemini API
* ChromaDB
* PyPDF
* python-dotenv

## Documents Indexed

* Python Documentation
* AWS Well-Architected Framework
* NIST AI Risk Management Framework
* React Documentation
* .NET Microservices Architecture Guide
* Resume PDF

## Chunking Strategy

* Chunk Size: 1000 characters
* Overlap: 200 characters
* Page-level extraction followed by chunking

## Embedding and Retrieval

* Embedding Model: Gemini Embedding Model
* Vector Database: ChromaDB
* Retrieval Method: Top-K Semantic Search

## Features

* Multi-document PDF ingestion
* Metadata storage (source and page number)
* Semantic search
* Source citations
* Interactive CLI interface
* Hallucination reduction using grounded context

## Installation

```bash
pip install -r requirements.txt
```

Create a `.env` file:

```env
GEMINI_API_KEY=your_api_key_here
```

## Usage

### Index Documents

```bash
python src/ingest.py
```

### Query Documents

```bash
python src/query.py
```

## Example Queries

* What are microservices?
* What is trustworthy AI?
* What are the pillars of AWS Well-Architected Framework?
* What does the Python calendar module do?

## Limitations

* No OCR support for scanned PDFs
* Retrieval quality depends on chunking strategy
* Optimized for PDF-based document collections

```
```
