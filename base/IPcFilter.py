from model.computer import Computer
import abc


class IPcFilter(metaclass=abc.ABCMeta):
    """Базовый класс для фильтрации компьютеров.
    
    Методы:
        return_list_of_filtered_computers() -> list[Computer]: должен возвращать список всех отфильтрованных компьютеров
        get_pcs()  -> list[Computer]: должен возвращать список всех ПК
        get_laptops() -> list[Computer]: должен возвращать список всех ноутбуков
        get_gaming_pcs() -> list[Computer]: должен возвращать список всех игровых компьютеров
        get_montage_pcs() -> list[Computer]: должен возвращать список всех компьютеров для монтажа/графики
        get_programming_pcs() -> list[Computer]: должен возвращать список всех компьютеров для программирования
        get_office_pcs() -> list[Computer]: должен возвращать список всех оффисных компьютеров
    """     
    @abc.abstractmethod 
    def __init__(self, list_of_computers: list[Computer]) -> None:
        pass

    @abc.abstractmethod 
    def return_list_of_filtered_computers(self) -> list[Computer]:
        """Должен возвращать список всех отфильтрованных компьютеров.

        Возвращает:
            list[Computer]: список всех отфильтрованных компьютеров
        """        
        pass

    @abc.abstractmethod 
    def get_pcs(self) -> list[Computer]:
        """Должен возвращать список всех ПК.

        Возвращает:
            list[Computer]: список всех ПК
        """        
        pass

    @abc.abstractmethod 
    def get_laptops(self) -> list[Computer]:
        """Должен возвращать список всех ноутбуков.

        Возвращает:
            list[Computer]: список всех ноутбуков
        """        
        pass

    @abc.abstractmethod 
    def get_gaming_pcs(self) -> list[Computer]:
        """Должен возвращать список всех игровых компьютеров.

        Возвращает:
            list[Computer]: список всех игровых компьютеров
        """        
        pass

    @abc.abstractmethod 
    def get_montage_pcs(self) -> list[Computer]:
        """Должен возвращать список всех компьютеров для монтажа/графики.

        Возвращает:
            list[Computer]: список всех компьютеров для монтажа/графики
        """    
        pass

    @abc.abstractmethod 
    def get_programming_pcs(self) -> list[Computer]:
        """Должен возвращать список всех компьютеров для программирования.

        Возвращает:
            list[Computer]: список всех компьютеров для программирования
        """        
        pass

    @abc.abstractmethod 
    def get_office_pcs(self) -> list[Computer]:
        """Должен возвращать список всех оффисных компьютеров.

        Возвращает:
            list[Computer]: список всех оффисных компьютеров
        """        
        pass
