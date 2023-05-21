def main ():
  intro()
  try :
    mile_need = float(input('Enter the number of miles: '))

  except :
    print('An error occured, try again using only numbers.')
    print()
    main()

  
  else :
     mile_to_km(mile_need)


def intro():
  print('This program converts miles into kilometers')
  print()

def mile_to_km(mile):
  km = mile * 1.61
  print (mile, 'miles converts to ', km, 'kilometers.')

main()