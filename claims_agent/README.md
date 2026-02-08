Autonomous Insurance Claims Processing Agent
Overview

This project implements a lightweight AI-powered claims processing agent that extracts information from FNOL (First Notice of Loss) insurance documents and automatically routes the claim to the appropriate workflow.

The goal is to simulate a real-world insurance intake system where unstructured documents are converted into structured claim data and processed using business rules.

Features

Extracts structured data from insurance FNOL PDF forms

Detects missing mandatory claim information

Applies business routing rules

Provides explainable reasoning for decisions

Fully local AI inference (privacy-safe, no external API dependency)

Architecture
PDF Document
      ↓
Text Extraction (pdfplumber)
      ↓
LLM Semantic Extraction (Local Model)
      ↓
Validation Layer (Required Fields Check)
      ↓
Decision Engine (Routing Rules)
      ↓
Explainable JSON Output

Routing Rules
Condition	Route
Missing mandatory fields	Manual Review
Estimated damage < 25,000	Fast Track
Fraud keywords detected	Investigation
Injury claims	Specialist Queue
Otherwise	Standard Processing
Installation
1. Install dependencies
pip install -r requirements.txt

2. Install Ollama

Download from https://ollama.com

Then install model:

ollama run gemma3:4b

3. Run application
python main.py

Output Format
{
  "extractedFields": {},
  "missingFields": [],
  "recommendedRoute": "",
  "reasoning": ""
}

Design Decisions

Used LLM semantic extraction instead of regex parsing to handle variable document formats

Separated validation and routing layers for auditability

Local inference ensures data privacy and avoids API dependency

Future Improvements

Support multiple document formats

Add confidence scoring

Integrate REST API endpoint

Batch claim processing