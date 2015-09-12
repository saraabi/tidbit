import datetime
import decimal
import random
import string
import re

def uid_generator(size=5,chars=string.ascii_uppercase + string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))

def get_uid(obj):
    uid = uid_generator()
    while uid == obj.__class__.objects.filter(uid=obj.uid):
        uid = uid_generator()
    return uid
