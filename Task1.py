"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""
def combine(calls, texts):
    call_list1 = list()
    for call in calls:
        call_list1.append(call[0])
    call_list2 = list()
    for call in calls:
        call_list2.append(call[1])
    text_list1 = list()
    for text in texts:
        text_list1.append(text[0])
     
    text_list2 = list()
    for text in texts:
        text_list2.append(text[1])

    combined = call_list1 + call_list2 + text_list1 + text_list2
    return combined
def unique(combined):
     #converts combined into a set for uniqueness and converts it back into a list.
    combined_set = set(combined)
    combined_list = list(combined_set)
    return len(combined_list)
    
print("There are", unique(combine(calls, texts)), "different telephone numbers in the records")

