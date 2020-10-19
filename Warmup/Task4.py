"""
Read file into texts and calls.
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 4 Problem Statement:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

# brainstorm:
# I can identify numbers that have outgoing calls but no texts or 
# incoming calls

def combine(texts, calls):
    # this function aggregates a list of incoming calls and all text message numbers
    # if they are not duplicates.
    # input: texts data and calls data
    # output: aggregated list
    checklist = []
    for text in texts:
        if text[0] not in checklist:
            checklist.append(text[0])
        if text[1] not in checklist:
            checklist.append(text[1])
    for call in calls:
        if call[1] not in checklist:
            checklist.append(call[1])
    return checklist


def identify(outgoing, checklist):
    # this function compares the list of outgoing call numbers with the compiled
    # list of texts and incoming calls.
    # input: outgoing calls and a combined list of texts and incoming calls
    # output: potential marketing numbers
    marketing = []

    for call in outgoing:
        if call not in checklist:
            marketing.append(call)
    return marketing


'''
def test1():
    # this is a test to see if there are any identified marketing numbers in the list
    # that is not supposed to be marketing numbers.
    try: 
        identify() in text()
    except: 
        print("There is an error.")
    finally:
        print("The error check is finished.")
'''
# test dataset
test_outgoing = ['9817 2947', '2398 1209']
test_text = ['1935 2093', '1947 0295', '9817 2947']

test_incoming = ['1935 2093', '1947 0295', '2398 1209']
# test1: expected answer = ['2398 1209']
print(identify(test_outgoing, test_text))


# test2: expected answer = [], need a different test set
combined = combine(test_incoming, test_text)
print(identify(test_outgoing, combined))

