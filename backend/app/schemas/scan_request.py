from pydantic import BaseModel

class ScanRequest(BaseModel):
    repository_url: str