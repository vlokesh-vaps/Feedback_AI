# Feedback Assistant (FastAPI + Groq)

A small feedback assistant API with a built-in web UI, deployable on Render.

## Features

- FastAPI backend with `POST /chat`
- Built-in chat UI at `GET /`
- Health check at `GET /health`
- Groq model integration using `GROQ_API_KEY`

## Local Run

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
uvicorn main:app --reload
```

Open `http://127.0.0.1:8000`.

## Deploy to Render

### Option 1: Blueprint deploy (recommended)

1. Push this project to GitHub.
2. In Render, click **New +** -> **Blueprint**.
3. Connect the repository and deploy.
4. In the created service, set environment variable:
   - `GROQ_API_KEY`: your Groq API key

This repo includes `render.yaml`, which configures:
- `buildCommand`: `pip install -r requirements.txt`
- `startCommand`: `uvicorn main:app --host 0.0.0.0 --port $PORT`
- `PYTHON_VERSION`: `3.12.8`

### Option 2: Manual Web Service

1. In Render, create a **Web Service** from this repo.
2. Runtime: `Python 3.12`.
3. Build command: `pip install -r requirements.txt`.
4. Start command: `uvicorn main:app --host 0.0.0.0 --port $PORT`.
5. Add environment variable `GROQ_API_KEY`.
6. Deploy.

## API Reference

### `GET /health`

Checks service status.

Response:

```json
{
  "success": true,
  "status": "ok"
}
```

### `POST /chat`

Send a user message and optional conversation history.

Request body:

```json
{
  "message": "The app is crashing when I upload a file",
  "history": [
    { "role": "user", "content": "Hi" },
    { "role": "assistant", "content": "Hello!" }
  ]
}
```

Response:

```json
{
  "success": true,
  "reply": "Thanks for reporting this. We appreciate your feedback and will review it."
}
```

## Notes

- Ensure `GROQ_API_KEY` is set in Render environment settings.
- Python version is pinned to `3.12.8` via `render.yaml` (and `runtime.txt` as a secondary pin).
- The `/` route serves the web UI and calls `/chat` internally.
