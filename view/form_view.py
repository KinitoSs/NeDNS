from base.ITerminal import ITerminal
from utils.get_choice_char import get_choice_char
from viewModel.recomendations_view_model import RecommendationsViewModel


class ViewAskFor(ITerminal):
    """Класс, генерирующий view вопроса с вариантами ответов.

    Методы:
        return_coice(): Возвращает выбор пользователя
    """

    __choice: int
    __choice_str: str
    __choice_range: int

    def __init__(self, choice_str, choice_range) -> None:
        """Конструктор всех нужных атрибутов.

        Параметры:
            choice_str (str): сам вопрос
            choice_range (int): количество вариантов ответа
        """
        self.__choice_str = choice_str
        self.__choice_range = choice_range
        self.__compose()

    def __compose(self) -> None:
        """Метод, формирующий вывод вопроса с вариантами ответов на экран (консоль)."""
        print(self.__choice_str)
        self.__choice = get_choice_char(self.__choice_range)
        print()

    def return_choice(self) -> int:
        """Метод, вовзращающий выбор пользователя

        Returns:
            int: выбор пользователя
        """
        return self.__choice


class FormView(ITerminal):
    """Форма, в которой выявляются предпочтения пользователя в выборе компьютера."""

    __pc_or_laptop: int  # 1: PC, 2: LAPTOP
    __is_for_gaming: int  # 1: Yes, 2: No
    __is_for_montage: int  # 1: Yes, 2: No
    __is_for_programming: int  # 1: Yes, 2: No
    __is_for_office: int  # 1: Yes, 2: No
    __price: int

    def __init__(self) -> None:
        """Инициализация формы."""
        super().__init__()
        self.__compose()
        self.__form_reslut_handle()

    def __compose(self) -> None:
        """Метод, формирующий вывод формы на экран."""
        self.clear()
        print("Для получения рекомендованного ПК/ноутбука пройдите простую форму.")
        print("==================================================================\n")
        self.__fill_form_result()

    def __fill_form_result(self) -> None:
        """Метод, выводящий вопросы на экран и запоминающий выборы пользователя."""
        self.__pc_or_laptop = ViewAskFor(
            "Какой тип вы предпочитаете?\n1. Персональный компьютер\n2. Ноутбук", 2
        ).return_choice()
        self.__is_for_gaming = ViewAskFor(
            "Играете в игры?\n1. Да\n2. Нет", 2
        ).return_choice()
        self.__is_for_montage = ViewAskFor(
            "Работаете ли с видео/графикой?\n1. Да\n2. Нет", 2
        ).return_choice()
        self.__is_for_programming = ViewAskFor(
            "Будете ли вы программировать?\n1. Да\n2. Нет", 2
        ).return_choice()
        self.__is_for_office = ViewAskFor(
            "Учитесь ли вы / работаете в оффисе?\n1. Да\n2. Нет", 2
        ).return_choice()
        self.__price = int(input(("Сколько вы готовы отдать за компьютер: ")))

    def __form_reslut_handle(self) -> None:
        """Метод, обрабатывающий ввод пользователей."""
        __form_result_dict = {
            "pc_or_laptop": self.__pc_or_laptop,
            "is_for_gaming": self.__is_for_gaming,
            "is_for_montage": self.__is_for_montage,
            "is_for_programming": self.__is_for_programming,
            "is_for_office": self.__is_for_office,
            "price": self.__price
        }
        RecommendationsViewModel(__form_result_dict)
