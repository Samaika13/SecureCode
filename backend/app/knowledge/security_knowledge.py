SECURITY_KNOWLEDGE = {

    "CWE-89": {
        "why":
            "SQL Injection allows attackers to manipulate database queries.",

        "impact":
            "Attackers may read, modify or delete sensitive database information.",

        "fix":
            "Use parameterized SQL queries instead of string concatenation."
    },

    "CWE-78": {
        "why":
            "Command Injection allows arbitrary operating system commands to be executed.",

        "impact":
            "An attacker may gain complete control of the server.",

        "fix":
            "Use subprocess.run(shell=False) and never concatenate user input."
    },

    "CWE-327": {
        "why":
            "Weak cryptographic algorithms can be broken using modern hardware.",

        "impact":
            "Passwords and sensitive information may be compromised.",

        "fix":
            "Use SHA-256 or stronger algorithms."
    },

    "CWE-22": {
        "why":
            "Path Traversal lets attackers access unintended files.",

        "impact":
            "Sensitive files such as passwords or configuration files may be exposed.",

        "fix":
            "Validate and sanitize all user-controlled file paths."
    },

    "CWE-798": {
        "why":
            "Hardcoded secrets may leak credentials if source code is exposed.",

        "impact":
            "Attackers can immediately use exposed credentials.",

        "fix":
            "Store secrets in environment variables or a secrets manager."
    }
}