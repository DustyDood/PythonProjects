num1 = 12
key = False


if num1 == 12:
    if key:
        print('Num1 is equal to 12 and they have the key')
    else:
        print('Num1 is equal to 12 and they do not have the key')
elif num1 < 12:
    print('Num1 is less than 12')
else:
    print('Num1 is not equal to 12')

rexrex = 100
tatsu = 1
tora = 102

if rexrex > tora:
    if rexrex > tatsu:
        print('rexrex is the winner!')
    else:
        print('tatsu is the winner! But everyone knows that is false')
elif tora > tatsu:
    print('tora is the winner!')
else:
    print('the results are inconclusive!')

print(isinstance(tatsu,float))
