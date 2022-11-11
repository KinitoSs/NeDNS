from base.IPcFilter import IPcFilter
from model.computer import Computer, ComputerType, CpuOrGpuFirm


class PcFilter(IPcFilter):
    """Класс, фильтрующий компьютеры."""
    
    __list_of_computers: list[Computer]

    def __init__(self, list_of_computers: list[Computer]) -> None:
        self.__list_of_computers = list_of_computers

    def return_list_of_filtered_computers(self) -> list[Computer]:
        return sorted(self.__list_of_computers, key=lambda x: x.price, reverse=False)

    def get_pcs(self) -> list[Computer]:
        result: list[Computer] = []
        for computer in self.__list_of_computers:
            if computer.computer_type == ComputerType.PC:
                result.append(computer)
        return result

    def get_laptops(self) -> list[Computer]:
        result: list[Computer] = []
        for computer in self.__list_of_computers:
            if computer.computer_type == ComputerType.LAPTOP:
                result.append(computer)
        return result

    def get_gaming_pcs(self) -> list[Computer]:
        result: list[Computer] = []
        for computer in self.__list_of_computers:
            if (
                (
                    (
                        computer.cpu_firm == CpuOrGpuFirm.AMD
                        and computer.cpu_series >= 3000
                    )
                    or (
                        computer.cpu_firm == CpuOrGpuFirm.INTEL
                        and computer.cpu_series >= 10000
                    )
                )
                and (
                    (
                        computer.gpu == CpuOrGpuFirm.NVIDIA
                        and computer.gpu_series >= 2000
                    )
                    or (
                        computer.gpu == CpuOrGpuFirm.AMD and computer.gpu_series >= 6600
                    )
                )
                and (computer.gpu_vram >= 6)
                and (computer.ram_size >= 32)
                and (computer.ssd_size >= 400)
                and (computer.hdd_size >= 900)
            ):
                result.append(computer)
        return result

    def get_montage_pcs(self) -> list[Computer]:
        result: list[Computer] = []
        for computer in self.__list_of_computers:
            if (
                (
                    (
                        computer.cpu_firm == CpuOrGpuFirm.AMD
                        and computer.cpu_series >= 2500
                    )
                    or (
                        computer.cpu_firm == CpuOrGpuFirm.INTEL
                        and computer.cpu_series >= 9000
                    )
                )
                and (
                    (
                        computer.gpu == CpuOrGpuFirm.NVIDIA
                        and computer.gpu_series >= 1600
                    )
                    or (
                        computer.gpu == CpuOrGpuFirm.AMD and computer.gpu_series >= 6500
                    )
                )
                and (computer.gpu_vram >= 6)
                and (computer.ram_size >= 16)
                and (computer.hdd_size >= 1000)
                and (computer.ssd_size >= 250)
            ):
                result.append(computer)
        return result

    def get_programming_pcs(self) -> list[Computer]:
        result: list[Computer] = []
        for computer in self.__list_of_computers:
            if (
                (
                    (
                        computer.cpu_firm == CpuOrGpuFirm.AMD
                        and computer.cpu_series >= 2400
                    )
                    or (
                        computer.cpu_firm == CpuOrGpuFirm.INTEL
                        and computer.cpu_series >= 9500
                    )
                )
                and (
                    (
                        computer.gpu == CpuOrGpuFirm.NVIDIA
                        and computer.gpu_series >= 2000
                    )
                    or (
                        computer.gpu == CpuOrGpuFirm.AMD and computer.gpu_series >= 6000
                    )
                )
                and (computer.gpu_vram >= 4)
                and (computer.ram_size >= 8)
                and (computer.ssd_size >= 128)
                and (computer.hdd_size >= 1000)
            ):
                result.append(computer)
        return result

    def get_office_pcs(self) -> list[Computer]:
        result: list[Computer] = []
        for computer in self.__list_of_computers:
            if (
                (
                    (
                        computer.cpu_firm == CpuOrGpuFirm.AMD
                        and computer.cpu_series >= 1000
                    )
                    or (
                        computer.cpu_firm == CpuOrGpuFirm.INTEL
                        and computer.cpu_series >= 8000
                    )
                )
                and (
                    (computer.gpu == CpuOrGpuFirm.NVIDIA and computer.gpu_series >= 700)
                    or (
                        computer.gpu == CpuOrGpuFirm.AMD and computer.gpu_series >= 5000
                    )
                )
                and (computer.gpu_vram >= 1)
                and (computer.ram_size >= 4)
                and (computer.hdd_size >= 500)
                and (computer.ssd_size >= 0)
            ):
                result.append(computer)
        return result
