from pathlib import Path

from app.scanners.weak_crypto_scanner import WeakCryptoScanner

findings = WeakCryptoScanner.scan(
    Path("test_crypto.py")
)

for finding in findings:
    print(finding)