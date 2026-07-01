from pydantic import BaseModel

class Finding(BaseModel):
    """represents a security finding detected by scanner"""

    file: str
    line: int
    keyword: str
    severity: str
    message: str