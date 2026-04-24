# ==========================================
# ROLE 3: OBSERVABILITY & QA ENGINEER
# ==========================================

def run_semantic_checks(doc_dict: dict) -> bool:
    content = doc_dict.get("content", "")
    doc_id = doc_dict.get("document_id", "unknown")

    # Check 1: Empty content is a failure
    if not content or len(content.strip()) < 10:
        print(f"Watchman Alert: rejected {doc_id} - content empty or too short")
        return False

    # Check 2: Semantic corruption tags
    toxic_keywords = ["Null pointer exception", "OCR Error", "Traceback"]
    content_lower = content.lower()
    for word in toxic_keywords:
        if word.lower() in content_lower:
            print(f"Watchman Alert: rejected {doc_id} - toxic keyword: {word}")
            return False

    return True
