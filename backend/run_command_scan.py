from pathlib import Path

from app.scanners.command_injection_scanner import CommandInjectionScanner

findings = CommandInjectionScanner.scan(
    Path("test_command.py")
)

for finding in findings:
    print(finding)