from pydantic import BaseModel

from app.models.finding import Finding

from app.models.risk import RiskSummary


class ScanSummary(BaseModel):
    HIGH: int
    MEDIUM: int
    LOW: int

class ScanResponse(BaseModel):
    repository: str
    total_findings: int
    summary: ScanSummary
    risk: RiskSummary
    findings: list[Finding]