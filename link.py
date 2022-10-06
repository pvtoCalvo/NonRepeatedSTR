import random
abecedarui = "abcdefghijklmnopqrstuvwxyz"
cadena = ''
for i in range(100):
    cadena = cadena + random.choice(abecedarui)
print("Cadena Original %s"%cadena)

cadena_grande = ''
cadena_pequena = ''



import time
start_time = time.time()

def first_repeated_char(str1):
  for index,c in enumerate(str1):
    if str1[:index+1].count(c) > 1:
      return index
  return None

for i in range(len(cadena)):
    index = first_repeated_char(cadena)
    if index is None:
        break
    if len(cadena_grande) < len(cadena[:index]):
            cadena_grande = cadena[:index]
    cadena = cadena[index+1:]



print ("Cadena Mas Grande %s"%cadena_grande)
print("--- %s seconds ---" % (time.time() - start_time))