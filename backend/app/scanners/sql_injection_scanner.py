from pathlib import Path

from app.models.finding import Finding

class SQLInjectionScanner:
    """Detects possible SQL injection vulnerabilities"""

    SQL_PATTERNS = ["SELECT", "INSERT", "UPDATE", "DELETE", "EXECUTE"]

    @staticmethod
    def scan(file_path: Path) -> list[Finding]:
        findings = []

        with open(file_path, "r", encoding="utf-8") as file:
            for line_number, line in enumerate(file, start=1):
                for keyword in SQLInjectionScanner.SQL_PATTERNS:
                    if keyword in line.upper():
                        findings.append(
                            Finding(
                                scanner="SQL Injection",
                                file=str(file_path),
                                line=line_number,
                                keyword=keyword,
                                severity="MEDIUM",
                                confidence="HIGH",
                                cwe="CWE-89",
                                message=f"Possible SQL query detected containing '{keyword}'.",
                                recommendation="Use parameterized SQL queries."
                            )
                        )

        return findings