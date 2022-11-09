from base.ITerminal import ITerminal
from model.computer import Computer


class RecommendationView(ITerminal):
    __list_of_recommended_computers: list[Computer]

    def __init__(self, list_of_recommended_computers):
        self.__list_of_recommended_computers = list_of_recommended_computers
        self.__compose()
        self.__render_main_view()

    def __compose(self):
        self.clear()
        print("Список рекомендуемых компьютеров/ноутбуков:")

        for computer in self.__list_of_recommended_computers:
            print(computer)

        self.pause()

    def __render_main_view(self):
        pass
