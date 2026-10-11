# These build instructions are supplied by IBM Lab 3 (PDF p. 8).
FROM python:3.10
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip3 install --no-cache-dir -r requirements.txt
COPY . .
CMD ["python", "demo.py"]
