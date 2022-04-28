from celery import shared_task
import os
# import oracle pro
# import sys
# sys.path.append("C:\Users\Administrator\Desktop\python\cx_oracle\pro")
# import main
from .main import db_conn

@shared_task
def oracle_conn(json):

    data = db_conn(json.lat , json.lon).conn()

    return data


@shared_task
def post_conn(lat , lon):
    pass