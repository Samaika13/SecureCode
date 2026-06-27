from pathlib import Path
from app.models.finding import Finding
from app.scanners.hardcoded_secret_scanner import HardcodedSecretScanner
from app.services.repo_service import RepositoryService
class ScanService:
    """coordinates scanning an entire repo"""

    @staticmethod
    def scan_repository(repo_path: Path) -> list[Finding]:
        