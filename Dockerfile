# Don't Remove Credit @TamilBots
# Subscribe YouTube Channel For Amazing Bot @TamilBots
# Ask Doubt on telegram @TamilSupport
#Join our Movie channel @TownBus

FROM python:3.10.8-slim-buster

RUN apt update && apt upgrade -y
RUN apt install git -y
COPY requirements.txt /requirements.txt

RUN cd /
RUN pip3 install -U pip && pip3 install -U -r requirements.txt
RUN mkdir /TAMIL-FILTER-BOT
WORKDIR /TAMIL-FILTER-BOT
COPY . /TAMIL-FILTER-BOT
CMD ["python", "bot.py"]
