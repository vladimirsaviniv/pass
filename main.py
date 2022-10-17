from itertools import product
import time
password = '99999999'
start_time = time.time()
chars = '0123456789'
#chars = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
for i in product(chars,repeat=len(password)):
  with open("number_password_8.txt", "a") as file:
      file.write(''.join(i))
      file.write('\n')
      print(''.join(i))
      if ''.join(i) == password:
          print('\nВаш пароль:',''.join(i),'\nПотребовалось времени:',round(float("%s" % (time.time() - start_time)),2),'секунд')
          break
