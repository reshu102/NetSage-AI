# NetSage AI

NetSage AI is a compact MERN network-troubleshooting assistant for Cisco-style evidence. It combines deterministic checks, an AI/mock diagnosis, and required human review.

## Features
- Dark network-operations dashboard with MongoDB-backed metrics and charts
- Diagnose workflow with rule checks and mock AI (works without an API key)
- Human accept, edit, and reject review states
- Case search, filters, detail pages, and 30 seeded Packet Tracer-style scenarios

## Setup
```bash
npm install
npm run install-all
copy .env.example .env
npm run seed
npm run dev
```
Start MongoDB locally first. Open `http://localhost:5173`.

## AI configuration
`AI_MODE=mock` is the default demo mode. To use OpenAI set `AI_MODE=openai` and `OPENAI_API_KEY` in the root `.env`; the key is only read by the backend.

## Demo flow
Dashboard → Troubleshoot → Diagnose → AI Result + Rule Checks → Human Review → Cases.
