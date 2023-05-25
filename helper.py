import os
import threading
import datetime

file_name = "Topology - Route Discovery - 2 - Route Status.mp4"
vid_h = 2
vid_m = 8
vid_sec = 11

tot_duration = datetime.datetime(year=2022, month=2, day= 2, hour=vid_h, minute=vid_m, second=vid_sec)
current_time = datetime.datetime(year=2022, month=2, day= 2, hour=0, minute=0, second=0)
origin_time = datetime.datetime(year=2022, month=2, day= 2, hour=0, minute=0, second=0)

threads = []
cntr = 1
while tot_duration - current_time > datetime.timedelta(minutes=10):
    print(current_time - origin_time, ",", datetime.timedelta(minutes=10))
    threads.append(threading.Thread(target=os.system, args=(f'ffmpeg -i "{file_name}" -ss {current_time - origin_time} -t {datetime.timedelta(minutes=10)} "{cntr}.mp4"',)))
    current_time += datetime.timedelta(minutes=10)
    cntr += 1
print(current_time - origin_time, ",", tot_duration - current_time)
threads.append(threading.Thread(target=os.system, args=(f'ffmpeg -i "{file_name}" -ss {current_time - origin_time} -t {tot_duration - current_time} "{cntr}.mp4"',)))

for thread in threads:
    thread.start()

for thread in threads:
    thread.join()

# cmd = 'ffmpeg -i "Topology - Route Discovery - 1 - Get Services.mp4" -ss 00:00:00 -t 00:10:00 "1.mp4"'
# os.system(cmd)