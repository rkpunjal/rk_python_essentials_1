# iterate through list items

emails = ["abc@email.com", "def@gmail.com", "ghi@gmail.com", "jkl@gmail.com", "mno@gmail.com", "pqr@gmail.com",
          "stu@gmail.com", "wxyz@gmail.com"]

for email in emails:
    print("sending mail to : ", email)

print()
print("using while and index")

email_index = 0
while email_index < len(emails):
    print("sending mail to : ", emails[email_index])
    email_index += 1

print()
print("----------------------------------------")

lando_2021_results = [4, 2, 5, 8, 3, 5, 5, 5, 3, 14, 10, 2, 7, 7, 8, 10, 10, 9, 10, 7]

print("lando_2021_results : ", lando_2021_results)


def average(nums):
    total = 0
    if nums == None:
        return 0

    for num in nums:
        total += num
    return total / len(nums)


print("average : ", average(lando_2021_results))


def lowest_value(nums):
    if (len(nums) > 0):
        lowest = nums[0]
    else:
        return None

    for num in nums:
        if num < lowest:
            lowest = num

    return lowest


print("lowest value : ", lowest_value(lando_2021_results))

