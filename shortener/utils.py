import random
import string


def get_random_string(length) -> str:
    symbols = string.ascii_letters + string.digits
    return "".join(random.choice(symbols) for i in range(length))
