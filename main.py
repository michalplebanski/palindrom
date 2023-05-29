def check_palindrom(text):
  chars = [x for x in text.lower() if x.isalnum()]
  return chars == chars[::-1]

texts = ["ała", "łapał", "Ikar łapał raki!"]

for text in texts:
  status = check_palindrom(text)
  print(status)
