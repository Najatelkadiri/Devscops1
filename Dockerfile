FROM python:3.9-alpine

WORKDIR /app

RUN apk add --no-cache gcc musl-dev python3-dev

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY api/ .

RUN adduser -D myuser
USER myuser

EXPOSE 5000
CMD ["python", "app.py"]