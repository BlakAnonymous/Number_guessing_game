run = True
while True:
    user_input = int(input('Enter Number: '))
    if user_input == 7:
        print('Congratulations, you guessed correctly!')
        break
    else:
        print('Sorry, wrong guess!')
        continue