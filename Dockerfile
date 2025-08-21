# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01

# ❌ buster hatao
# FROM python:3.10.8-slim-buster
# ✅ latest supported image use karo
FROM python:3.10-slim-bookworm  

ENV DEBIAN_FRONTEND=noninteractive

# Install system deps
RUN apt-get update && apt-get install -y --no-install-recommends \
    git \
    ffmpeg \
    wget \
    curl \
    build-essential \
 && rm -rf /var/lib/apt/lists/*

# Copy requirements
COPY requirements.txt /requirements.txt

# Install Python deps
RUN pip install --no-cache-dir -U pip setuptools wheel \
 && pip install --no-cache-dir -r /requirements.txt

# Workdir
WORKDIR /VJ-FILTER-BOT

# Copy all files
COPY . /VJ-FILTER-BOT

# Run bot
CMD ["python", "bot.py"]
