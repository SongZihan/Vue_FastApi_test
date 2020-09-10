from fastapi import FastAPI
from starlette.responses import FileResponse
from starlette.staticfiles import StaticFiles

app = FastAPI()

# 绑定静态文件
app.mount("/static", StaticFiles(directory="static"), name="static")



@app.get("/")
async def root():
    return FileResponse('templates/index.html')


if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app,host='localhost',port=8000)