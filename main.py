from fastapi import FastAPI, File, UploadFile, HTTPException
from PyPDF2 import PdfReader
from pdf2image import convert_from_bytes
import pytesseract
import io

app = FastAPI(title="PDF OCR API")

@app.post("/extract-pdf")

async def extract_pdf(file: UploadFile = File()):
    if not file.filename.endswith(".pdf"):
        raise HTTPException(status_code=400, detail="Only PDF files are supported.")


    content = await file.read()
    reader = PdfReader(io.BytesIO(content))
    page_count = len(reader.pages)

    ocr_data = []
    total_text_length = 0

    for idx, page in enumerate(reader.pages, start=1):
        text = page.extract_text()
        if not text or len(text.strip()) == 0:
            # fallback to OCR on image
            images = convert_from_bytes(content, first_page=idx, last_page=idx,poppler_path=r'C:\Program Files (x86)\poppler-24.07.0\Library\bin')
            ocr_text = ""
            for image in images:
                ocr_text += pytesseract.image_to_string(image)
            text = ocr_text

        ocr_data.append({"page_number": idx, "text": text})
        total_text_length += len(text)

        return {
            "page_count": page_count,
            "text_count": total_text_length,
            "ocr_data": ocr_data
        }
