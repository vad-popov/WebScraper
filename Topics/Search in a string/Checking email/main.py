import re
def check_email(string):
    return bool(re.search(r'.+@.+\..+', string) and ' ' not in string)
