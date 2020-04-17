"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone. 

Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""
# I want to identify the longest time 
# then match it with that call in a for loop.
def combine(calls):
# gets all the call duration into a list so that I can find the max
    duration = []
    for call in calls:
        duration.append(int(call[3]))
    return max(duration)


def identify(calls):
# Purpose of the function: I can identify the index of the call that spent 
# the longest time. 
   
    for i in range(len(calls)):
        if int(calls[i][3]) == 4617:
            return calls[i]
    
print(identify(calls)[0],"spent the longest time", identify(calls)[3], "seconds, on the phone during September 2016.")