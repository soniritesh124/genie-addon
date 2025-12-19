FROM python:3.11-slim

# Install jq (REQUIRED for Home Assistant add-on options)
RUN apt-get update && \
    apt-get install -y jq && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY app.py .
COPY run.sh .

RUN pip install flask requests
RUN chmod +x /app/run.sh

CMD ["/app/run.sh"]
