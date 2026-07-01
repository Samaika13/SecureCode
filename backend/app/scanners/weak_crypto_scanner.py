from pathlib import Path

from app.models.finding import Finding

class WeakCryptoScanner:
    """Detects weak cryptographic algorithms."""

    WEAK_ALGORITHMS = [
        "hashlin.md5(",
        "hashlib.sha1(",
        ".md5(",
        ".sha1(",
    ]

    @staticmethod
    def scan(file_path: Path) -> list[Finding]:
        findings = []

        with open(file_path, "r", encoding="utf-8") as file:
            for line_number, line in enumerate(file, start=1):
                for algorithm in WeakCryptoScanner.WEAK_ALGORITHMS:
                    if algorithm.lower() in line.lower():
                        findings.append(
                            Finding(
                                file=str(file_path),
                                line=line_number,
                                keyword=algorithm,
                                severity="MEDIUM",
                                message=f"Weak cryptographic algorithm '{algorithm}' detected."
                            )
                        )
        return findings