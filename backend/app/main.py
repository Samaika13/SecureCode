from fastapi import FastAPI, HTTPException

from app.schemas.scan_request import ScanRequest
from app.schemas.scan_response import ScanResponse
from app.services.repo_service import RepositoryService
from app.services.scan_service import ScanService

app = FastAPI(
    title="SecureCode API",
    description="AI-powered security analysis platform",
    version="1.0.0"
)

@app.get("/")
def root():
    return {
        "message": "Welcome to SecureCode!",
        "status": "Backend is running 🚀"
    }

@app.post("/scan", response_model=ScanResponse)
def scan(request: ScanRequest):
    """Scans repository for security vulnerabilities."""

    if not RepositoryService.validate_github_url(request.repository_url):
        raise HTTPException(
            status_code=400,
            detail="Invalid GitHub repository URL."
        )
    
    try:
        # clone the repo
        repo_path = RepositoryService.clone_repository(
            request.repository_url
        )

        # scan the repo
        findings = ScanService.scan_repository(repo_path)

        # return the results
        return ScanResponse(
            repository=repo_path.name,
            total_findings=len(findings),
            findings=findings
        )
    
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )