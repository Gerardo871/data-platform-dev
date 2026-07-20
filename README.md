# data-platform-dev
End-to-end data platform with Medallion architecture (Bronze/Silver/Gold) using Airflow, Postgress and Adminer. 

## Docker

```bash
# Entrar a la carpeta docker para ejecutar los comandos
cd docker

# Build and run
docker compose up -d

# Stop and remove
docker compose down
```

## ETL

```bash
#PD04647PDTC Euro (S/ por Euro) — Compra
#PD04648PDTC Euro (S/ por Euro) — Venta
# Ejecutar el ETL
python etl/pipeline.py --start_date 2025-02-01 --end_date 2025-07-19 --serie_id PD04647PD
```