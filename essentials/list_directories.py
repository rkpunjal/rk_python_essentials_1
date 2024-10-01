from functools import reduce


time_string = "1:05:22"
time_string = "05:22"

# _times = ['MM:SS', 'HH:MM:SS', 'SS']
# seconds = [sum(int(x) * 60 ** i for i, x in enumerate(reversed(_time.split(':')))) for _time in _times]

seconds =  reduce(lambda prev, next: prev * 60 + next, [float(x) for x in time_string.split(":")], 0)
seconds = int(seconds)

print("time_string : ", time_string)
print("seconds : ", seconds)


