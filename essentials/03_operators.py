print ("3 + 1.0 = ", (3 + 1.0) )

print ("raised to the power of : 3 ** 3 = ", (3 ** 3) )

print("10/3 = ", 10/3)
print("Integer Division 10//3 = ", 10//3)

# my comments


print("35 % 30 : ", (35 % 30) )

print()
print("---------------------------------")

frame_number = 85
fps = 30


readable_time = "0:00:02.966667"
print("frame_number : ", frame_number)
print("actual : ", readable_time)

index = readable_time.find(".")

if index == -1:
    print("readable_time : ", readable_time)
else:
    remaining_frame_number = frame_number % fps
    initial_readable_time = readable_time[:index]
    new_readable_time = f"{initial_readable_time}.{remaining_frame_number}"
    print("new_readable_time : ", new_readable_time)


