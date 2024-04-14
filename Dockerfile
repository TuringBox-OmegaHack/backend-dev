FROM python:3.12.1-alpine

ENV HOME /home/app

RUN export LC_ALL=es_ES.UTF-8

WORKDIR ${HOME}
ENV PATH $HOME/.local/bin:$PATH

ADD requirements.txt ${HOME}/requirements.txt

RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt