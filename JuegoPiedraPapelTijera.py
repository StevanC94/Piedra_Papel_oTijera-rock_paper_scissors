import random
options =('piedra','papel','tijera' )
computer_wins = 0
user_wins = 0
rounds =1
x= input('\nBienvenido \nIngresa tu nombre: ').upper()
while True:

  print('*'*20) 
  print('ROUND',rounds)
  print('*'*20)
  print('MARCADOR')
  print('computadora = ',computer_wins)
  print(x+' = ',user_wins)
  print('*'*20)
  print('\nBienvenido '+ x +'\nIngrese la seleccion de su preferencia')
  user_option = input('piedra, papel o tijera: ').lower()
  rounds += 1
  computer_option = random.choice(options)
  if not user_option in options:
    print('\nINFORMACION INVALIDA\n')
    continue
  print('opcion seleccionada por el jugador 1: \n',user_option)
  print('opcion seleccionada por la computadora: \n',computer_option)
  if user_option == computer_option:
    print('Empate!')
  elif user_option =='piedra' :
    if computer_option =='tijera':
      print('piedra gana a tijera!')
      print('*'*20)
      print('GANO'+x+'!')
      print('*'*20)
      user_wins +=1
    else:
      print('papel gana a piedra')
      print('computadora gano')
      computer_wins +=1
  elif user_option == 'papel':
    if computer_option == 'tijera':
      print('tijera gana a papel!')
      print('*'*20)
      print('computadora gana!')
      print('*'*20)
      computer_wins +=1
    else:
      print('papel gana a piedra')
      print('*'*20)
      print('GANO'+x+'!')
      print('*'*20)
      user_wins +=1
  elif user_option == 'tijera':
    if computer_option == 'piedra':
      print('piedra gana a papel!')
      print('*'*20)
      print('computadora gana!')
      print('*'*20)
      computer_wins +=1
    else:
      print('tijera gana a papel')
      print('*'*20)
      print('GANO'+x+'!')
      print('*'*20)
      user_wins +=1
  if computer_wins == 2:
    print('/'*30)
    print('LA COMPUTADORA ES LA GANADORA')
    print('/'*30)
    break
  if user_wins == 2:
    print('/'*30)
    print(x +'ES EL GANADOR')
    print('/'*30)
    break
  
  