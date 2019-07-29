"""
Input is saved into a list of observations (obs)
month, day, hour and minute denote their respective times of the observations
status is set to one of three values:
    If a guard starts their shift, their ID number is saved
    If a guard wakes up, it is set as 0
    If a guard is asleep, it is set as 1
This information is stored as a single sting in obs
Once all input has been read into obs, it is sorted so that all observations about a single shift are together
"""
obs = []
raw = open("day4_input.txt","r")
for line in raw:
    month = line[6:8]
    day = line[9:11]
    hour = line[12:14]
    minute = line[15:17]
    if line[19] =="G":
        status = line[line.find("#"):line.find("b")-1]
    elif line[19] == "w":
        status = 0
    elif line[19] == "f":
        status = 1
    observation = month + day + hour + minute + str(status)
    obs.append(observation)
raw.close()
obs.sort()

"""
Obsevations of the same watch are joined together into a single list (watch)
Each entry in watch denotes one minute, and is set to either 0 (awake) or 1 (asleep)
The final entry in a list gives the ID number of the guard
watches is a list to store each individual watch
index gives the index for watches. It is set to -1 so it is properly set to 0 on the initial pass
For each individual observation in obs:
    if the status is the ID number of a guard, this indicates a new watch has begun, and so a new watch is created. The guard is initially assumed to be awake (0) for the whole shift
    if the status is aleep or awake, the guard is presumed to remain in that state for the remaineder of the shift. From the minute given in obs, all remaining minutes in a watch
    are set to the appropriate value, 0 for awake and 1 for asleep
"""

watches = []
index = -1
for ob in obs:
    if ob[8] == "#":
        index += 1
        watch = [0]*61
        watch[60] = ob[ob.find("#")+1:]
        watches.insert(index,watch)
    if ob[8] == "0":
        start = int(ob[6:8])
        while start < 60:
            watches[index][start] = 0
            start += 1
    if ob[8] == "1":
        start = int(ob[6:8])
        while start < 60:
            watches[index][start] = 1
            start += 1

#By going through watches, a list containing all the individual ID numbers of the guards is generated
ID_list = []
for watch in watches:
    if watch[60] not in ID_list:
        ID_list.append(watch[60])

"""
Find which guard spends the most time asleep
For each guard, find watches they were on.
Then sum up all the minutes in a watch (this is why awake was set to 0 and asleep to 1) to give the amount of time asleep
Each guards ID and total time asleep is save in the list sleep
sleep is then passed through to find the guard with the highest number of minutes asleep
"""
sleep = []
for ID in ID_list:
    asleep = 0
    for watch in watches:
        if ID == watch[60]:
            i = 0
            while i < 60:
                asleep += watch[i]
                i += 1
    snooze = [asleep,ID]
    sleep.append(snooze)
sleep_max = 0
sleep_max_id = 0
for snooze in sleep:
    if snooze[0] > sleep_max:
        sleep_max = snooze[0]
        sleep_max_id = snooze[1]

"""
Find which minute the previously identified guard is most frequently asleep
Set up a list covering each minute in an hour, all initialised to 0
Iterating over the watches the guard performed, each in the frequency list adds on the value from the watch list
Then the maximum value in the list is found and stored, as is the corresponding minute of the hour
The minute of most frequent sleep is multiplied by the guard's ID and output
"""
sleep_freq = [0]*60
for watch in watches:
    if watch[60] == sleep_max_id:
        i = 0
        while i < 60:
            sleep_freq[i] += watch[i]
            i += 1

sleep_max = max(sleep_freq)
sleep_max_time = sleep_freq.index(sleep_max)
answer1 = int(sleep_max_id)*int(sleep_max_time)
print("Part 1 answer: " + str(answer1))

#As the second part of the task is likely to identify a differnet guard, appropriate values are reset to 0. sleep_max_time stoes the specific minute a guard is most frequently asleep
sleep_max = 0
sleep_max_time = 0
sleep_max_ID = 0

"""
Find the guard who is asleep the most often for a specific minute
This uses the same method for determining sleep frequency as above, but now applied to every guard
After a given guards most frequent minute spent asleep is found, it is compared to the highest value (sleep_max, initially 0)
If it beats sleep_max, it is stored along with the specific minute and guard's ID.
Once all guards are checked, the minute of most frequent sleep is multiplied with the respective guard's ID and output
"""
for ID in ID_list:
    sleep_freq = [0]*60
    for watch in watches:
        if watch[60] == ID:
            i = 0
            while i < 60:
                sleep_freq[i] += watch[i]
                i += 1
    high_freq = max(sleep_freq)
    high_freq_time = sleep_freq.index(high_freq)
    if high_freq > sleep_max:
        sleep_max = high_freq
        sleep_max_time = high_freq_time
        sleep_max_ID = ID
answer2 = int(sleep_max_time)*int(sleep_max_ID)
print("Part 2 answer: " + str(answer2))
