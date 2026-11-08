from fastapi import APIRouter, FastAPI

router = APIRouter(prefix="/api")


@router.get("/hello")
def hello():
    return {"message": "Hello from Terraform-deployed backend version 2"}


@router.get("/health")
def health():
    return {"status": "ok"}


app = FastAPI()
app.include_router(router)
