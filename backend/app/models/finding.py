from dataclasses import dataclass

@dataclass
class Finding:
    """represents a security finding detected by scanner"""

    file: str
    line: int
    keyword: str
    severity: str
    message: str