import os


class ITerminal:
    def clear(self) -> None:
        print('\n' * 80)

    def pause(self) -> None:
        os.system('pause')
