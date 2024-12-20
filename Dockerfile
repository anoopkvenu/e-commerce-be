FROM python:3.8

WORKDIR /dist

COPY ./app/requirement.txt /dist/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /dist/requirements.txt

COPY . /dist

ENV PYTHONPATH="${PYTHONPATH}:/dist/app"

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]