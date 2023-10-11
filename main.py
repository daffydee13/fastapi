from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse

app = FastAPI(title="Databricks CRUD")
app.mount("/ui", StaticFiles(directory="ui"), name="ui")

@app.get("/", response_class=FileResponse)
async def get_index_html():
    return "ui/index.html"
