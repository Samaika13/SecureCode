from fastapi import FastAPI

app = FastAPI(
    title="SecureCode API",
    description="AI-powered security analysis platform",
    version="1.0.0"
)

@app.get("/")
def root():
    return {
        "message": "Welcome to SecureCode!",
        "status": "Backend is running 🚀"
    }