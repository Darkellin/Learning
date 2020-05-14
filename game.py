# Импортируем модуль под Excel
import xlrd
import xlwt
file = "Test.xlsx"
# открываем файл Excel
wb = xlrd.open_workbook(file)
#выбираем вкладку Excel
sheet0 = wb.sheet_by_index(0)

#Запрашиваем данные, текст вопроса будет у нас в первой колонке. Соответственно переменной у нас будет строка.
question = 0
answer = 1
ListOfAnswers = []
while question < 5:
        print(sheet0.cell_value(question, 0))
        question += 1
        # модуль, собирающий баллы.
        while answer < 12:
            print(sheet0.cell_value(question, answer))
            answer += 2
        a = input("Ваш ответ...")
        ListOfAnswers.append(a)
        answer = 1   
print(ListOfAnswers)

my_list = [1, 2]
my_list.append(13)
print(my_list)