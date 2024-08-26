1.-  Crear ambiente de Pyhton
2.- Instalar dependencia desde requirements.txt
3.- Ejecutar el ambiente local de AWS con Docker `docker-compose up -d`
4.- Configurar las variables de entorno en el .env
```
AWS_ACCESS_KEY_ID=test
AWS_SECRET_ACCESS_KEY=test
DEFAULT_REGION=us-east-1
DYNAMODB_TABLE_FUNDS=fundations
DYNAMODB_TABLE_TRANSACTIONS=transactions
FASTAPI_DEBUG=True
INITIAL_AMOUNT=500000.00
```
5.- Ejecutar el proyecto: `uvicorn app.main:app --reload --port 5000 --host 0.0.0.0`
