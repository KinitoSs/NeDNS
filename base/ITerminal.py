import os
import abc


class ITerminal(metaclass=abc.ABCMeta):
    """Базовый класс терминала.

    Методы:
        clear(): "очищает" консоль (на самом деле принтует 80 пустых строк)
        pause(): "нажмите любую кнопку, чтобы продолжить"
    """
    
    def clear(self) -> None:
        """ "очищает" консоль (на самом деле принтует 80 пустых строк)"""
        print("\n" * 80)
        # pass

    def pause(self) -> None:
        """ "нажмите любую кнопку, чтобы продолжить" """
        os.system("pause")
