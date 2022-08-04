from fastapi import FastAPI, status
from fastapi.responses import JSONResponse
from fastapi.responses import RedirectResponse

from os import getenv

app = FastAPI()

ENV_VAR = getenv('ENV_VAR')

@app.get("/health")
def health():
    return JSONResponse(status_code=status.HTTP_200_OK, content={"Status": "Healthy"})

@app.get("/")
def root():
    msg = "Hello from app runner!"
    if ENV_VAR:
        msg += f" {ENV_VAR}"
    return JSONResponse(status_code=status.HTTP_200_OK, content=msg)
    
@app.get("/learn")
def redirect():
    return RedirectResponse("https://www.apprunnerworkshop.com/")

if __name__ == '__main__':
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8080, log_level="info")