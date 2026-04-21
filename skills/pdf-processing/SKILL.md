---
name: pdf-processing
description: Extract text and tables from PDF files, merge multiple PDFs, and split PDFs by page range. Use this skill when dealing with PDF documents.
license: apache-2.0
metadata:
  author: bryborge
  version: "1.0"
---

# PDF Processing Skill

## Prerequisites

This skill relies on a bundled Python script located in `scripts/pdf_manager.py`. The script requires the `pypdf` library. If it is not installed in the environment, install it via `pip install pypdf` before proceeding.

## Execution Steps

### Extracting Text

When requested to read or extract text from a PDF, execute the script's `extract` command.

-   **Command**: `python scripts/pdf_manager.py extract <path_to_pdf>`
-   **Expected Output**: The script will output the extracted text to stdout.
-   **Agent Action**: Read the standard output and summarize, format, or return the text exactly as the user requested.
-   **Edge Cases**: If the PDF is image-based (scanned) or encrypted, the script will fail. Inform the user if OCR processing or a decryption password is required.

### Merging PDFs

When requested to combine multiple PDF files, execute the script's `merge` command.

-   **Command**: `python scripts/pdf_manager.py merge <output_path.pdf> <input_1.pdf> <input_2.pdf> ...`
-   **Expected Output**: A success message to stdout confirming the merged file path.
-   **Agent Action**: Verify that all input file paths exist before running the command. Once successful, provide the user with the path to the newly merged file.

### Splitting PDFs

When requested to extract a specific page range from a PDF, execute the script's `split` command.

-   **Command**: `python scripts/pdf_manager.py split <input_path.pdf> <output_path.pdf> <start_page> <end_page>`
-   **Parameters**: Both `start_page` and `end_page` are 1-indexed integers (inclusive). For example, pages 5 to 10 extracts pages 5, 6, 7, 8, 9, and 10.
-   **Expected Output**: A success message to stdout confirming the number of pages extracted and the output file path.
-   **Agent Action**: Verify that the input PDF file exists. Validate that the page range makes sense (start <= end). Once successful, provide the user with the path to the newly split PDF file and confirm the page range extracted.

## Output Format

-   **For Text Extraction**: Present the extracted content using markdown blockquotes or code blocks to separate it from your conversational response.
-   **For Merging**: Provide a clear confirmation message with the absolute or relative path to the new merged document.
-   **For Splitting**: Provide a clear confirmation message with the absolute or relative path to the new split document and the page range that was extracted.
