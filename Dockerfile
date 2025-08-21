# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01

FROM python:3.10-slim-bookworm

# Prevent interactive prompts during apt installs
ENV DEBIAN_FRONTEND=noninteractive

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    git \
    ffmpeg \
    wget \
    curl \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements first for caching
COPY requirements.txt /requirements.txt

# Install Python dependencies
RUN pip install --no-cache-dir -U pip setuptools wheel \
    && pip install --no-cache-dir -r /requirements.txt

# Create working directory
WORKDIR /VJ-FILTER-BOT

# Copy all files
COPY . /VJ-FILTER-BOT

# Run bot
CMD ["python", "bot.py"]
