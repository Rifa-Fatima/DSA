days =int(input("How many day's temperature?"))
l =[]
for day in range(1,days+1):
    temp = int(input(f'Day {day}\'s temperature: '))
    l.append(temp)
average = sum(l)/len(l)
print(f'The average temperature is : {average}')
count = 0
for i in l:
    if int(i) > average:
        count +=1
print(f'{count} day(s) are above average temperature.')
    

