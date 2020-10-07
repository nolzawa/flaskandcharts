import pymongo
from datetime import datetime, timedelta

# Configure MongoDB
connection = pymongo.MongoClient('mongodb://localhost:27017')
db = connection['TMA']

#collection : trolley

def get_high(objDate=None):
    filter = {}
    if objDate is not None:
        start=datetime(objDate.year, objDate.nmonth, objDate.day) #get the start of the date
        end=start+timedelta(days=1) # this get the ending
        filter['date'] = { #this filters only the time between start and end date will appear
            '$lt':end,
            '$gte':start
        }
    return db.trolley.find(filter).sort("temp",-1).limit(1)

def get_low(objDate=None):
    filter = {}
    if objDate is not None:
        start=datetime(objDate.year, objDate.nmonth, objDate.day) #get the start of the date
        end=start+timedelta(days=1) # this get the ending
        filter['date'] = { #this filters only the time between start and end date will appear
            '$lt':end,
            '$gte':start
        }
    return db.trolley.find(filter).sort("temp",+1).limit(1)

def f_date(objDate=None):
    filter = {}
    if objDate is not None:
        start=datetime(objDate.year, objDate.nmonth, objDate.day) #get the start of the date
        end=start+timedelta(days=1) # this get the ending
        filter['date'] = { #this filters only the time between start and end date will appear
            '$lt':end,
            '$gte':start
        }
    return db.trolley.find(filter)
    

def count_active(objDate=None):
    filter = {}
    if objDate is not None:
        start=datetime(objDate.year, objDate.nmonth, objDate.day) #get the start of the date
        end=start+timedelta(days=1) # this get the ending
        filter['date'] = { #this filters only the time between start and end date will appear
            '$lt':end,
            '$gte':start
        }
        results = db.trolley.distinct("name")
        r_len = len(results)
        return r_len

def count_all(): #gets all unique trolley names in the collection
    results = db.trolley.distinct("name")
    r_len = len(results)
    return r_len

def create_trolley(name, date, time, temp):
    assert name is not None
    assert date is not None
    assert time is not None
    assert temp is not None

    db.trolley.insert_one({'name':name, 'date': date, 'time': time, 'temp': temp})

def update_trolley(name, new_temp):
    assert name is not None
    assert new_temp is not None

    db.trolley.update_one({'name':name}, {'$set':{'temp':new_temp}})

def delete_trolley(name):
    assert name is not None

    db.trolley.delete_one({'name':name})

