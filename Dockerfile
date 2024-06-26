FROM python:3.10-slim

WORKDIR /app

# Install dependecies
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

# Run the discord bot
CMD ["python", "main.py"]