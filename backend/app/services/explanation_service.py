from app.knowledge.security_knowledge import SECURITY_KNOWLEDGE

class ExplanationService:
    """"Returns security explanations based on CWE IDs."""

    @staticmethod
    def explain(cwe: str):

        return SECURITY_KNOWLEDGE.get(
            cwe,
            {
                "why": "No explanation available.",
                "impact": "Unknown.",
                "fix": "No recommendation available."
            }
        )