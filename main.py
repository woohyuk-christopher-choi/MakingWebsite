from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

app = FastAPI()

# Static 파일 설정
app.mount("/static", StaticFiles(directory="./"), name="static")

@app.get("/", response_class=HTMLResponse)
async def read_root():
    with open('./main.html', 'r', encoding='utf-8') as html_file:
        return html_file.read()
    
@app.get("/download-resume")
def download_resume():
    return FileResponse("./WoohyukChoi_Resume.pdf", media_type='application/pdf', filename="WoohyukChoi_Resume.pdf")

@app.get("/download-paper1")
def download_resume():
    return FileResponse("./ISIS2023.pdf", media_type='application/pdf', filename="ISIS2023.pdf")

@app.get("/download-paper2")
def download_resume():
    return FileResponse("./IMS2023.pdf", media_type='application/pdf', filename="IMS2023.pdf")
