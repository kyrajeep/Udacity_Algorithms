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
TASK 4:
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
# I can identify numbers that have outgoing calls but no texts or incoming calls
# text data and call data are separate. Can I merge them together? Is there a better way?
# fix outgoing calls-> check if I can find them anywhere in the message data.
# save the list, and check with the receiving call data.
# question: how do I check the result?
def outgoing(calls):
# I think I need to loop through all the outgoing call list. is there a better way?
# Can I recycle the outgoing call list from previous tasks? If yes, how? I need to pass it in the parameter. Put on Git repo and ask a question. call_list1 to Task4.
# The function loops through the outgoing call list, check with the text list
    outgoing = []
    for call in calls:
        # this for loop creates a list of numbers making outgoing calls.
        if call[0] not in outgoing:
            outgoing.append(call[0])
    
    return outgoing
    
def text(texts, calls):
    # this function aggregates a list of incoming calls and all text message numbers
    # if they are not duplicates.
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

    
def identify(texts):
    # this function compares the list of outgoing call numbers with the compiled
    # list of texts and incoming calls.
    marketing = []
    outgoings = outgoing(calls)
    textnumber = text(texts, calls)
    for call in outgoings:
        if call not in textnumber:
            marketing.append(call)
    return marketing

def test1():
    # this is a test to see if there are any identified marketing numbers in the list
    # that is not supposed to be marketing numbers.
    try: 
        identify(texts) in text(texts, calls)
    except: 
        print("There is an error.")
    finally:
        print("The error check is finished.")

#test1()
print(identify(texts))
