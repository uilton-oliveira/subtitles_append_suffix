FROM python:3-alpine

# Setup env
ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONFAULTHANDLER 1

WORKDIR /renamer

COPY . .

EXPOSE 8000
ENTRYPOINT ["python", "main.py"]