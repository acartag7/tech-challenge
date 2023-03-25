# Build stage
FROM python:3.11.2-slim-bullseye

ARG FLASK_APP=encoder.py

LABEL \
    org.opencontainers.image.authors="Arnold Cartagena - cartagena.arnold@gmail.com" \
    org.opencontainers.image.title="Tech Challenge Character Encoder" \
    org.opencontainers.image.description="Docker container to run the tech challenge character encoder"

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir --trusted-host pypi.python.org -r requirements.txt

COPY ${FLASK_APP} .

# Set the environment variables for Flask
ENV FLASK_APP=${FLASK_APP}
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_RUN_PORT=80

# Expose port 80 for the Flask application
EXPOSE 80

# Use a non-root user
RUN addgroup --gid 1000 appuser && adduser --uid 1000 --gid 1000 --disabled-password --gecos "" appuser
USER appuser

# Run the Flask application when the container launches
CMD ["flask", "run"]

# Health check the app responds ok and 200 status code when called at /status
HEALTHCHECK --interval=5s --timeout=3s --start-period=10s --retries=3 CMD curl -f http://localhost/status || exit 1
