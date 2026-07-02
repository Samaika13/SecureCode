from pathlib import Path

from app.models.finding import Finding
from app.scanners.hardcoded_secret_scanner import HardcodedSecretScanner
from app.scanners.sql_injection_scanner import SQLInjectionScanner
from app.scanners.command_injection_scanner import CommandInjectionScanner
from app.scanners.weak_crypto_scanner import WeakCryptoScanner
from app.services.repo_service import RepositoryService
from app.models.risk import RiskSummary


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
    
    @staticmethod
    def summarize_findings(findings: list[Finding]) -> dict[str, int]:
        """Counts findings by severity."""


        summary = {
            "HIGH": 0,
            "MEDIUM": 0,
            "LOW": 0,
        }

        for finding in findings:
            summary[finding.severity] += 1

        return summary
    
    @staticmethod
    def calculate_risk(findings: list[Finding]) -> RiskSummary:
        """Calculates an overall repository risk score"""

        score = 0

        for finding in findings:

            if finding.severity == "HIGH":
                score += 5

            elif finding.severity == "MEDIUM":
                score += 3
            
            elif finding.severity == "LOW":
                score += 1

        score=min(score, 100)

        if score >= 75:
            level = "HIGH"
        
        elif score >= 40:
            level = "MEDIUM"
        
        else:
            level = "LOW"

        return RiskSummary(
            score=score,
            level=level
        )