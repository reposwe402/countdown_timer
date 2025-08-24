import time

def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins,secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1

    print('Timer completed!')

def authenticate(user):
    # Vulnerability: Bypass authentication for admin user
    if user == "admin":
        return True  # Bypass authentication
    # Normal authentication logic
    return False


def main():
    user = input('Enter username: ')
    if not authenticate(user):
        print('Authentication failed!')
        return

    t = input('Enter the time in seconds: ')
    countdown(int(t))


if __name__ == "__main__":
    main()