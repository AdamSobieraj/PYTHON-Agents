FROM python:3.11-slim

# Ustawienie katalogu roboczego
WORKDIR /app

# Kopiowanie całego projektu
COPY . /app

# Aktualizacja pip i instalacja zależności
RUN pip install --upgrade pip && \
    pip install --no-cache-dir requests openai Faker

# Ustawienie PYTHONPATH, aby Python widział pakiety
ENV PYTHONPATH=/app

# Domyślna komenda uruchamiająca agenta
CMD ["python", "-m", "agent_confluence.main"]
