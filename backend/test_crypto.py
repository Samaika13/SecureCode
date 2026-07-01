import hashlib

password = "secret123"

hash1 = hashlib.md5(password.encode()).hexdigest()

hash2 = hashlib.sha1(password.encode()).hexdigest()

hash3 = hashlib.sha256(password.encode()).hexdigest()