import time
timestamp = time.strftime('%H:%M:%S')
print(timestamp)
def greet():
    current_hour = int(time.strftime('%H'))

    if 5 <= current_hour < 12:
        print("Good Morning!")
    elif 12 <= current_hour < 18:
        print("Good Afternoon!")
    else:
        print("Good Evening!")
if __name__ == "__main__":
    greet()