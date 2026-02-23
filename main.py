from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"mesaj": "Şener AI Sports Sistemi Çalışıyor 🔥"}
