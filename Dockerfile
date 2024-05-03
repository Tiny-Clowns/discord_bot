FROM python:3.10-slim

WORKDIR /app

# Install discord.py pip
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

# Run the discord bot
CMD ["python", "main.py"]