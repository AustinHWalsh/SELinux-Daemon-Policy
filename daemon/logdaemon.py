import time

count = 0
# Write a new message to the log/messages file every minute
while True:
    with open("/var/log/messages", "a") as logfile:
        logfile.write(f"A new log message from {__file__}: {count}\n")

    count += 1
    time.sleep(60)
