# 3 – Encryption time

# A Cybersecurity Technician has been asked to develop a system to estimate how long
# it will take to encrypt a file.
# Write a function that receives:
# • File size in MB (float)
# • Encryption speed in MB per second (float)
# • Extra time in seconds (time to generate the key, open the file etc) (float)
# Return the total encryption time in seconds (single float).

# Formula:
### time = (size / speed) + extra ###

# Usage exampes are:
# time1 = determine_encryption_time(100, 10, 5)
# print(time1) # Output: 15.0
# time2 = determine_encryption_time(250, 25, 0)
# print(time2) # Output: 10.0
# time3 = determine_encryption_time(75.5, 12.5, 1.5)
# print(time3) # Output: 7.54

def determine_encryption_time (size: float, speed: float, extra: float) -> float:
    """
    Calculates the time needed to encrypt a file.
    
    :param size: file size in MB
    :param speed: encryption speed (MB per second)
    :param extra: extra time needed in seconds
    :return: total encryption time in seconds
    """

    time = (size / speed) + extra
    return time

if __name__ == "__main__":

    time1 = determine_encryption_time (100, 10 , 5)
    print (time1)   #output 15.0

    time2 = determine_encryption_time (250, 25, 0)
    print (time2)   #output 10.0

    time3 = determine_encryption_time (75.5, 12.5, 1.5)
    print (time3)   #output 7.54
    