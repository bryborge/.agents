import sys
import argparse
try:
    from pypdf import PdfReader, PdfWriter
except ImportError:
    print("Error: The 'pypdf' library is required. Install it using 'pip install pypdf'.", file=sys.stderr)
    sys.exit(1)


def extract_text(pdf_path):
    try:
        reader = PdfReader(pdf_path)
        text = ""
        for page in reader.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"

        if not text.strip():
            print("No extractable text found. The PDF might be scanned or image-based.", file=sys.stderr)
            sys.exit(1)

        print(text)
    except Exception as e:
        print(f"Error extracting text: {e}", file=sys.stderr)
        sys.exit(1)


def merge_pdfs(output_path, input_paths):
    try:
        writer = PdfWriter()
        for path in input_paths:
            reader = PdfReader(path)
            for page in reader.pages:
                writer.add_page(page)

        with open(output_path, "wb") as f:
            writer.write(f)
        print(f"Successfully merged {len(input_paths)} files into {output_path}")
    except Exception as e:
        print(f"Error merging files: {e}", file=sys.stderr)
        sys.exit(1)


def split_pdf(input_path, output_path, start_page, end_page):
    try:
        reader = PdfReader(input_path)
        total_pages = len(reader.pages)

        # Validate page numbers (user input is 1-indexed)
        if start_page < 1 or end_page < 1:
            print("Error: Page numbers must be >= 1", file=sys.stderr)
            sys.exit(1)
        if start_page > end_page:
            print("Error: Start page must be <= end page", file=sys.stderr)
            sys.exit(1)
        if start_page > total_pages or end_page > total_pages:
            print(f"Error: PDF has only {total_pages} pages", file=sys.stderr)
            sys.exit(1)

        writer = PdfWriter()
        # Convert to 0-indexed for internal use
        for page_num in range(start_page - 1, end_page):
            writer.add_page(reader.pages[page_num])

        with open(output_path, "wb") as f:
            writer.write(f)
        pages_extracted = end_page - start_page + 1
        print(f"Successfully split PDF: extracted {pages_extracted} page(s) (pages {start_page}-{end_page}) to {output_path}")
    except Exception as e:
        print(f"Error splitting PDF: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="PDF processing tool for Agent Skills")
    subparsers = parser.add_subparsers(dest="command", required=True)

    # Extract command
    extract_parser = subparsers.add_parser("extract", help="Extract text from a PDF")
    extract_parser.add_argument("file", help="Path to the target PDF file")

    # Merge command
    merge_parser = subparsers.add_parser("merge", help="Merge multiple PDFs together")
    merge_parser.add_argument("output", help="Path for the merged output PDF")
    merge_parser.add_argument("inputs", nargs="+", help="Paths to the input PDFs to be merged")

    # Split command
    split_parser = subparsers.add_parser("split", help="Extract a page range from a PDF")
    split_parser.add_argument("input", help="Path to the input PDF file")
    split_parser.add_argument("output", help="Path for the output PDF file")
    split_parser.add_argument("start_page", type=int, help="Starting page number (1-indexed)")
    split_parser.add_argument("end_page", type=int, help="Ending page number (1-indexed, inclusive)")

    args = parser.parse_args()

    if args.command == "extract":
        extract_text(args.file)
    elif args.command == "merge":
        merge_pdfs(args.output, args.inputs)
    elif args.command == "split":
        split_pdf(args.input, args.output, args.start_page, args.end_page)
