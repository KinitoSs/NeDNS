from model.computer import get_list_of_all_computers
from model.pc_filter import PcFilter
from view.recomendation_view import RecommendationView


class RecommendationsViewModel:
    __form_result: dict
    __pc_filter: PcFilter

    def __init__(self, form_result: dict) -> None:
        self.__form_result = form_result
        self.__pc_filter = PcFilter(get_list_of_all_computers())

        self.__filter(self.__form_result, self.__pc_filter)
        self.__render_recommendations_view()

    def __filter(self, form_result: dict, pc_filter: PcFilter) -> None:
        pass

    def __render_recommendations_view(self) -> None:
        RecommendationView(self.__pc_filter.return_list_of_filtered_computers())
