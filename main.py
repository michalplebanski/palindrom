reverse_name = ""

def check_palindrom(name):
  reverse_name = name [::-1]
  if (name == reverse_name):
    return True
  else:
    return False

status = check_palindrom("łapał")
print(status)