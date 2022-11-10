from enum import Enum


class CpuOrGpuFirm(Enum):
    INTEL = 1
    AMD = 2
    NVIDIA = 3


class ComputerType(Enum):
    PC = 1
    LAPTOP = 2


class Computer:
    # firm: str = None
    # model: str = None
    # computer_type: ComputerType = None
    # price: float = None
    # cpu_firm: CpuOrGpuFirm = None
    # cpu_series: int = None
    # ram_size: int = None
    # ram_hrz: int = None
    # gpu: CpuOrGpuFirm = None
    # gpu_series: int = None
    # gpu_vram: int = None
    # ssd_size: int = None
    # hdd_size: int = None
    
    def __init__(self, firm: str, model: str, computer_type: ComputerType, price: float, cpu_firm: CpuOrGpuFirm, cpu_series: int,
                       ram_size: int, ram_hrz: int, gpu: CpuOrGpuFirm, gpu_series: int, gpu_vram: int, ssd_size: int,
                       hdd_size: int):
        self.firm = firm
        self.model = model
        self.computer_type = computer_type
        self.price = price
        self.cpu_firm = cpu_firm
        self.cpu_series = cpu_series
        self.ram_size = ram_size
        self.ram_hrz = ram_hrz
        self.gpu: CpuOrGpuFirm = gpu
        self.gpu_series = gpu_series
        self.gpu_vram = gpu_vram
        self.ssd_size = ssd_size
        self.hdd_size = hdd_size

    def set_all_params(self, firm: str, model: str, computer_type: ComputerType, price: float, cpu_firm: CpuOrGpuFirm, cpu_series: int,
                       ram_size: int, ram_hrz: int, gpu: CpuOrGpuFirm, gpu_series: int, gpu_vram: int, ssd_size: int,
                       hdd_size: int):        
        self.firm = firm
        self.model = model
        self.computer_type = computer_type
        self.price = price
        self.cpu_firm = cpu_firm
        self.cpu_series = cpu_series
        self.ram_size = ram_size
        self.ram_hrz = ram_hrz
        self.gpu: CpuOrGpuFirm = gpu
        self.gpu_series = gpu_series
        self.gpu_vram = gpu_vram
        self.ssd_size = ssd_size
        self.hdd_size = hdd_size

    def __str__(self):
        return f"{self.firm} - {self.model} - {self.price} - {self.cpu_firm} - {self.cpu_series} - {self.gpu} - {self.gpu_series} - {self.ram_size} - {self.ssd_size} - {self.hdd_size}"


def get_list_of_all_computers() -> list[Computer]:
    result = [Computer(firm="Типа оффисный", 
                       model="34FE", 
                       computer_type=ComputerType.PC, 
                       price=80000, 
                       cpu_firm=CpuOrGpuFirm.INTEL, 
                       cpu_series=10400,
                       ram_size=16,
                       ram_hrz=2400,
                       gpu=CpuOrGpuFirm.NVIDIA,
                       gpu_series=2600,
                       gpu_vram=4,
                       ssd_size=500,
                       hdd_size=1000),
              Computer(firm="DEXP", 
                       model="34FE", 
                       computer_type=ComputerType.PC, 
                       price=80000, 
                       cpu_firm=CpuOrGpuFirm.INTEL, 
                       cpu_series=10400,
                       ram_size=16,
                       ram_hrz=2400,
                       gpu=CpuOrGpuFirm.NVIDIA,
                       gpu_series=2600,
                       gpu_vram=4,
                       ssd_size=500,
                       hdd_size=1000),
              Computer(firm="DEXP", 
                       model="34FE", 
                       computer_type=ComputerType.PC, 
                       price=80000, 
                       cpu_firm=CpuOrGpuFirm.INTEL, 
                       cpu_series=13000,
                       ram_size=50,
                       ram_hrz=2400,
                       gpu=CpuOrGpuFirm.NVIDIA,
                       gpu_series=4090,
                       gpu_vram=41,
                       ssd_size=1500,
                       hdd_size=1000),
              Computer(firm="DEXP", 
                       model="34FE", 
                       computer_type=ComputerType.PC, 
                       price=80000, 
                       cpu_firm=CpuOrGpuFirm.INTEL, 
                       cpu_series=10400,
                       ram_size=16,
                       ram_hrz=2400,
                       gpu=CpuOrGpuFirm.NVIDIA,
                       gpu_series=2600,
                       gpu_vram=4,
                       ssd_size=500,
                       hdd_size=1000),
              Computer(firm="DEXP", 
                       model="34FE", 
                       computer_type=ComputerType.PC, 
                       price=80000, 
                       cpu_firm=CpuOrGpuFirm.INTEL, 
                       cpu_series=10400,
                       ram_size=16,
                       ram_hrz=2400,
                       gpu=CpuOrGpuFirm.NVIDIA,
                       gpu_series=2600,
                       gpu_vram=4,
                       ssd_size=500,
                       hdd_size=1000),
            ]
    return result
