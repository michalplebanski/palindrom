reverse_name = ""

def check_palindrom(name):
  reverse_name = name [::-1]
  return name == reverse_name

status = check_palindrom("łapał")
print(status)
