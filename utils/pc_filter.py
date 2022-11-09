# def filter_by_type(pc_list: list, pc_type: PcType) -> list:
#     result: list = []
#     for pc in pc_list:
#         if pc.type == pc_type:
#             result.append(pc)
#     return result
#
#
# def get_gaming_pcs(pc_list: list) -> list:
#     result: list = []
#     for pc in pc_list:
#         if ((pc.cpu_firm == CpuOrGpuFirm.AMD and pc.cpu_series >= 3000) or
#             (pc.cpu_firm == CpuOrGpuFirm.INTEL and pc.cpu_series >= 10000)) and \
#                 ((pc.gpu == CpuOrGpuFirm.NVIDIA and pc.gpu_series >= 2000) or
#                  (pc.gpu == CpuOrGpuFirm.AMD and pc.gpu_series >= 6600)) and \
#                 (pc.gpu_vram >= 6) and \
#                 (pc.ram_size >= 32) and \
#                 (pc.hdd_size >= 1000) and \
#                 (pc.hdd_size >= 500):
#             result.append(pc)
#     return result
