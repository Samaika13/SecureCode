from pathlib import Path
from app.models.finding import Finding

class HardcodedSecretScanner:
    """Detects possible hardcoded secrets in source code"""

    SECRET_KEYWORDS = {
    "API_KEY",
    "SECRET",
    "PASSWORD",
    "TOKEN",
    "ACCESS_KEY",
    "PRIVATE_KEY",
}
    
    @staticmethod
    def scan(file_path: Path) ->list[Finding]:
        findings: list[Finding] = []
        with open(file_path, "r", encoding="utf-8") as file:
            for line_number, line in enumerate(file, start=1):
                for keyword in HardcodedSecretScanner.SECRET_KEYWORDS:
                    if keyword in line.upper():
                        findings.append(
                            Finding(
                                file=str(file_path),
                                line=line_number,
                                keyword=keyword,
                                severity="HIGH",
                                message=f"Possible hardcoded {keyword} detected."
                            )
                        )
        return findings
