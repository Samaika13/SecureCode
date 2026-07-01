from pathlib import Path

from app.models.finding import Finding
from app.scanners.hardcoded_secret_scanner import HardcodedSecretScanner
from app.scanners.sql_injection_scanner import SQLInjectionScanner
from app.scanners.command_injection_scanner import CommandInjectionScanner
from app.scanners.weak_crypto_scanner import WeakCryptoScanner
from app.services.repo_service import RepositoryService


class ScanService:
    """Coordinates scanning an entire repository."""

    SCANNERS = [
        HardcodedSecretScanner,
        SQLInjectionScanner,
        CommandInjectionScanner,
        WeakCryptoScanner,
    ]

    @staticmethod
    def scan_repository(repo_path: Path) -> list[Finding]:
        source_files = RepositoryService.list_source_files(repo_path)
        
        all_findings: list[Finding] = []

        for source_file in source_files:
            for scanner in ScanService.SCANNERS:
                findings = scanner.scan(source_file)
                all_findings.extend(findings)

        return all_findings