from pathlib import Path

from app.scanners.python_ast_sql_scanner import PythonASTSQLScanner

findings = PythonASTSQLScanner.scan(
    Path("test_ast_sql.py")
)

if not findings:
    print("No findings")
else:
    for finding in findings:
        print(finding)