import pandas as pd
import numpy as np
import re


file = open("AOTC2018_4.txt")

data = [x.strip() for x in file]
data = sorted(data)

columns_ = ["date","id"] + [str(x) for x in range(0,60)]

schedule = pd.DataFrame(0, index=np.arange(len(data)+1), columns=columns_)
# print(schedule)

find_date = re.compile("\d\d-\d\d\s")
find_time = re.compile(":\d\d")
find_ID	  = re.compile("#\d*")

guard_id = ""
sleep_time = 0
wake_time = 0
counter = -1

for i in range(len(data)):
# for i in range(15):
	m_date = re.search(find_date, data[i])
	m_time = re.search(find_time, data[i])
	m_ID   = re.search(find_ID  , data[i])

	
	# if m_date:
	# 	print(m_date.group(0))

	if m_ID:
		# print(m_ID.group(0))
		guard_id = m_ID.group(0)

		# if guard_id == "#73":
		# 	print(data[i])
	else:
		if "falls" in data[i]:
			sleep_time = int(m_time.group(0).replace(":",""))
		elif "wakes" in data[i]:
			wake_time = int(m_time.group(0).replace(":",""))

	if sleep_time != 0 and wake_time != 0:

		schedule.loc[counter,'date'] = m_date.group(0)
		schedule.loc[counter,'id'] = guard_id
		schedule.loc[counter,str(sleep_time):str(wake_time-1)] += 1

		# if guard_id == "#73":
		# 	print(guard_id,": ",sleep_time,"-",wake_time)


		sleep_time = 0
		wake_time = 0

	if "Guard" in data[i]:
		# print("HERE IT IS")
		sleep_time = 0
		wake_time = 0
		counter += 1

# print(schedule)

# print(schedule.groupby("id").sum().sum(axis=1))
# print(schedule.groupby("id").sum().max(axis=1))
# print(schedule.groupby("id").sum().max(axis=0))
print(schedule.groupby("id").sum().loc["#73":"#79","40":"47"])


# print(schedule.loc[schedule["id"]=="#191", ["date","24","25","26","27","28"]])
# print(schedule.iloc[:5,5:25])

print(73*44)  # part 1
print(191*26) # part 2












