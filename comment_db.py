from replit import db
import uuid

def clear():
  db['comments']={}

def init():
  if 'comments' not in db or db['comments']==[]:
    db['comments']={}

def add(comment):
    init()
    db['comments'][str(uuid.uuid4())]=comment


def get(search_query=None):
    init()
    results = []
    for id, comment in db['comments'].items():
        if search_query is None or search_query in comment:
            results.append(comment)
    return results
