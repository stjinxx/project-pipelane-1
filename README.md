# DE E-commerce Pipeline

End-to-end data engineering pipeline untuk analytics e-commerce (Olist dataset).

## Stack
- PostgreSQL 16
- Metabase
- Docker Compose
- (coming) Python, dbt, Airflow

## Prerequisites
- Docker Desktop / Docker Engine + Compose plugin
- Git

## How to run
1. `cp .env.example .env` lalu isi password
2. `make up`
3. Buka Metabase: http://localhost:3000
4. Postgres: `localhost:5432`

## Project structure
...

## Roadmap
- [x] Week 1 Day 1: Docker Compose + Postgres + Metabase
- [ ] Week 1 Day 3: Download Olist dataset
- [ ] Week 1 Day 4-5: Python ingestion
- [ ] Week 2: dbt transformation
- [ ] Week 3: Airflow orchestration
- [ ] Week 4: Data quality + CI
- [ ] Week 5: Dashboard + monitoring
- [ ] Week 6: Polish