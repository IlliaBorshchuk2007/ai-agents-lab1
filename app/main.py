from fastapi import FastAPI
from pydantic import BaseModel, Field, ConfigDict

app = FastAPI(title="Educational Videos API")


class Video(BaseModel):
    model_config = ConfigDict(str_strip_whitespace=True)

    title: str = Field(min_length=1)
    topic: str = Field(min_length=1)
    duration_minutes: int = Field(gt=0, strict=True)


videos = []


@app.post("/videos", status_code=201)
def create_video(video: Video):
    videos.append(video)
    return video


@app.get("/videos")
def get_videos():
    return videos


from app.ai import extract_video
from fastapi import HTTPException


class VideoText(BaseModel):
    text: str = Field(min_length=1)


@app.post("/videos/ai", status_code=201)
def create_video_ai(data: VideoText):
    result = extract_video(data.text)

    if result is None:
        raise HTTPException(
            status_code=422,
            detail="Недостатньо інформації. Вкажіть назву, тему та тривалість відео."
        )

    video = Video(**result)
    videos.append(video)

    return video
