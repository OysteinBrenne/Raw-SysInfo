import wmi
from modules import wmi_info as wmii
import sys
c = wmi.WMI()


#commands // sys,cpu,ram,disk,gpu,mb,bios,users,network,windows,battery,startup,audio,display,input

cli_arg = str(sys.argv[1]).lower()
if cli_arg == "sys":
    print (wmii.get_wmi_info(c.Win32_ComputerSystem,"Win32_ComputerSystem"))
elif cli_arg == "cpu":
    print (wmii.get_wmi_info(c.Win32_Processor,"Win32_Processor"))

elif cli_arg == "ram":
    print(wmii.get_wmi_info(c.Win32_PhysicalMemory,"Win32_PhysicalMemory"))

elif cli_arg == "disk":
    print(wmii.get_wmi_info(c.Win32_DiskDrive,"Win32_DiskDrive"))

elif cli_arg == "gpu":
    print(wmii.get_wmi_info(c.Win32_VideoController,"Win32_VideoController"))

elif cli_arg == "mb":
    print(wmii.get_wmi_info(c.Win32_BaseBoard,"Win32_BaseBoard"))

elif cli_arg == "bios":
    print(wmii.get_wmi_info(c.Win32_BIOS,"Win32_BIOS"))

elif cli_arg == "users":
    print(wmii.get_wmi_info(c.Win32_UserAccount,"Win32_UserAccount"))

elif cli_arg == "net":
    print(wmii.get_wmi_info(c.Win32_NetworkAdapterConfiguration,"Win32_NetworkAdapterConfiguration"))

elif cli_arg == "windows":
    print(wmii.get_wmi_info(c.Win32_OperatingSystem,"Win32_OperatingSystem"))

elif cli_arg == "battery":
    print(wmii.get_wmi_info(c.Win32_Battery,"Win32_Battery"))

elif cli_arg == "startup":
    print(wmii.get_wmi_info(c.Win32_StartupCommand,"Win32_StartupCommand"))

elif cli_arg == "audio":
    print(wmii.get_wmi_info(c.Win32_SoundDevice,"Win32_SoundDevice"))

elif cli_arg == "display":
    print(wmii.get_wmi_info(c.Win32_DesktopMonitor,"Win32_DesktopMonitor"))

elif cli_arg == "input":
    print(wmii.get_wmi_info(c.Win32_Keyboard,"Win32_Keyboard"))
    print(wmii.get_wmi_info(c.Win32_PointingDevice,"Win32_PointingDevice"))

elif cli_arg == "custom":
    arg_custom = str(sys.argv[2])
    try:
        print(wmii.get_wmi_info(getattr(c, arg_custom), arg_custom))
    except Exception as error:
        print("invalid command " + str(error))


elif cli_arg == "help":
    print("Raw Sysinfo 0.8")
    print("github.com/OysteinBrenne/Raw-SysInfo")
    print("--------------------------------------")
    print("sys")
    print("cpu")
    print("ram")
    print("disk")
    print("gpu")
    print("mb")
    print("bios")
    print("users")
    print("net")
    print("windows")
    print("battery")
    print("startup")
    print("audio")
    print("display")
    print("input")
    print("`custom` must include a second argument ie pconfig custom Win32_Keyboard")


else: 
    print (f"{cli_arg} is not a valid argument, use help to list avalible arguments")
print ()