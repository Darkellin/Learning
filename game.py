# Импортируем модуль под Excel
import xlrd
file = "Test.xlsx"
# открываем файл Excel
wb = xlrd.open_workbook(file)
#выбираем вкладку Excel
sheet0 = wb.sheet_by_index(0)

#Запрашиваем данные, текст вопроса будет у нас в первой колонке. Соответственно переменной у нас будет строка.
question = 0
answer = 1
while question < 5:
        print(sheet0.cell_value(question, 0))
        question += 1
        answer = 1
        while answer < 12:
            print(sheet0.cell_value(question, answer))
            answer += 2
        if
        
        

  
Первый вопрос
    Первый ответ
    Второй ответ
    Третий Ответ
    Четвертый ответ
    Пятый ответ
    Шестой ответ
Второй вопрос
    Первый ответ
    Второй ответ
    Третий Ответ
    Четвертый ответ
    Пятый ответ
    Шестой ответ


