

#for i in range(5):
 #   print("{} iteration through the loop".format(i))
  #  i+=2


i = 0

while i < 10:
    i += 1
    if i == 4:
        continue

    print("{} iteration through the loop".format(i))

else:
    print('all done')


for y in range(0, 10, 1):

    if y == 3:
        continue
    print('I can count to ' + str(y))
else:
    print('all done?')
