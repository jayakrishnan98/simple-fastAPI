# tf-backend-demo

Minimal FastAPI backend.

## Run locally

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn main:app --host 0.0.0.0 --port 8000
```

- `GET /api/hello` returns `{"message": "Hello from Terraform-deployed backend"}`
- `GET /api/health` returns `{"status": "ok"}`
