FROM python:3.11

WORKDIR /code

# allow docker to cache installed dependencies
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

#Mounts app code to image
COPY . .

EXPOSE 8000


CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

# docker run -p 8000:8000 <tag name>