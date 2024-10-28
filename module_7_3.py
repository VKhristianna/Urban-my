# Представим, что файл 'test_file.txt' содержит следующий текст:
# It`s a text for task Найти везде,
# Используйте его для самопроверки.
# Успехов в решении задачи!
# text text text

text_file = 'test_file.txt'
with open(text_file, 'w', encoding='utf-8') as file:
    file.write('It`s a text for task Найти везде,\nИспользуйте его для самопроверки.\nУспехов в решении задачи!\ntext text text\n')

    '''
Напишите класс WordsFinder, объекты которого создаются следующим образом:
WordsFinder('file1.txt, file2.txt', 'file3.txt', ...).
Объект этого класса должен принимать при создании неограниченного количество названий файлов 
и записывать их в атрибут file_names в виде списка или кортежа.    
'''

class WordsFinder:  
    def __init__(self, *file_names):  
        self.file_names = file_names  

    '''
get_all_words - метод, который возвращает словарь следующего вида:
{'file1.txt': ['word1', 'word2'], 'file2.txt': ['word3', 'word4'], 'file3.txt': ['word5', 'word6', 'word7']}
Создайте пустой словарь all_words.
Переберите названия файлов и открывайте каждый из них, используя оператор with.
Для каждого файла считывайте единые строки, переводя их в нижний регистр (метод lower()).
Избавьтесь от пунктуации [',', '.', '=', '!', '?', ';', ':', ' - '] в строке.
Разбейте эту строку на элементы списка методом split().
В словарь all_words запишите полученные данные, ключ - название файла, значение - список из слов этого файла.    
'''
    def get_all_words(self):  
        all_words = {}  
        punctuation = [',', '.', '=', '!', '?', ';', ':', ' - ']
        for file_name in self.file_names:  
            with open(file_name, 'r', encoding='utf-8') as file:  
                text = file.read().lower()          # Приводим текст к нижнему регистру
                for char in punctuation:            # Избавляемся от пунктуации
                    text = text.replace(char, '')
                all_words[file_name] = text.split() # Разбиваем текст на слова
        return all_words

    '''
find(self, word) - метод, где word - искомое слово.
Возвращает словарь, где ключ - название файла, значение - позиция первого такого слова в списке слов этого файла.
В методах find и count пользуйтесь ранее написанным методом get_all_words для получения названия файла и списка его слов.
Для удобного перебора одновременно ключа(названия) и значения(списка слов) можно воспользоваться методом словаря - item().
'''
    def find(self, word):  
        word = word.lower()                         # Приводим слово к нижнему регистру
        find_dict = {}
        all_words = self.get_all_words()  
        for file_name, words in all_words.items():  
            if word in words:  
                find_dict[file_name] = words.index(word)
        return find_dict

    '''
count(self, word) - метод, где word - искомое слово.
Возвращает словарь, где ключ - название файла, значение - количество слова word в списке слов этого файла.
'''
    def count(self, word):  
        word = word.lower()
        count_dict = {}
        all_words = self.get_all_words()  
        for file_name, words in all_words.items():  
            count = words.count(word)  
            if count > 0:
                count_dict[file_name] = count
        return count_dict

# Пример использования:  
finder2 = WordsFinder('test_file.txt')  
print(finder2.get_all_words())  # Все слова
print(finder2.find('TEXT'))      # Позиция слова
print(finder2.count('teXT'))     # Количество слова в тексте

# Вывод на консоль:
# {'test_file.txt': ["it's", 'a', 'text', 'for', 'task', 'найти', 'везде', 'используйте', 'его', 'для',
# 'самопроверки', 'успехов', 'в', 'решении', 'задачи', 'text', 'text', 'text']}
# {'test_file.txt': 3}
# {'test_file.txt': 4}
