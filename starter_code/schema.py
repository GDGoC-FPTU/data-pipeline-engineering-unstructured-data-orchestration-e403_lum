from pydantic import BaseModel, Field

# ==========================================
# ROLE 1: LEAD DATA ARCHITECT
# ==========================================

class UnifiedDocument(BaseModel):
    """
    Hệ thống cần 6 trường thông tin chuẩn (document_id, source_type, author, category, content, timestamp).
    """
    document_id: str = Field(..., description="Định danh bản ghi (docId / video_id)")
    source_type: str = Field(..., description="Nguồn: PDF hoặc Video")
    author: str = Field(..., description="Tác giả / creator")
    category: str = Field(..., description="Danh mục nội dung")
    content: str = Field(..., description="Nội dung đã chuẩn hóa (text / transcript)")
    timestamp: str = Field(..., description="Thời điểm tạo hoặc publish")
