from fastapi import FastAPI

app = FastAPI(
    title="CubeHabits API",
    description="API da plataforma CubeHabits para gerenciamento de hábitos",
    version="0.0.1",
)


@app.get("/")
def read_root():
    return {"Hello": "World"}
