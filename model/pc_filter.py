from model.computer import Computer, ComputerType


class PcFilter:
    __list_of_computers: list[Computer]

    def __init__(self, list_of_computers: list[Computer]) -> None:
        self.__list_of_computers = list_of_computers

    def return_list_of_filtered_computers(self) -> list[Computer]:
        return self.__list_of_computers

    def get_pcs(self) -> list[Computer]:
        result: list[Computer] = []
        for computer in self.__list_of_computers:
            if computer.type == ComputerType.PC:
                result.append(computer)
        return result

    def get_laptops(self) -> list[Computer]:
        result: list[Computer] = []
        for computer in self.__list_of_computers:
            if computer.type == ComputerType.LAPTOP:
                result.append(computer)
        return result
