 #  E2 lab 4
 #    @author Jacobo Henao / Stefania Zapata / David Sánchez

def min(y, z, x, morning, afternoon):
    total_morning   = total(morning)
    total_afternoon = total(afternoon)
    limit = y*z
    hours = total_morning + total_afternoon
    return (hours - limit) * x
    
def total(hor):
    total = 0
    for i in hor:
        total += i
    return total

def convert_input(linea):
    for i in range(len(linea)):
        linea[i] = int(linea[i])
        
linea = input()

while(linea != '0 0 0'):
    linea = linea.split(' ')
    convert_input(linea)
    
    if linea[0] < 1 or linea[1] < 1 or linea[2] < 1 or linea[0] > 100 or linea[1] > 10000 or linea[2] > 5:
        print('invalid input')
        break
    
    morning   = input().split(' ')
    afternoon = input().split(' ')
    convert_input(morning)
    convert_input(afternoon)
    
    print(min(linea[0], linea[1], linea[2], morning, afternoon))
    linea = input()
    