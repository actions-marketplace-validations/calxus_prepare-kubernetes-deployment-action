FROM gtadam89/python

MAINTAINER gtadam@protonmail.ch

COPY entrypoint.sh /entrypoint.sh
COPY requirements.txt /requirements.txt
COPY prepare.py /prepare.py
COPY service/ /service

ENTRYPOINT ["/entrypoint.sh"]