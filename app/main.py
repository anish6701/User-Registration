from fastapi import FastAPI

app = FastAPI(title='Test')

@app.get("/")
async def root():
    return{"message":"Hello To User Registration"}