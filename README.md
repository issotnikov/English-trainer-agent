# English Trainer AI

AI-платформа для изучения английского языка с персональным обучением и адаптивным Skill Graph.

## Цель

Помочь пользователям перейти с уровня A1/A2 до уровня C1 через:

- Персональные уроки
- AI Tutor
- Skill Graph
- Vocabulary Trainer
- Progress Analytics

## MVP Scope

### Входит

- Assessment Engine
- Tutor Engine
- Skill Graph
- Vocabulary Trainer
- Progress Dashboard

### Не входит

- Voice
- Mobile App
- IELTS
- TOEFL
- Multiplayer
- Marketplace

## Архитектура

Frontend:

- Next.js
- TypeScript

Backend:

- FastAPI
- PostgreSQL
- Redis

AI:

- OpenAI API

## Запуск проекта

```bash
docker compose up --build
```

## Документация

- docs/PRD_v1.md
- docs/SKILL_GRAPH_SPEC.md
- docs/AI_TUTOR_SPEC.md
- docs/BACKEND_TECH_SPEC.md

## MVP Roadmap

Sprint 1 – Infrastructure

Sprint 2 – Skill Graph

Sprint 3 – Assessment

Sprint 4 – Tutor

Sprint 5 – Vocabulary

Sprint 6 – Progress
