filnavn = ["data0.txt", "data1.txt", "data2.txt"]
data = []
for fil in filnavn:
    with open(fil, 'r') as file:
        data.append(file.read())

print("Størrelsen på inndata:")
for x in data:
    print(len(x))

# # Oppgave 1

import re

d = data[1].replace('Time:', '').replace('Distance:', '')
d = re.sub(' +', ' ', d).split("\n")
d = [x.strip().split(" ") for x in d]
d = [[int(y) for y in x] for x in d]

time, dist = d[0], d[1]


# ## Mellomregning

def run_strat(hold_time, run_time, run_dist):
    if hold_time == 0 or hold_time >= run_time:
        return 0
    
    time_spent = hold_time
    time_rem = run_time - hold_time
    speed = hold_time
    
    tot_dist = time_rem * speed
    return tot_dist


number_of_ways_to_beat_record = []
for run_i in range(len(time)):
    count = 0
    for hold_time in range(1, time[run_i]):
        if run_strat(hold_time, time[run_i], dist[run_i]) > dist[run_i]:
            count += 1
    number_of_ways_to_beat_record.append(count)


# ## Løsning

def multiplyList(myList):
    result = 1
    for x in myList:
        result = result * x
    return result


multiplyList(number_of_ways_to_beat_record)

# # Oppgave 2

import re

d = data[1].replace('Time:', '').replace('Distance:', '')
d = re.sub(' +', '', d).split("\n")
d = [int(x) for x in d]

# ## Mellomregning

count = 0
for i in range(d[0]):
    if run_strat(i, d[0], d[1]) > d[1]:
        count += 1

# ## Løsning

count
