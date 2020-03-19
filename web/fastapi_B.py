from fastapi import FastAPI

app = FastAPI()
@app.get("/")
def first_api():
    return "hello world"

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}


"""
FastAPI 是基于 Starlette 构建的，其性能与 NodeJS 和 Go 相当，而且它还支持原生 WebSocket 和 GraphQL。
Starlette 是一个轻量级的 ASGI 框架 / 工具包，具有包括 WebSocket 和 GraphQL 支持，进程内后台任务和真正的高性能等一系列特性。
除此之外，还有 100% 类型注解的代码库和无依赖。可以把它看作是一版非常轻量的、现代的和异步的 Flask。
"""
