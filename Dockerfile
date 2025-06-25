# Base Python
FROM python:3.11-slim

# Diretório de trabalho
WORKDIR /app

# Copia requirements.txt
COPY requirements.txt .

# Instala dependências
RUN pip install --no-cache-dir -r requirements.txt

# Copia arquivos
COPY ./app /app/app

# Expondo porta
EXPOSE 8000

# Comando de inicialização
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
