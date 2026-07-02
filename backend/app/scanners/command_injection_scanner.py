from pathlib import Path

from app.models.finding import Finding

class CommandInjectionScanner:
    """Detects possible command injection vulnerabilities."""

    DANGEROUS_PATTERNS = [
        "os.system(",
        "subprocess.call(",
        "subprocess.Popen(",
        "subprocess.run(",
        "os.popen(",
    ]

    @staticmethod
    def scan(file_path: Path) -> list[Finding]:
        findings = []

        with open(file_path, "r", encoding="utf-8") as file:
            for line_number, line in enumerate(file, start=1):
                for pattern in CommandInjectionScanner.DANGEROUS_PATTERNS:
                    if pattern.lower() in line.lower():
                        findings.append(
                            Finding(
                                scanner="Command Injection",
                                file=str(file_path),
                                line=line_number,
                                keyword=pattern,
                                severity="HIGH",
                                confidence="HIGH",
                                cwe="CWE-78",
                                message=f"Possible command injection using '{pattern}'.",
                                recommendation="Avoid executing user input. Prefer subprocess.run(..., shell=False)."
                            )
                        )
        return findings