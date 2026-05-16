# Feedback Assistant (FastAPI + Groq)

A small feedback assistant API with a built-in web UI, deployable on Vercel.

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

## Deploy to Vercel

1. Push this project to GitHub.
2. In Vercel, click **Add New Project** and import the repo.
3. Framework preset: **Other**.
4. Add environment variable:
   - `GROQ_API_KEY`: your Groq API key
5. Deploy.

This repo includes:
- `vercel.json` for routing and Python build
- `api/index.py` as Vercel entrypoint

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

- Ensure `GROQ_API_KEY` is set in Vercel project settings.
- The `/` route serves the web UI and calls `/chat` internally.
