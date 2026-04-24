import re

# ==========================================
# ROLE 2: ETL/ELT BUILDER
# ==========================================

def clean_pdf_text(raw_text: str) -> str:
    # Remove noise like HEADER_PAGE_1 and FOOTER_PAGE_1
    cleaned = re.sub(r"HEADER_PAGE_\d+", "", raw_text)
    cleaned = re.sub(r"FOOTER_PAGE_\d+", "", cleaned)
    return cleaned.strip()

def process_pdf_data(raw_json: dict) -> dict:
    content = raw_json.get("extractedText", "")
    content = clean_pdf_text(content if isinstance(content, str) else str(content))
    return {
        "document_id": str(raw_json.get("docId") or ""),
        "source_type": "PDF",
        "author": str(raw_json.get("authorName") or "").strip(),
        "category": str(raw_json.get("docCategory") or ""),
        "content": content,
        "timestamp": str(raw_json.get("createdAt") or ""),
    }

def process_video_data(raw_json: dict) -> dict:
    transcript = raw_json.get("transcript", "")
    text = transcript if isinstance(transcript, str) else str(transcript)
    return {
        "document_id": str(raw_json.get("video_id") or ""),
        "source_type": "Video",
        "author": str(raw_json.get("creator_name") or "").strip(),
        "category": str(raw_json.get("category") or ""),
        "content": text,
        "timestamp": str(raw_json.get("published_timestamp") or ""),
    }
