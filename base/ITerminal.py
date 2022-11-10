import os


class ITerminal:
    def clear(self) -> None:
        # print('\n' * 80)
        pass

    def pause(self) -> None:
        os.system('pause')
