from mongoengine import *
from datetime import datetime


class Pages(Document):
    title = StringField(max_length=200, require=True)
    date_modified = DateTimeField(default=datetime.utcnow)