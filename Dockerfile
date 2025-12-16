FROM python:3.10-slim

WORKDIR /app

# Build-time configurable pip settings
ARG PIP_INDEX_URL=https://pypi.org/simple
ARG PIP_EXTRA_INDEX_URL
ARG PIP_TIMEOUT=300
ARG PIP_RETRIES=10

# Basic pip env tuning
ENV PIP_DISABLE_PIP_VERSION_CHECK=1 \
		PIP_DEFAULT_TIMEOUT=${PIP_TIMEOUT} \
		PYTHONDONTWRITEBYTECODE=1 \
		PYTHONUNBUFFERED=1

# System build deps for native wheels (gcc, zlib, etc.)
RUN apt-get update && apt-get install -y --no-install-recommends \
			build-essential \
			gcc \
			pkg-config \
			libz-dev \
			libjpeg-dev \
			libpng-dev \
		&& rm -rf /var/lib/apt/lists/*

# Upgrade pip and helpers for better resolver and wheels
RUN python -m pip install --upgrade pip setuptools wheel

# Install dependencies
COPY requirements_docker.txt .
RUN pip install --no-cache-dir --retries ${PIP_RETRIES} --default-timeout ${PIP_TIMEOUT} \
			-i ${PIP_INDEX_URL} $( [ -n "${PIP_EXTRA_INDEX_URL}" ] && printf -- "--extra-index-url %s" "${PIP_EXTRA_INDEX_URL}" ) \
			-r requirements_docker.txt \
		|| pip install --no-cache-dir --retries ${PIP_RETRIES} --default-timeout ${PIP_TIMEOUT} \
			-i https://pypi.tuna.tsinghua.edu.cn/simple \
			-r requirements_docker.txt

# Copy project files
COPY . .

# Create output directory
RUN mkdir -p output

# Run the main script
CMD ["python", "main.py"]
