from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse, JSONResponse

app = FastAPI()

# Existing routers here...
# app.include_router(...)

# Serve frontend
app.mount("/", StaticFiles(directory="../frontend", html=True), name="frontend")

# Fallback for unknown routes
@app.exception_handler(404)
def not_found(request, exc):
    return FileResponse("../frontend/404.html")
@app.get("/favicon.ico")
def favicon():
    return FileResponse("../frontend/favicon.ico")