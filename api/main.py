from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Receipt(BaseModel):
    name: str
    total:float

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.put("/ingest-receipt")
def put_receipt(receipt_id: int, receipt:Receipt):

    return {"id":receipt_id, "receipt":receipt}