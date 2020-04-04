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


from collections import defaultdict
phone_time = defaultdict(int)

for call in calls:
    phone_time[call[0]] += int(call[3])
    phone_time[call[1]] += int(call[3])

longest_time = 0
longest_phone_number = 0

for k, v in phone_time.items():
    if v > longest_time:
        longest_time = v
        longest_phone_number = k

print(f'{longest_phone_number} spent the longest time, {longest_time} seconds, on the phone during September 2016.')

# Using dict
# phone_time = dict()
# if phone_time.get(call[0], 0) == 0:
#     phone_time[call[0]] = int(call[3])
# else:
#     phone_time[call[0]] += int(call[3])

# if phone_time.get(call[1], 0) == 0:
#     phone_time[call[1]] = int(call[3])
# else:
#     phone_time[call[1]] += int(call[3])