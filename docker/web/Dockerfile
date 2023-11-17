FROM python:latest


COPY run.py run.py


RUN pip install fastapi
RUN pip install uvicorn


ENTRYPOINT [ "python","run.py" ]