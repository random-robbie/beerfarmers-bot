FROM python:3.6-alpine
RUN apk add --no-cache git openssh-client bash
RUN python3 -m ensurepip
ADD . /
RUN pip3 install tweepy
RUN git config --global url."https://github.com/".insteadOf git@github.com:
RUN git config --global url."https://".insteadOf git://
ENTRYPOINT ["bash bot.sh"]
