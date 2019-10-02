def is_leap(x):
       if(x % 4 == 0 and (x % 400 == 0 or x % 100 != 0)):
           print('leap year')
       else: 
           print('not ;eap year')
year = int(input("Input year"))
is_leap(year)

