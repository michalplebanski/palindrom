def check_palindrom(name):
  name = name.replace(" ", "")
  reverse_name = name.isalnum()
  return reverse_name

status = check_palindrom("łapał")
print(status)
