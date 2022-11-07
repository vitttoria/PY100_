import random
import string

a = string.ascii_uppercase + string.ascii_lowercase + string.digits


def get_random_password(fun) -> str:
    random.sample(fun, 8)
    return ''.join(random.sample(fun, 8))


print(get_random_password(a))
