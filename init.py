from base.ITerminal import ITerminal
from view.main_view import MainView


if __name__ == "__main__":
    app: ITerminal = MainView()

    # print("""
    # Ноутбук или компьютер?
    # 1. Ноутбук
    # 2. Компьютер
    # """)
    # machine_choice = int(input("Введите нужную цифру: "))
    # if machine_choice == 1:
    #     machine_choice = "ноутбук"
    # elif machine_choice == 2:
    #     machine_choice = "комьютер"
    # else:
    #     print('Такого нет')
    #
    # print(f"""
    # Привет! Для чего Вам нужен {machine_choice}?
    # 1. Для игр
    # 2. Для работы с видео и графикой
    # 3. Для программирования
    # 4. Для работы в офисе и для учебы
    # """)
    #
    # user_output: list = list(map(int, input("Введите ваши ответы через запятую: ").split(',')))
    # priority: int = min(user_output)
    #
    # if machine_choice == "комьютер":
    #     print("Вам подойдут следующие комьютеры:")
    #     if priority == 1:
    #         print("""
    #         1. HP 2134 UltraGamingX [150 000, Ryzen 7 5600X, MSI RTX 3060, 16gb RAM, 1TB SSD, 750W]
    #         2. DEXP 228130 MicroGamingX [80 000, i5-10400F, GeForce MSI 2060S, 16gb RAM, 512gb SSD, 500W]
    #         """)
    #     elif priority == 2:
    #         print("""
    #         1. ASUS sus 323e33 [100 000, i5-12400F, GTX 1660 GP, 16gb RAM, 512gb SSD, HDD 2TB, 500W]
    #         2. ZOOMAN 234f [80 000, i5-10400F, GTX 1650 GP, 16gb RAM, 512gb SSD, HDD 1TB, 500W]
    #         """)
    #     elif priority == 3:
    #         print("""
    #         1. HP
    #         """)
    #     elif priority == 4:
    #         pass
    #
    # elif machine_choice == "ноутбук":
    #     if priority == 1:
    #         pass
    #     elif priority == 2:
    #         pass
    #     elif priority == 3:
    #         pass
    #     elif priority == 4:
    #         pass
    #
