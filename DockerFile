#Docker File of the Web Scraper
FROM python:latest
RUN export DOCKER_BUILDKIT=0export DOCKER_BUILDKIT=0
RUN export COMPOSE_DOCKER_CLI_BUILD=0

RUN  apt-get update \
  && apt-get install -y wget \
  && rm -rf /var/lib/apt/lists/*

COPY . . 

RUN apt-get update
RUN apt-get install -y gnupg2

RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -
RUN sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list'
RUN apt-get -y update
RUN apt-get install -y google-chrome-stable
RUN apt-get update
RUN echo "deb http://archive.ubuntu.com/ubuntu focal-updates main restricted universe multiverse" | tee -a /etc/apt/sources.list

RUN apt-get -y install software-properties-common
RUN apt -y install curl
RUN wget -O /tmp/chromedriver.zip http://chromedriver.storage.googleapis.com/`curl -sS chromedriver.storage.googleapis.com/LATEST_RELEASE`/chromedriver_linux64.zip
RUN apt-get install -yqq unzip
RUN unzip /tmp/chromedriver.zip chromedriver -d /usr/local/bin/

USER root
RUN python -m pip install selenium

RUN pip install --upgrade pip

RUN python -m pip install -r requirements.txt

CMD ["python", "Web_Scraper.py"]


