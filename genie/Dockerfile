FROM python:3.11-slim

WORKDIR /app
COPY app.py .
COPY run.sh .

RUN pip install flask requests
RUN chmod +x run.sh

CMD ["/app/run.sh"]