import wmi
seperator = "-----------------------------------------------------------------------------------------------------"
c = wmi.WMI()
def get_wmi_info(input,name):
    system_wmi_raw = input()
    system_wmi_str = f"{seperator}\n".join(str(nic) for nic in system_wmi_raw)
        

    system_wmi_str = "\n".join(line.replace(";","") for line in system_wmi_str.splitlines())
    system_wmi_str = "\n".join(line.replace('"',"") for line in system_wmi_str.splitlines())
    system_wmi_str = "\n".join(line.replace('}',"") for line in system_wmi_str.splitlines())
    system_wmi_str = "\n".join(line.replace('{',"") for line in system_wmi_str.splitlines())
    system_wmi_str = "\n".join(line.replace(f'instance of {name}',"") for line in system_wmi_str.splitlines())
    system_wmi_str = "\n".join(line.strip() for line in system_wmi_str.splitlines())
    system_wmi_str = "\n".join(filter(None, (line.strip() for line in system_wmi_str.splitlines())))


    system_wmi_str = system_wmi_str.strip()
    return system_wmi_str
    
