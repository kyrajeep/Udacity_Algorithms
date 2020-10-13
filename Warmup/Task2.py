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


def combine(calls):

# input: calls data
#output: phone number with the longest time (receiving + calling).
    duration = {}
    for call in calls:
        number = 0
        duration = calc_dur(call, number, duration)
        number = 1
        duration = calc_dur(call, number, duration)   
    result_key = max(duration, key = lambda x: duration[x])
    result_value = duration[result_key]
    return result_key, result_value

def calc_dur(call, number, duration):
    # a helper function to calculate duration and add
    # the key and increment value in the dictionary.
    if call[number] not in duration.keys():
        duration[call[number]] = int(call[3])
    elif call[number] in duration.keys():
        duration[call[number]] += int(call[3])
    return duration    
print(combine(calls)[0],"spent the longest time", combine(calls)[1], "seconds, on the phone during September 2016.")