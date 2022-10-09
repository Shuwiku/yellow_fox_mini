import socket
import pythoncom
import wmi


def user_pc():  # Получить данные о ПК
    pythoncom.CoInitialize()

    pc = wmi.WMI()
    pc_info = pc.Win32_ComputerSystem()[0]

    os_info = pc.Win32_OperatingSystem()[0]
    sys_os = str(os_info.Name.split('|')[0])

    sys_cpu = str(pc.Win32_Processor()[0].Name)
    sys_gpu = str(pc.Win32_VideoController()[0].Name)
    ram = float(os_info.TotalVisibleMemorySize)
    sys_ram = str(ram / 1048576)

    pc_owner = str(pc_info.PrimaryOwnerName)
    pc_family = str(pc_info.SystemFamily)
    pc_time_zone = str(pc_info.CurrentTimeZone)

    info = {
        'os': sys_os,
        'cpu': sys_cpu, 'gpu': sys_gpu, 'ram': sys_ram,
        'pc_owner': pc_owner, 'pc_family': pc_family, 
        'pc_time_zone': pc_time_zone
    }
    return info


def user_name():  # Получить имя ПК
    name = socket.gethostname()
    return name


def user_ip():  # Получить IP ПК
    name = user_name()
    ip = socket.gethostbyname(name)
    return ip
