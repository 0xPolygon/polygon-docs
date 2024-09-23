FROM python:3.12-alpine

RUN apk update
RUN apk add rsync
RUN apk add git
RUN apk add nodejs npm
RUN apk add --no-cache bash
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt --no-cache-dir

# Build doc by default
ENTRYPOINT ["mkdocs"]
CMD ["serve", "--dev-addr", "0.0.0.0:8000"]
