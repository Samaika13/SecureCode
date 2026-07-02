from pathlib import Path

from app.models.finding import Finding

class PathTraversalScanner:
    """Detects possible path traversal vulnerabilities."""

    FILE_PATTERNS =[
        "open(",
        "Path(",
        "os.open(",
        "os.listdir(",
        "os.walk(",
        "shutil.copy(",
        "shutil.move(",
    ]

    @staticmethod
    def scan(file_path: Path) -> list[Finding]:
        findings = []

        with open(file_path, "r", encoding="utf-8") as file:
            for line_number, line in enumerate(file, start=1):
                for pattern in PathTraversalScanner.FILE_PATTERNS:
                    if pattern.lower() in line.lower():
                        findings.append(
                            Finding(
                                scanner="Path Traversal",
                                file=str(file_path),
                                line=line_number,
                                keyword=pattern,
                                severity="MEDIUM",
                                confidence="HIGH",
                                cwe="CWE-22",
                                message=f"Potential filesystem operation using {pattern}",
                                recommendation="Validate user-controlled paths."
                            )
                        )
        return findings
