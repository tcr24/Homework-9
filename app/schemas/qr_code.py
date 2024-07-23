from pydantic import BaseModel
from typing import List, Optional

class QRCodeRequest(BaseModel):
    url: str
    size: Optional[int] = 10

class QRCodeResponse(BaseModel):
    message: str
    qr_code_url: str
    links: List[dict]
