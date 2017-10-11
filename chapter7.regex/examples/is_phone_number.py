# function to check whether a string matches the pattern, returning either True or False.
# example: 076-789 60 10

def isPhoneNumber(text):
  if len(text) != 13:
     return False
  for i in range(0, 3):
    if not text[i].isdecimal():
      return False
  if text[3] != '-':
    return False
  for i in range(4, 7):
    if not text[i].isdecimal():
      return False
  if text[7] and text[10] != ' ':
    return False
  for i in range(8, 10):
    if not text[i].isdecimal():
      return False
  for i in range(11, len(text)):
    if not text[i].isdecimal():
      return False
  return True

message = 'Call me at 076-789 60 10 tomorrow. 076-789 70 94 is my office.'
for i in range(len(message)):
  chunk = message[i:i+13]
  if isPhoneNumber(chunk):
    print('Phone number found: ' + chunk)
print('Done')