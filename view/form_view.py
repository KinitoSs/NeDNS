from base.ITerminal import ITerminal
from utils.get_choice_char import get_choice_char
from viewModel.recomendations_view_model import RecommendationsViewModel


class ViewAskFor(ITerminal):
    __choice: int
    __choice_str: str
    __choice_range: int

    def __init__(self, choice_str, choice_range) -> None:
        self.__choice_str = choice_str
        self.__choice_range = choice_range
        self.__compose()

    def __compose(self) -> None:
        print(self.__choice_str)
        self.__choice = get_choice_char(self.__choice_range)
        print()

    def return_choice(self) -> int:
        return self.__choice


class FormView(ITerminal):
    __pc_or_laptop: int  # 1: PC, 2: LAPTOP
    __is_for_gaming: int  # 1: Yes, 2: No
    __is_for_montage: int  # 1: Yes, 2: No
    __is_for_programming: int  # 1: Yes, 2: No
    __is_for_office: int  # 1: Yes, 2: No

    def __init__(self) -> None:
        super().__init__()
        self.__compose()
        self.__form_reslut_handle()

    def __compose(self) -> None:
        self.clear()
        print("Для получения рекомендованного ПК/ноутбука пройдите простую форму.")
        print("==================================================================\n")
        self.__fill_form_result()

    def __fill_form_result(self) -> None:
        self.__pc_or_laptop = ViewAskFor("Какой тип вы предпочитаете?\n1. Персональный компьютер\n2. Ноутбук",
                                         2).return_choice()
        self.__is_for_gaming = ViewAskFor("Играете в игры?\n1. Да\n2. Нет", 2).return_choice()
        self.__is_for_montage = ViewAskFor("Работаете ли с видео/графикой?\n1. Да\n2. Нет", 2).return_choice()
        self.__is_for_programming = ViewAskFor("Будете ли вы программировать?\n1. Да\n2. Нет", 2).return_choice()
        self.__is_for_office = ViewAskFor("Учитесь ли вы / работаете в оффисе?\n1. Да\n2. Нет", 2).return_choice()

    def __form_reslut_handle(self) -> None:
        __form_result_dict = {
            'pc_or_laptop': self.__pc_or_laptop,
            'is_for_gaming': self.__is_for_gaming,
            'is_for_montage': self.__is_for_montage,
            'is_for_programming': self.__is_for_programming,
            'is_for_office': self.__is_for_office
        }
        RecommendationsViewModel(__form_result_dict)
