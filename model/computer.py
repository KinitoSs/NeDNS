from enum import Enum


class CpuOrGpuFirm(Enum):
    INTEL = 1
    AMD = 2
    NVIDIA = 3


class ComputerType(Enum):
    PC = 1
    LAPTOP = 2


class Computer:
    firm: str = None
    model: str = None
    type: ComputerType = None
    price: float = None
    cpu_firm: CpuOrGpuFirm = None
    cpu_series: int = None
    ram_size: int = None
    ram_hrz: int = None
    gpu: CpuOrGpuFirm = None
    gpu_series: int = None
    gpu_vram: int = None
    ssd_size: int = None
    hdd_size: int = None

    def set_all_params(self, firm, model, type, price, cpu_firm, cpu_series,
                       ram_size, ram_hrz, gpu, gpu_series, gpu_vram, ssd_size,
                       hdd_size) -> None:
        self.firm: str = firm
        self.model: str = model
        self.type: ComputerType = type
        self.price: float = price
        self.cpu_firm: CpuOrGpuFirm = cpu_firm
        self.cpu_series: int = cpu_series
        self.ram_size: int = ram_size
        self.ram_hrz: int = ram_hrz
        self.gpu: CpuOrGpuFirm = gpu
        self.gpu_series: int = gpu_series
        self.gpu_vram: int = gpu_vram
        self.ssd_size: int = ssd_size
        self.hdd_size: int = hdd_size

    def __str__(self):
        return f"{self.firm} - {self.model} - {self.price} - {self.cpu_firm} - {self.cpu_series} - {self.ram_size}"


def get_list_of_all_computers() -> list[Computer]:
    return [Computer(), Computer(), Computer(), Computer(), Computer(), Computer(), Computer(), Computer(), Computer(),
            Computer(), Computer(), Computer(), Computer(), Computer(), Computer(), Computer(), Computer(), Computer()]
