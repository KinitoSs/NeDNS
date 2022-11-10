from model.computer import get_list_of_all_computers
from model.pc_filter import PcFilter
from view.recomendation_view import RecommendationView


class RecommendationsViewModel:
    __form_result: dict
    __pc_filter: PcFilter

    def __init__(self, form_result: dict) -> None:
        self.__form_result = form_result
        self.__pc_filter = PcFilter(get_list_of_all_computers())

        self.__filter()
        self.__render_recommendations_view()

    def __filter(self) -> None:
        # self.__form_result['pc_or_laptop']: int           1: PC,  2: LAPTOP
        # self.__form_result['is_for_gaming']: int          1: Yes, 2: No
        # self.__form_result['is_for_montage']: int         1: Yes, 2: No
        # self.__form_result['is_for_programming']: int     1: Yes, 2: No
        # self.__form_result['is_for_office']: int          1: Yes, 2: No

        if self.__form_result["pc_or_laptop"] == 1:
            self.__pc_filter = PcFilter(self.__pc_filter.get_pcs())
        else:
            self.__pc_filter = PcFilter(self.__pc_filter.get_laptops())

        if self.__form_result["is_for_gaming"] == 1:
            self.__pc_filter = PcFilter(self.__pc_filter.get_gaming_pcs())
        elif self.__form_result["is_for_montage"] == 1:
            self.__pc_filter = PcFilter(self.__pc_filter.get_montage_pcs())
        elif self.__form_result["is_for_programming"] == 1:
            self.__pc_filter = PcFilter(self.__pc_filter.get_programming_pcs())
        elif self.__form_result["is_for_office"] == 1:
            self.__pc_filter = PcFilter(self.__pc_filter.get_office_pcs())

    def __render_recommendations_view(self) -> None:
        RecommendationView(self.__pc_filter.return_list_of_filtered_computers())
