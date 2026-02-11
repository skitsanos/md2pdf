# Use a modern Python runtime compatible with project requirements (>=3.10)
FROM python:3.13-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1

# Set working directory
WORKDIR /app

# Install system dependencies required for WeasyPrint
RUN apt-get update && apt-get install -y --no-install-recommends \
    libcairo2 \
    libpango-1.0-0 \
    libpangocairo-1.0-0 \
    libgdk-pixbuf-2.0-0 \
    libffi8 \
    fonts-dejavu-core \
    shared-mime-info \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements first to leverage Docker cache
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy only package files needed for installation
COPY setup.py README.md ./
COPY md2pdf ./md2pdf

# Install the package
RUN pip install --no-deps .

# Create non-root runtime user and writable docs directory
RUN groupadd --system app && useradd --system --gid app --create-home app \
    && mkdir -p /docs \
    && chown -R app:app /app /docs

# Set the working directory to /docs for file operations
WORKDIR /docs
USER app

# Set the entrypoint to md2pdf command
ENTRYPOINT ["md2pdf"]

# Default command shows help
CMD ["--help"]
