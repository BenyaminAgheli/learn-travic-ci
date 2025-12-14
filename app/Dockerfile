FROM python:3.10-slim

WORKDIR /app

RUN apt-get update\
	&& apt-get install -y --no-install-recommends curl\
	&& rm -rf /var/lib/apt/lists/* /var/cache/apt/*

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

CMD ["python", "app.py"]
