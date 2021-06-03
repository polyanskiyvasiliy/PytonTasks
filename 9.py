minsInHour = 60

print('В первой строке введите назначенное время втречи по паттерну \"ЧЧ:ММ\" \n с новой строчки время прибытия')

h1, m1 = map(int, input().split(sep=':'))
h2, m2 = map(int, input().split(sep=':'))

m1 = minsInHour * h1 + m1
m2 = minsInHour * h1 + m2

if abs(m1 - m2) > 15:
    print('Встреча не состоится')
else:
    print('Встреча состоится')
