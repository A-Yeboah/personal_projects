# A versatile temperature converter that handles conversions between Celsius,
# Fahrenheit and Kelvin.

try:
  # import ast
  import ast

  # take the temperature value in degree celcius
  temp_from = (input('What temperature are you converting from(°C/°F/K):'))\
  .strip().lower()
  temp_to = (input('What temperature are you converting to(°C/°F/K)'))
  temperature = ast.literal_eval(input('What is the temperature?:'))

  # convert to Fahrenheit, Celcius and Kelvin respectively
  fah_temp_from_cel = (temperature * 1.8) + 32 # temp in Fahrenheit from Celcius
  kel_temp_from_cel = temperature + 273.15 # temp in Kelvin from Celcius
  cel_temp_from_fah = (temperature - 32) * 5/9 # temp in Celcius from Kelvin
  kel_temp_from_fah = (temperature - 32) * 5/9 + 273.15 # temp in K from C
  cel_temp_from_kel = temperature - 273.15 # temp in C from K
  fah_temp_from_kel = (temperature - 273.15) * 9/5 + 32 # temp in C from K

  # if user temp_from == 'Celcius'
  if temp_from.startswith('c'):
    if temp_to.startswith('f'):
      print(f'The temperature is {fah_temp_from_cel:.2f}°F')
    if temp_to.startswith('k'):
      print(f'The temperature is {kel_temp_from_cel:.2f}K')

  # if user temp_from == 'Fahrenheit'
  if temp_from.startswith('f'):
    if temp_to.startswith('c'):
      print(f'The temperature is {cel_temp_from_fah:.2f}°C')
    if temp_to.startswith('k'):
      print(f'The temperature is {kel_temp_from_fah:.2f}K')

  # if user temp_from == 'Kelvin'
  if temp_from.startswith('k'):
    if temp_to.startswith('c'):
      print(f'The temperature is {cel_temp_from_kel:.2f}°C')
    if temp_to.startswith('f'):
      print(f'The temperature is {fah_temp_from_kel:.2f}°F')

except ValueError:
  print('You did not input the correct value:')

