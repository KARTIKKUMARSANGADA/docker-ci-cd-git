from fastapi import FastAPI

app = FastAPI()

# Root endpoint
@app.get("/")
def read_root():
    return {"message": "Hello, Docker + CI/CD 🚀"}

# Health check (useful for deployment)
@app.get("/health")
def health_check():
    return {"status": "OK"}

# Sample dynamic route
@app.get("/greet/{name}")
def greet(name: str):
    return {"message": f"Hello {name}!"}