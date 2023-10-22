29.Create a program that prompts the user to enter numbers until they enter 'q'
to quit, then calculate the sum.


total = 0
while True:
    d = input('enter a integer or enter q to quit>')
    if d == 'q':
        break
        total+=int(d)
        print(f'running total:{total}')
