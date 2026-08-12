FROM --platform=$BUILDPLATFORM python:3.12 AS build

ARG TARGETPLATFORM
ARG BUILDPLATFORM

WORKDIR /app

COPY ./requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir --upgrade -r ./requirements.txt

EXPOSE 8000

COPY . .

COPY ./entrypoint.sh /app/entrypoint.sh
RUN chmod +x /app/entrypoint.sh
ENTRYPOINT ["/app/entrypoint.sh"]

CMD ["fastapi", "run", "src/main.py", "--port", "8000"]
