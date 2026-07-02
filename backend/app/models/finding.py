from pydantic import BaseModel

class Finding(BaseModel):
    """represents a security finding detected by scanner"""

    scanner: str
    file: str
    line: int
    keyword: str
    severity: str
    confidence: str
    cwe: str
    message: str
    recommendation: str