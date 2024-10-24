FROM python:3.12-alpine
LABEL authors="sorena"

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    APP_HOME=/app \
    REQUIREMENTS_FILE=requirements/prod.txt

WORKDIR ${APP_HOME}

COPY requirements/ requirements/
COPY requirements.txt requirements_dev.txt ./

RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r ${REQUIREMENTS_FILE}

COPY . ${APP_HOME}


EXPOSE 8000

CMD python manage.py migrate && python manage.py runserver 0.0.0.0:8000
