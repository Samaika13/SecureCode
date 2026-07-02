from pathlib import Path

from app.scanners.path_traversal_scanner import PathTraversalScanner

findings = PathTraversalScanner.scan(
    Path("test_path.py")
)

for finding in findings:
    print(finding)