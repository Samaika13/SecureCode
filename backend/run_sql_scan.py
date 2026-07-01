from pathlib import Path

from app.scanners.sql_injection_scanner import SQLInjectionScanner

findings = SQLInjectionScanner.scan(
    Path("test_sql.py")
)

for finding in findings:
    print(finding)