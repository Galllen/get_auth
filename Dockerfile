FROM python:3.11-slim

RUN apt-get update && apt-get install -y \
    chromium chromium-driver \
    ca-certificates \
    fonts-liberation \
    libnss3 libatk-bridge2.0-0 libgtk-3-0 \
    libgbm1 libasound2 \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
RUN mkdir -p /app/session

CMD ["python", "-m", "bot.main"]
