# Реализуйте класс Wordplay, описывающий расширяемый набор слов. При создании экземпляра класс должен принимать один аргумент:
# words — список, определяющий начальный набор слов. Если не передан, начальный набор слов считается пустым
# Экземпляр класса Wordplay должен иметь один атрибут:
# words — список, содержащий набор слов
# Класс Wordplay должен иметь четыре метода экземпляра:
# add_word() — метод, принимающий в качестве аргумента слово и добавляющий его в набор. Если слово уже есть в наборе, метод ничего не должен делать
# words_with_length() — метод, принимающий в качестве аргумента натуральное число n и возвращающий список слов из набора, длина которых равна n
# only() — метод, принимающий произвольное количество аргументов — букв, и возвращающий все слова из набора, которые включают в себя только переданные буквы
# avoid() — метод, принимающий произвольное количество аргументов — букв, и возвращающий все слова из списка words, которые не содержат ни одну из этих букв

class Wordplay:
    def __init__(self, words=()):
        self.words = list(words)

    def add_word(self, w):
        if w not in self.words:
            self.words += (w, )

    def words_with_length(self, n):
        return list(filter(lambda el: len(el) == n, self.words))

    def only(self, *args):
        return list(filter(lambda x: set(x) <= set(args), self.words))

    def avoid(self, *args):
        return list(filter(lambda x: set(x).isdisjoint(set(args)), self.words))
