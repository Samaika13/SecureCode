import ast
from pathlib import Path

from app.models.finding import Finding

class SQLVisitor(ast.NodeVisitor):

    def __init__(self, file_path: Path):
        self.file_path = file_path
        self.findings = []

    def visit_Call(self, node):
        if(
            isinstance(node.func, ast.Attribute)
            and node.func.attr == "execute"
        ):
            if node.args:
                first_arg = node.args[0]

                if isinstance(first_arg, ast.BinOp):
                    self.findings.append(
                        Finding(
                            scanner="Python AST SQL Scanner",
                            file=str(self.file_path),
                            line=node.lineno,
                            keyword="SQL Concatenation",
                            severity="HIGH",
                            confidence="HIGH",
                            cwe="CWE-89",
                            message="SQL query built using string concatenation.",
                            recommendation="Use parameterized SQL queries instead of building SQL using string concatenation."
                        )
                    )
        self.generic_visit(node)


class PythonASTSQLScanner:

    @staticmethod
    def scan(file_path: Path) -> list[Finding]:

        if file_path.suffix != ".py":
            return []
        
        try:
            tree = ast.parse(
                file_path.read_text(encoding="utf-8")
            )

        except Exception:
            return []
        
        visitor = SQLVisitor(file_path)
        visitor.visit(tree)
        return visitor.findings