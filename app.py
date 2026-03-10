import os

def add(a, b):
    return a + b


# VULNERABLE FUNCTION
def ping(host):
    # Command injection vulnerability
    return os.system("ping -c 1 " + host)
