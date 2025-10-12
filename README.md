@"
# NLPApp

A simple Python Tkinter desktop application that uses the NLPCloud API.

## Features
- NER (Entity Extraction)
- Sentiment Analysis
- Headline Generation
- Grammar & Spelling Correction
- Language Detection

## Requirements
- Python 3.8+
- pip install -r requirements.txt
- Set environment variable `NLPCLOUD_API_KEY`

## Run
Windows PowerShell:
```powershell
setx NLPCLOUD_API_KEY \"your_api_key_here\"
python NLPApp.py

macOS / Linux:

export NLPCLOUD_API_KEY=\"your_api_key_here\"
python3 NLPApp.py