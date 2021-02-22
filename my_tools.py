import random as rnd
import string


def rand_string(min_len,max_len):
    return ''.join(rnd.choice(string.ascii_lowercase) for i in range(rnd.randint(min_len,max_len)))