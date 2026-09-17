# 🤖 Multi-Input AI Analysis Pipeline

<p align="center">
  <strong>AI-Powered Multi-Format Document & Data Analysis using Python + Gemini API</strong>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/Gemini-API-4285F4?style=for-the-badge&logo=google&logoColor=white" alt="Gemini API">
  <img src="https://img.shields.io/badge/AI-Automation-00C2FF?style=for-the-badge" alt="AI Automation">
  <img src="https://img.shields.io/badge/Status-Completed-00C853?style=for-the-badge" alt="Status">
</p>

<p align="center">
  <a href="https://github.com/">
    <img src="https://img.shields.io/badge/GitHub-Repository-181717?style=flat-square&logo=github" alt="GitHub">
  </a>
  <img src="https://img.shields.io/badge/Assignment-03-6C63FF?style=flat-square" alt="Assignment">
  <img src="https://img.shields.io/badge/BSCS-5th%20Semester-FF6B6B?style=flat-square" alt="BSCS">
</p>

---

## 📌 Project Information

| Field                | Details                    |
| -------------------- | -------------------------- |
| 📚 **Assignment**    | Assignment 3 — AI Pipeline |
| 👨‍💻 **Author**     | Sayyam Shahid              |
| 🎓 **Program**       | BSCS                       |
| 📖 **Semester**      | 5th Semester               |
| 🤖 **Internship**    | AI Automation Institute    |
| 🏫 **University**    | FUUAST, Islamabad          |
| 🧠 **AI Model**      | Gemini API                 |
| 🐍 **Main Language** | Python                     |
| ⚙️ **Project Type**  | AI Automation Pipeline     |

---

# 🌟 Project Overview

**Multi-Input AI Analysis Pipeline** is a Python-based AI automation system that accepts multiple types of input, automatically identifies the input format, extracts or prepares its content, sends the information to the **Gemini AI model**, and generates a structured analysis report.

The purpose of this project is to reduce repetitive manual work involved in:

* 📄 Reading documents
* 📊 Examining structured data
* 🖼️ Understanding images
* ❓ Answering user questions
* 📝 Generating reports
* 🔄 Automating information-processing workflows

Instead of creating a separate program for every file type, this project provides a **single automated pipeline**.

---

# 🎯 Main Objective

The main objective is to build an AI pipeline capable of handling different input formats through one unified workflow:

```text
Different Inputs
      ↓
Input Detection
      ↓
Content Extraction
      ↓
Prompt Preparation
      ↓
Gemini AI
      ↓
AI Analysis
      ↓
Structured Output
```

---

# 📥 Supported Inputs

The pipeline currently supports:

| Input            | Extension                        | Processing                          |
| ---------------- | -------------------------------- | ----------------------------------- |
| 📄 Text          | `.txt`                           | Direct text extraction              |
| 📊 CSV           | `.csv`                           | Rows converted into structured text |
| 📕 PDF           | `.pdf`                           | Text extraction using PyPDF2        |
| 🖼️ Image        | `.jpg`, `.jpeg`, `.png`, `.webp` | Direct Gemini visual analysis       |
| 🗂️ JSON         | `.json`                          | Structured data loading             |
| 📝 Markdown      | `.md`                            | Direct text extraction              |
| 💬 User Question | —                                | Direct AI question-answering        |

---

# 🔥 Key Features

### 🧩 Multi-Input Support

One pipeline can process multiple input formats.

### 🔍 Automatic Input Detection

The program determines the appropriate processing method based on the file extension.

### 📄 Document Processing

TXT, Markdown, CSV, PDF, and JSON files can be processed automatically.

### 👁️ Image Analysis

Images can be sent to Gemini for multimodal visual analysis.

### 🤖 Gemini AI Integration

The extracted information is analyzed using Google's Gemini API.

### 🔄 Retry Mechanism

Temporary API failures are handled using retry logic with exponential waiting.

### 📑 Structured Reports

The AI result can be stored in:

* TXT
* JSON

### 🔐 Environment-Based API Key

The Gemini API key is loaded securely through `.env`.

### ⚡ Automated Workflow

The complete process is controlled through Python.

---

# 🏗️ System Architecture

```text
                    ┌──────────────────────┐
                    │      USER INPUT      │
                    └──────────┬───────────┘
                               │
          ┌────────────────────┼────────────────────┐
          │                    │                    │
          ▼                    ▼                    ▼
     ┌─────────┐          ┌─────────┐         ┌─────────┐
     │  Files  │          │ Images  │         │Question │
     └────┬────┘          └────┬────┘         └────┬────┘
          │                    │                    │
          └────────────────────┼────────────────────┘
                               ▼
                    ┌──────────────────────┐
                    │  Python Input        │
                    │  Detection            │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │ Content Extraction   │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │ Prompt Preparation   │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │     Gemini API       │
                    │     AI Model         │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │    AI Analysis       │
                    └──────────┬───────────┘
                               │
                 ┌─────────────┴─────────────┐
                 ▼                           ▼
        ┌────────────────┐          ┌────────────────┐
        │   TXT Report   │          │   JSON Report  │
        └────────────────┘          └────────────────┘
```

---

# 🔄 Complete Pipeline

```text
┌────────────────┐
│     INPUT      │
│ TXT / CSV /    │
│ PDF / IMAGE /  │
│ JSON / MD / Q  │
└───────┬────────┘
        │
        ▼
┌────────────────┐
│ INPUT DETECTION│
└───────┬────────┘
        │
        ▼
┌────────────────┐
│    CONTENT     │
│   EXTRACTION   │
└───────┬────────┘
        │
        ▼
┌────────────────┐
│     PROMPT     │
│   PREPARATION  │
└───────┬────────┘
        │
        ▼
┌────────────────┐
│   GEMINI API   │
└───────┬────────┘
        │
        ▼
┌────────────────┐
│   AI ANALYSIS  │
└───────┬────────┘
        │
        ▼
┌─────────────────────────┐
│     OUTPUT GENERATION   │
├─────────────┬───────────┤
│             │           │
▼             ▼           ▼
TXT          JSON       Terminal
Report       Report     Response
```

---

# ⚙️ Processing Workflow

## 1️⃣ Input Detection

Python checks the selected file and determines its format.

```text
File
 ↓
Extension Check
 ↓
┌──────┬──────┬──────┬──────┬──────┐
TXT   CSV    PDF   IMAGE   JSON    MD
```

---

## 2️⃣ Content Extraction

Each format uses an appropriate processing method.

```text
TXT / MD
   ↓
Read Text

CSV
   ↓
Read Rows
   ↓
Structured Text

PDF
   ↓
PyPDF2
   ↓
Extract Text

JSON
   ↓
json.load()
   ↓
Formatted Data

IMAGE
   ↓
Gemini Vision Input
```

---

## 3️⃣ Prompt Preparation

The pipeline prepares a structured prompt containing:

* Input type
* Input filename
* Analysis instructions
* Extracted content
* Required report sections

The AI is instructed to provide:

```text
Executive Summary
        ↓
Main Information
        ↓
Important Points
        ↓
Key Findings
        ↓
Data Analysis
        ↓
Questions & Answers
        ↓
Conclusion
```

---

# 🤖 Gemini AI Processing

The prepared information is sent to the Gemini API.

```text
Python Application
       │
       ▼
Prepared Prompt
       │
       ▼
Gemini API
       │
       ▼
Gemini Model
       │
       ▼
Generated Analysis
       │
       ▼
Python Application
```

The pipeline also includes a retry mechanism to handle temporary API or network failures.

---

# 📤 Output Generation

Generated analysis can be stored inside the `output/` directory.

```text
output/
│
├── sample_analysis.txt
├── sample_analysis.json
└── user_question_answer.txt
```

### TXT Output

Human-readable report containing the AI analysis.

### JSON Output

Structured output that can be reused by another application or automation workflow.

---

# 📝 Example Input

### `sample.txt`

```text
Artificial Intelligence in Automation

Artificial Intelligence can automate repetitive tasks and help
organizations analyze information faster.

An AI pipeline can accept different types of input, process the
information using Python, send it to an AI model, and generate
a useful report.

The main benefits are automation, faster analysis, and structured output.
```

---

# 📊 Example AI Output

```text
EXECUTIVE SUMMARY

The input explains how Artificial Intelligence can be used to
automate repetitive tasks and analyze information.

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
```

---

# 🖥️ Application Menu

When the program starts, the user receives an interactive menu:

```text
=======================================================
              MULTI-INPUT AI PIPELINE
=======================================================

1. Text File (.txt)
2. CSV File (.csv)
3. PDF File (.pdf)
4. Image (.jpg/.jpeg/.png/.webp)
5. User Question
6. JSON File (.json)
7. Markdown File (.md)
8. Exit

=======================================================
Select an option:
```

---

# 💬 User Question Workflow

The pipeline can also work without a file.

```text
             USER QUESTION
                   │
                   ▼
          Python Receives Input
                   │
                   ▼
            Prompt Preparation
                   │
                   ▼
               Gemini API
                   │
                   ▼
               AI Answer
                   │
                   ▼
        ┌──────────┴──────────┐
        ▼                     ▼
    Terminal             TXT File
                         Output
```

Example:

```text
Question:
What is artificial intelligence?

        ↓

Gemini AI

        ↓

AI-generated explanation

        ↓

output/user_question_answer.txt
```

---

#
