
FROM python:3.9-slim

WORKDIR /STREAMLIT

RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    software-properties-common \
    git \
    && rm -rf /var/lib/apt/lists/*


COPY . /STREAMLIT

RUN git clone https://github.com/HectorNuneztl/STREAMLIT.git .

RUN pip freeze > requirements.txt

RUN pip3 install -r requirements.txt

EXPOSE 8501

HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health

ENTRYPOINT ["streamlit", "run", "app3.py", "--server.port=8501", "--server.address=0.0.0.0"]