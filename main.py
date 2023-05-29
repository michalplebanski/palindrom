def check_palindrom(name):
  if name.isalnum():
    name = name.lower().replace(" ", "")
    return name == name[::-1]  
  
status = check_palindrom("łapał")
print(status)
