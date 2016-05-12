import random
import string

s = string.ascii_letters + string.digits

def header_active(page, current_page):
    if page == current_page:
        return "active"
    return ""

def random_string(length):
    return "".join([ random.choice(s) for i in range(length)])
