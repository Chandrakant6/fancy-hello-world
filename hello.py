import time

def hello(s = 'hello world'):
  for i in range(len(s)):
	  specialChar = '''!@#$%^&*(),./<>?;':"[]{}\|-_=+'''
      l = '1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ ' + specialChar
      for j in l:
          print(s[:i] + j)
          time.sleep(.1) # seconds
          if s[i] == j:
              time.sleep(.5)
              break
