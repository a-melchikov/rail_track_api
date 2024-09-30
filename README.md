Для подключения к базе данных:

```bash
docker-compose up -d
```

```bash
psql -h 127.0.0.1 -p 5433 -U admin -d station_db
```

Для запуска фронтенда:

```bash
cd frontend/
npm start
```

Для запуска бекенда:

```bash
poetry run python main.py
```
