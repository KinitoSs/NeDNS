from base.ITerminal import ITerminal
from utils.get_choice_char import get_choice_char
from view.form_view import FormView


class MainView(ITerminal):
    __choice: int

    def __init__(self) -> None:
        super().__init__()
        self.__compose()
        self.__handle_choice()

    def __compose(self) -> None:
        self.clear()
        print(
            "NeDNS - программа по подбору компьютера/ноутбука в соответствии с вашими предпочтениями."
        )
        print(
            "========================================================================================\n"
        )
        print("Меню:\n1. Подобрать ПК/ноутбук\n2. Выход")
        self.__choice = get_choice_char(2)

    def __handle_choice(self) -> None:
        if self.__choice == 1:
            FormView()
            self.__init__()
        else:
            return
