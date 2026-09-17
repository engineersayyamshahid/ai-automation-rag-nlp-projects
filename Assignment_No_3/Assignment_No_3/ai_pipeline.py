import os
import csv
import json
import time
from pathlib import Path

from dotenv import load_dotenv
from google import genai
from google.genai import types

import PyPDF2


# ============================================
# CONFIGURATION
# ============================================

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    raise ValueError(
        "GEMINI_API_KEY not found. "
        "Please add it to your .env file."
    )

client = genai.Client(api_key=API_KEY)

MODEL = "gemini-3.6-flash"

BASE_DIR = Path(__file__).parent

INPUT_DIR = BASE_DIR / "input"
OUTPUT_DIR = BASE_DIR / "output"

INPUT_DIR.mkdir(exist_ok=True)
OUTPUT_DIR.mkdir(exist_ok=True)


# ============================================
# BANNER
# ============================================

print("=" * 55)
print("          MULTI-INPUT AI ANALYSIS PIPELINE")
print("=" * 55)


# ============================================
# INPUT TYPE DETECTION
# ============================================

def detect_input_type(file_path):

    extension = file_path.suffix.lower()

    if extension == ".txt":
        return "TEXT"

    elif extension == ".csv":
        return "CSV"

    elif extension == ".pdf":
        return "PDF"

    elif extension in [".jpg", ".jpeg", ".png", ".webp"]:
        return "IMAGE"

    elif extension == ".json":
        return "JSON"

    elif extension == ".md":
        return "MARKDOWN"

    else:
        return "OTHER"


# ============================================
# TEXT PROCESSING
# ============================================

def read_text(file_path):

    with open(
        file_path,
        "r",
        encoding="utf-8"
    ) as file:

        return file.read()


# ============================================
# CSV PROCESSING
# ============================================

def read_csv(file_path):

    rows = []

    with open(
        file_path,
        "r",
        encoding="utf-8-sig",
        newline=""
    ) as file:

        reader = csv.DictReader(file)

        for row in reader:
            rows.append(row)

    return json.dumps(
        rows,
        indent=2,
        ensure_ascii=False
    )


# ============================================
# PDF PROCESSING
# ============================================

def read_pdf(file_path):

    text = ""

    with open(
        file_path,
        "rb"
    ) as file:

        reader = PyPDF2.PdfReader(file)

        print(
            f"Pages processed: {len(reader.pages)}"
        )

        for page in reader.pages:

            page_text = page.extract_text()

            if page_text:
                text += page_text + "\n"

    return text


# ============================================
# JSON PROCESSING
# ============================================

def read_json(file_path):

    with open(
        file_path,
        "r",
        encoding="utf-8"
    ) as file:

        data = json.load(file)

    return json.dumps(
        data,
        indent=2,
        ensure_ascii=False
    )


# ============================================
# IMAGE MIME TYPE
# ============================================

def get_mime_type(file_path):

    extension = file_path.suffix.lower()

    mime_types = {

        ".jpg": "image/jpeg",
        ".jpeg": "image/jpeg",
        ".png": "image/png",
        ".webp": "image/webp"

    }

    return mime_types.get(
        extension,
        "application/octet-stream"
    )


# ============================================
# GEMINI AI PROCESSING
# ============================================

def ask_gemini(prompt, image_path=None):

    max_retries = 5

    for attempt in range(max_retries):

        try:

            # --------------------------------
            # IMAGE INPUT
            # --------------------------------

            if image_path:

                image_bytes = image_path.read_bytes()

                image_part = types.Part.from_bytes(
                    data=image_bytes,
                    mime_type=get_mime_type(image_path)
                )

                response = client.models.generate_content(

                    model=MODEL,

                    contents=[
                        image_part,
                        prompt
                    ]
                )

            # --------------------------------
            # TEXT / DATA INPUT
            # --------------------------------

            else:

                response = client.models.generate_content(

                    model=MODEL,

                    contents=prompt
                )

            return response.text

        except Exception as error:

            print(
                f"\nGemini request failed "
                f"(attempt {attempt + 1}/{max_retries})"
            )

            print(f"Error: {error}")

            # Retry
            if attempt < max_retries - 1:

                wait_time = 2 ** attempt

                print(
                    f"Retrying in "
                    f"{wait_time} seconds..."
                )

                time.sleep(wait_time)

            else:

                print(
                    "\nGemini request failed "
                    "after multiple attempts."
                )

                raise


# ============================================
# SAVE FILE OUTPUT
# ============================================

def save_output(
    report,
    input_name,
    input_type
):

    # Clean filename
    safe_name = Path(input_name).stem

    txt_file = (
        OUTPUT_DIR /
        f"{safe_name}_analysis.txt"
    )

    json_file = (
        OUTPUT_DIR /
        f"{safe_name}_analysis.json"
    )

    # ----------------------------------------
    # TEXT OUTPUT
    # ----------------------------------------

    with open(
        txt_file,
        "w",
        encoding="utf-8"
    ) as file:

        file.write(report)

    # ----------------------------------------
    # JSON OUTPUT
    # ----------------------------------------

    data = {

        "pipeline":
            "Multi-Input AI Analysis Pipeline",

        "input_name":
            input_name,

        "input_type":
            input_type,

        "ai_model":
            MODEL,

        "analysis":
            report
    }

    with open(
        json_file,
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            data,
            file,
            indent=4,
            ensure_ascii=False
        )

    print("\nOutput saved:")

    print(
        f"TXT : {txt_file}"
    )

    print(
        f"JSON: {json_file}"
    )


# ============================================
# USER QUESTION PROCESSING
# ============================================

def process_user_question():

    print("\n" + "-" * 55)
    print("                 USER QUESTION")
    print("-" * 55)

    question = input(
        "\nEnter your question: "
    ).strip()

    if not question:

        print(
            "\nQuestion cannot be empty."
        )

        return

    print(
        "\n[1/3] Processing user question..."
    )

    prompt = f"""
You are an intelligent AI assistant.

Answer the user's question accurately,
clearly, and helpfully.

USER QUESTION:

{question}

Instructions:

1. Give a direct answer.
2. Explain important details.
3. Use simple and clear language.
4. Do not invent information.
5. If the question requires reasoning,
   explain the reasoning briefly.
"""

    print(
        "\n[2/3] Sending question to Gemini AI..."
    )

    answer = ask_gemini(prompt)

    print(
        "\n[3/3] Generating final answer..."
    )

    output_file = (
        OUTPUT_DIR /
        "user_question_answer.txt"
    )

    with open(
        output_file,
        "w",
        encoding="utf-8"
    ) as file:

        file.write(
            "USER QUESTION\n"
        )

        file.write(
            question
        )

        file.write(
            "\n\nAI ANSWER\n"
        )

        file.write(
            answer
        )

    print("\n" + "=" * 55)
    print("                  AI ANSWER")
    print("=" * 55)

    print("\n")
    print(answer)

    print(
        f"\nAnswer saved to: {output_file}"
    )


# ============================================
# FILE PIPELINE
# ============================================

def run_pipeline(file_path):

    file_path = Path(file_path)

    # ----------------------------------------
    # CHECK FILE
    # ----------------------------------------

    if not file_path.exists():

        raise FileNotFoundError(
            f"File not found: {file_path}"
        )

    # ----------------------------------------
    # DETECT TYPE
    # ----------------------------------------

    input_type = detect_input_type(
        file_path
    )

    print("\n" + "-" * 55)

    print(
        f"Input File   : {file_path.name}"
    )

    print(
        f"Detected Type: {input_type}"
    )

    print("-" * 55)

    # ----------------------------------------
    # STEP 1
    # ----------------------------------------

    print(
        "\n[1/4] Reading and processing input..."
    )

    content = ""

    image_path = None

    # ----------------------------------------
    # TEXT
    # ----------------------------------------

    if input_type in [
        "TEXT",
        "MARKDOWN"
    ]:

        content = read_text(
            file_path
        )

    # ----------------------------------------
    # CSV
    # ----------------------------------------

    elif input_type == "CSV":

        content = read_csv(
            file_path
        )

    # ----------------------------------------
    # PDF
    # ----------------------------------------

    elif input_type == "PDF":

        content = read_pdf(
            file_path
        )

    # ----------------------------------------
    # JSON
    # ----------------------------------------

    elif input_type == "JSON":

        content = read_json(
            file_path
        )

    # ----------------------------------------
    # IMAGE
    # ----------------------------------------

    elif input_type == "IMAGE":

        image_path = file_path

        content = (
            "The input is an image. "
            "The image will be directly "
            "provided to the Gemini AI model "
            "for visual analysis."
        )

    # ----------------------------------------
    # OTHER
    # ----------------------------------------

    else:

        content = (
            f"The input is a file with "
            f"extension {file_path.suffix}. "
            f"Analyze any useful information "
            f"that can be extracted."
        )

    print(
        f"Characters processed: "
        f"{len(content)}"
    )

    # ----------------------------------------
    # STEP 2
    # ----------------------------------------

    print(
        "\n[2/4] Preparing AI analysis..."
    )

    prompt = f"""
You are an AI document, data,
and information analysis assistant.

Analyze the provided input carefully.

========================================
INPUT INFORMATION
========================================

Input Type:
{input_type}

Input Name:
{file_path.name}

========================================
TASK
========================================

Analyze the input and produce a useful,
structured response.

Your analysis should include:

1. Executive Summary
2. Main Information
3. Important Points
4. Key Findings
5. Data Analysis (if applicable)
6. Questions and Answers (if applicable)
7. Conclusion

========================================
INPUT-SPECIFIC INSTRUCTIONS
========================================

TEXT:
Summarize the text and identify
important concepts and information.

CSV:
Analyze the dataset, identify patterns,
calculate useful observations when possible,
and mention important trends.

PDF:
Summarize the document and extract
important information.

IMAGE:
Describe the visible content, identify
important text or objects, and explain
the overall meaning of the image.

JSON:
Analyze the structured data and identify
important information and patterns.

MARKDOWN:
Analyze the document content and provide
a structured summary.

OTHER:
Analyze whatever useful information
is available.

========================================
IMPORTANT
========================================

Do not invent information.

Only make claims that are supported
by the provided input.

INPUT DATA:

{content}
"""

    # ----------------------------------------
    # STEP 3
    # ----------------------------------------

    print(
        "\n[3/4] Sending data to Gemini AI..."
    )

    report = ask_gemini(
        prompt,
        image_path=image_path
    )

    # ----------------------------------------
    # STEP 4
    # ----------------------------------------

    print(
        "\n[4/4] Saving AI results..."
    )

    save_output(
        report,
        file_path.name,
        input_type
    )

    # ----------------------------------------
    # COMPLETE
    # ----------------------------------------

    print("\n" + "=" * 55)
    print(
        "       PIPELINE COMPLETED SUCCESSFULLY"
    )
    print("=" * 55)

    print("\nAI RESULT:\n")

    print(report)


# ============================================
# FILE SELECTION MENU
# ============================================

def select_file(
    extensions
):

    files = [

        file

        for file in INPUT_DIR.iterdir()

        if file.is_file()

        and file.suffix.lower()
        in extensions
    ]

    if not files:

        print(
            "\nNo matching files found "
            "in the input folder."
        )

        print(
            f"\nInput folder:\n{INPUT_DIR}"
        )

        return None

    print(
        "\nFiles available:"
    )

    for index, file in enumerate(
        files,
        start=1
    ):

        print(
            f"{index}. {file.name}"
        )

    selection = input(
        "\nSelect file number: "
    ).strip()

    try:

        index = int(selection) - 1

        return files[index]

    except (
        ValueError,
        IndexError
    ):

        print(
            "\nInvalid file selection."
        )

        return None


# ============================================
# MAIN MENU
# ============================================

def main():

    while True:

        print("\n")
        print("=" * 55)
        print("              SELECT INPUT TYPE")
        print("=" * 55)

        print(
            "\n1. Text File (.txt)"
        )

        print(
            "2. CSV File (.csv)"
        )

        print(
            "3. PDF File (.pdf)"
        )

        print(
            "4. Image (.jpg/.jpeg/.png/.webp)"
        )

        print(
            "5. User Question"
        )

        print(
            "6. JSON File (.json)"
        )

        print(
            "7. Markdown File (.md)"
        )

        print(
            "8. Exit"
        )

        print(
            "\n" + "-" * 55
        )

        choice = input(
            "Enter your choice (1-8): "
        ).strip()

        # ====================================
        # TEXT
        # ====================================

        if choice == "1":

            file_path = select_file(
                [".txt"]
            )

            if file_path:
                run_pipeline(file_path)

        # ====================================
        # CSV
        # ====================================

        elif choice == "2":

            file_path = select_file(
                [".csv"]
            )

            if file_path:
                run_pipeline(file_path)

        # ====================================
        # PDF
        # ====================================

        elif choice == "3":

            file_path = select_file(
                [".pdf"]
            )

            if file_path:
                run_pipeline(file_path)

        # ====================================
        # IMAGE
        # ====================================

        elif choice == "4":

            file_path = select_file(
                [
                    ".jpg",
                    ".jpeg",
                    ".png",
                    ".webp"
                ]
            )

            if file_path:
                run_pipeline(file_path)

        # ====================================
        # USER QUESTION
        # ====================================

        elif choice == "5":

            process_user_question()

        # ====================================
        # JSON
        # ====================================

        elif choice == "6":

            file_path = select_file(
                [".json"]
            )

            if file_path:
                run_pipeline(file_path)

        # ====================================
        # MARKDOWN
        # ====================================

        elif choice == "7":

            file_path = select_file(
                [".md"]
            )

            if file_path:
                run_pipeline(file_path)

        # ====================================
        # EXIT
        # ====================================

        elif choice == "8":

            print(
                "\nThank you for using "
                "the AI Pipeline."
            )

            break

        # ====================================
        # INVALID
        # ====================================

        else:

            print(
                "\nInvalid choice."
            )

            print(
                "Please select a number "
                "between 1 and 8."
            )


# ============================================
# PROGRAM START
# ============================================

if __name__ == "__main__":

    main()