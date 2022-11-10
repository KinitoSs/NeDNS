from base.ITerminal import ITerminal
from model.computer import Computer


class RecommendationView(ITerminal):
    """Экран рекомендуемых компьютеров."""

    __list_of_recommended_computers: list[Computer]

    def __init__(self, list_of_recommended_computers: list[Computer]):
        """Инициализация экрана рекомендуемых компьютеров.

        Аргументы:
            list_of_recommended_computers (list[Computer]): список рекомендуемых компьютеров
        """
        self.__list_of_recommended_computers = list_of_recommended_computers
        self.__compose()

    def __compose(self):
        """Метод, формирующий вывод экрана рекомендуемых компьютеров."""
        self.clear()
        print("Список рекомендуемых компьютеров/ноутбуков:")

        for computer in self.__list_of_recommended_computers:
            print(computer)

        self.pause()
