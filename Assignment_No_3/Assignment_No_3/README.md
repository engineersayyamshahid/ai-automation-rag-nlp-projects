Multi-Input AI Analysis Pipeline



Assignment Information

Field               Details

Assignment      Assignment 3 --- AI Pipeline
Author          Sayyam Shahid
Program         BSCS
Semester        5th Semester
Internship      AI Automation Institute
University      FUUAST, Islamabad
AI Model        Gemini API
Main Language   Python

Author LinkedIn: Sayyam
Shahid

1. Project Overview

The Multi-Input AI Analysis Pipeline is a Python-based AI automation
project that accepts different types of input, processes the information
according to its format, sends the prepared information to a Gemini AI
model, and generates a structured analysis.

The pipeline is designed to reduce repetitive manual work involved in
reading documents, examining data, answering questions, and preparing
reports.

2. Supported Inputs

The pipeline supports:

Text files --- .txt

CSV files --- .csv

PDF files --- .pdf

Images --- .jpg, .jpeg, .png, .webp

JSON files --- .json

Markdown files --- .md

User questions

3. Pipeline Workflow

Input
  │
  ├── Text
  ├── CSV
  ├── PDF
  ├── Image
  ├── JSON
  ├── Markdown
  └── User Question
          │
          ▼
   Python Input Detection
          │
          ▼
   Content Extraction
          │
          ▼
   Prompt Preparation
          │
          ▼
      Gemini API
          │
          ▼
     AI Analysis
          │
          ▼
   Output Generation
       │          │
       ▼          ▼
     TXT         JSON
     Report      Report

Simple Pipeline

Input → Python → Content Extraction → Gemini API → AI Analysis → Final
Output

4. Technologies Used

Python

Python is used as the main programming language for controlling the
complete workflow.

Gemini API

The Gemini API is used as the AI processing component. It receives the
prepared prompt or image input and generates the analysis.

PyPDF2

PyPDF2 is used to extract text from PDF documents.

python-dotenv

python-dotenv loads the Gemini API key from the .env file.

CSV and JSON

Python's built-in csv and json modules are used to process
structured data.

pathlib

pathlib is used for file and directory management.

5. Main Processing Steps

Step 1 --- Input Detection

The program checks the file extension and determines whether the input
is TXT, CSV, PDF, image, JSON, Markdown, or another type.

Step 2 --- Content Extraction

The appropriate processing function is selected:

TXT/Markdown → text is read directly.

CSV → rows are converted into JSON-formatted text.

PDF → text is extracted using PyPDF2.

JSON → structured data is loaded and formatted.

Image → the image is sent directly to Gemini for visual analysis.

Step 3 --- AI Prompt Preparation

The program prepares a structured prompt containing:

Input type

Input name

Analysis instructions

Extracted input content

The requested analysis includes:

Executive Summary

Main Information

Important Points

Key Findings

Data Analysis, when applicable

Questions and Answers, when applicable

Conclusion

Step 4 --- Gemini AI Processing

The prepared information is sent to the Gemini API.

The pipeline also includes a retry mechanism for temporary API failures.

Step 5 --- Output Generation

For file analysis, the result is saved as:

output/
├── sample_analysis.txt
└── sample_analysis.json

For user questions:

output/
└── user_question_answer.txt

6. Example Input

sample.txt

Artificial Intelligence in Automation

Artificial Intelligence can automate repetitive tasks and help organizations
analyze information faster.

An AI pipeline can accept different types of input, process the information
using Python, send it to an AI model, and generate a useful report.

The main benefits are automation, faster analysis, and structured output.

7. Example Output

EXECUTIVE SUMMARY

The input explains how Artificial Intelligence can be used to automate
repetitive tasks and analyze information.

MAIN INFORMATION

- AI can automate repetitive activities.
- AI can help analyze information quickly.
- A pipeline can connect input, Python processing, an AI model,
  and final output.

KEY FINDINGS

1. Automation can reduce manual work.
2. Python can prepare and process different input formats.
3. An AI model can generate structured analysis.
4. The final result can be stored as a report.

CONCLUSION

AI pipelines provide a practical way to connect data processing
with AI analysis and automated report generation.

8. Project Structure

Assignment_No_3/
│
├── input/
│   ├── sample.csv
│   ├── sample.jpg
│   ├── sample.txt
│   └── SAYYAM SHAHID.pdf
│
├── output/
│   ├── ai_report.txt
│   ├── sample_analysis.json
│   └── sample_analysis.txt
│
├── .env
├── .gitignore
├── ai_pipeline.py
├── README.md
└── requirements.txt

9. Installation

Make sure Python is installed.

Install the required packages:

pip install -r requirements.txt

Or install the main dependencies directly:

pip install google-genai python-dotenv PyPDF2

10. API Key Configuration

Create a .env file in the project root:

GEMINI_API_KEY=your_gemini_api_key_here

The API key should not be hard-coded into the Python source code or
uploaded publicly.

11. Run the Project

Run:

python ai_pipeline.py

The program displays a menu:

=======================================================
              SELECT INPUT TYPE
=======================================================

1. Text File (.txt)
2. CSV File (.csv)
3. PDF File (.pdf)
4. Image (.jpg/.jpeg/.png/.webp)
5. User Question
6. JSON File (.json)
7. Markdown File (.md)
8. Exit

Select the required option and follow the instructions.

12. User Question Workflow

The pipeline also supports direct questions.

User Question
      ↓
Python receives question
      ↓
Prompt preparation
      ↓
Gemini API
      ↓
AI Answer
      ↓
user_question_answer.txt

The generated answer is displayed in the terminal and saved to the
output folder.

13. Error Handling

The project includes several error-handling mechanisms:

Missing API key detection

File existence checking

Invalid file-selection handling

Empty user-question validation

Gemini API retry mechanism

Exponential waiting between retry attempts

14. Limitations

Some limitations of the pipeline are:

A valid Gemini API key is required.

The configured Gemini model must be available to the API account.

PDF extraction may be incomplete for scanned/image-only PDFs.

AI output depends on the quality and completeness of the input.

API failures or network problems can interrupt AI processing.

Large files may require additional chunking or token-management
logic in a production system.

15. Assignment Requirements Covered

Requirement     Implementation

Input           TXT, CSV, PDF, Image, JSON, Markdown, User Question
Processing      Python
AI Model        Gemini API
Output          TXT, JSON, AI Answer, Analysis
Pipeline        Multi-step automated workflow
Diagram         Included
Sample Input    Included
Sample Output   Included
Explanation     Included in assignment
Screenshots     VS Code / working pipeline screenshots

16. Learning Outcomes

Through this project, I learned how to:

Build an AI automation pipeline.

Work with multiple file formats.

Detect input types programmatically.

Extract information from documents.

Connect Python with an AI API.

Prepare structured prompts.

Process image input with an AI model.

Handle API errors and retries.

Generate structured TXT and JSON outputs.

Organize an AI project into reusable functions.

17. Author

Sayyam Shahid
BSCS --- 5th Semester
AI Automation Institute
FUUAST, Islamabad

LinkedIn

Connect with Sayyam Shahid on
LinkedIn

18. Conclusion

The Multi-Input AI Analysis Pipeline demonstrates how Python and an AI
API can be connected to automate information processing. Instead of
manually processing each input type, the system detects the input,
extracts or prepares its content, sends it to Gemini for analysis, and
saves the generated result.

This project provides a practical foundation for developing more
advanced AI automation systems involving document analysis, data
processing, multimodal AI, automated reporting, and intelligent
assistants.

Author: Sayyam Shahid
Assignment 3 --- AI Pipeline
BSCS Semester 5 | AI Automation Institute | FUUAST Islamabad