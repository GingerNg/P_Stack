from fastapi import FastAPI

app = FastAPI()
@app.get("/")
def first_api():
    return "hello world"


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}

# pip3 install fastapi uvicorn gunicorn
# gunicorn -w 4 -k uvicorn.workers.UvicornH11Worker main:app

# uvicorn fastapi_B:app --reload --host=0.0.0.0 --port=8080

#   --host TEXT                     Bind socket to this host.  [default:
#                                   127.0.0.1]
#   --port INTEGER                  Bind socket to this port.  [default: 8000]

# 查看API文档  http://IP:PORT/docs
