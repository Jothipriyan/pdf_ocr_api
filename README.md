# pdf_ocr_api

🚀 Features
✅ Extract text from PDFs (both digital and scanned)
✅ Accurate OCR using Tesseract
✅ Structured JSON response:

Page count

Total extracted text count

Per-page extracted text
✅ Robust error handling
✅ Swagger UI documentation at /docs


📦 Requirements
Python 3.8+

Tesseract OCR installed

Poppler installed (for pdf2image)



▶ Running the API
**uvicorn main:app --reload**


Success JSON Response
json
Copy
Edit
{
  "page_count": 5,
  "text_count": 2345,
  "ocr_data": [
    {"page_number": 1, "text": "Extracted text from page 1..."},
    {"page_number": 2, "text": "Extracted text from page 2..."}
    // ... continue for all pages
  ]
}
