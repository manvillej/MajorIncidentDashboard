import pandas as pd
import numpy as np

def simulateArrivals(rate, size):
    '''with a rate of occurence and a number of events to generate, this creates an array of datetime arrivals '''
    return pd.Timestamp('today').normalize() - pd.to_timedelta(
        24*60*60*365*np.cumsum(
            np.random.exponential(1./rate, size=size)
        ), unit='s')

# DONE - get a json major incident as template
# DONE - get a json incident as template

# parameterize fields: application, category, assigned to, opened by, etc
# generate description using chatgpt? https://www.geeksforgeeks.org/how-to-use-chatgpt-api-in-python/
# generate short descroption using chatgpt?
# generate closed notes using chatgpt
# simulate assigned time
# simulate closure time


# on initialization of class, generate sample data as json files
# on query, just return json files