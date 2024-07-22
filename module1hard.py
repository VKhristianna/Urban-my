# Дополнительное практическое задание по модулю: "Базовые структуры данных."
grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
a,b,c,d,e = grades # Присвоила переменные спискам
list_ball = [sum(a)/len(a),sum(b)/len(b),sum(c)/len(c),sum(d)/len(d),sum(e)/len(e)] # Средний балл по каждому студенту
#print(list_ball)
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
all_students = sorted(list(students)) # Преобразовала множество в список + сортировка по алфавиту
#print(all_students)
ball_students = dict(zip(all_students, map(float, list_ball))) # Объединила данные в словарь
print(ball_students)
