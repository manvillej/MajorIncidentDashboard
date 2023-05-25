import json
import random

import pandas as pd
import numpy as np


Applications = []
OutageTypes = []
ITWorkers = []
Directors = []
Customers = []


def simulateArrivals(rates, sizes):
    '''with a rate of occurence and a number of events to generate, this creates an array of datetime arrivals '''
    return pd.Timestamp('today').normalize() - pd.to_timedelta(
        24*60*60*365*np.cumsum(
            np.concatenate([poissonArrivalSample(rate, size) for rate, size in zip(rates, sizes)])
        ), unit='s')

def poissonArrivalSample(rate, size):
    return np.random.exponential(1./rate, size=size)
    

def simulateDuration(rate, size):
    '''meant for simulating time spent to complete something, assignment, task completion, etc.'''
    pass

def getMajorIncidentTemplate():
    with open('./templates/majorIncident.json','r') as fp:
        majorIncidentTemplate = json.load(fp)
    return majorIncidentTemplate['records'][0]

def generateMajorIncident(index, createdDate="", short_description="", category="", assigned_to="", assignment_group=""):
    record = getMajorIncidentTemplate()
    # record[''] = ''
    record['impact'] = '1'
    record['urgency'] = '1'
    record['priority'] = '1'
    record['state'] = '6'
    record['major_incident_state'] = 'accepted'
    record['active'] = 'true'
    record['short_description'] = short_description
    record['category'] = category
    record['assigned_to'] = assigned_to
    record['resolved_by'] = resolved_by
    record['assignment_group'] = assignment_group
    record['business_impact'] = ''
    record['description'] = ''
    record['cause'] = ''
    record['close_code'] = 'Solved (Permanently)'
    record['caller_id'] = ''
    record['close_notes'] = ''
    record['contact_type'] = ''
    record['severity'] = ''
    record['sys_id'] = ''
    record['number'] = f'INC004{(numbersLength-(index)+1):04d}'
    record['business_duration']=''
    record['calendar_duration']=''
    record['resolved_at']=''
    record['closed_at']=''
    record['sys_updated_on'] = ''
    record['sys_created_on'] = createdDate
    record['opened_at'] = createdDate
    business_duration
    return record

def generateRandomParameterList(choices, size):
    #mylist = ["geeks", "for", "python"]
    #print(random.choices(mylist, weights = [10, 1, 1], k = 5))
    return random.choices(choices, k=size)


# DONE - get a json incident as template

# parameterize fields: application, category, assigned to, opened by, etc
# generate description using chatgpt? https://www.geeksforgeeks.org/how-to-use-chatgpt-api-in-python/
# generate short descroption using chatgpt?
# generate closed notes using chatgpt
# simulate assigned time
# simulate closure time


# on initialization of class, generate sample data as json files
# on query, just return json files