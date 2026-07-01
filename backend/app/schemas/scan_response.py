from pydantic import BaseModel

from app.models.finding import Finding

class ScanResponse(BaseModel):
    repository: str
    total_findings: int
    findings: list[Finding]