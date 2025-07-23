import customtkinter as ctk
import ctypes,wmi,threading,pythoncom
from modules import font as font
from modules import wmi_info as wmii
from modules import welcome

c = wmi.WMI()
ctypes.windll.shcore.SetProcessDpiAwareness(1)

side_bar_width = 85
side_bar_frame_width = 85
side_bar_button_pady = 2

main = ctk.CTk()
main.resizable(width=False,height=False)

main.geometry("600x500")
main.title("Raw SysInfo 0.8")

main.grid_columnconfigure(0, weight=0,minsize=side_bar_width,)  
main.grid_columnconfigure(1, weight=1)  
main.grid_rowconfigure(1, weight=1)    
main.columnconfigure(2, weight=1)
main.columnconfigure(1, weight=1)

main_screen = ctk.CTkFrame(main,corner_radius=0)
main_screen.grid(row=1,column=1,columnspan=4,sticky="nsew",)

side_bar = ctk.CTkScrollableFrame(main,width=side_bar_frame_width,fg_color=font.fg_color_1,corner_radius=0,)
side_bar.grid(row=1,column=0,columnspan=1,sticky="ns" ,padx=0, pady=0,)
side_bar._scrollbar.grid_forget()

cpu_lock = threading.Lock()
net_lock = threading.Lock()

def clear_main_screen():
    for widget in main_screen.winfo_children():
        widget.destroy()
    for widget in side_bar.winfo_children():
        widget.configure(fg_color=font.fg_color_1)


                  
def start_welcome_info():
    clear_main_screen()
    info_label = ctk.CTkTextbox(main_screen,font=font.font_2,corner_radius=0,fg_color=font.fg_color_2)
    info_label.pack(fill="both",expand=True)
    info_label.insert("0.0",f"{welcome.welcome_text}")
    info_label.configure(state="disabled")

def start_sys_info():
    clear_main_screen()
    info_label = ctk.CTkTextbox(main_screen,font=font.font_2,corner_radius=0,fg_color=font.fg_color_2)
    info_label.pack(fill="both",expand=True)
    info_label.insert("0.0",wmii.get_wmi_info(c.Win32_ComputerSystem,"Win32_ComputerSystem"))
    info_label.configure(state="disabled")
    sidebar_system_button.configure(fg_color=font.clicked_color_1)

def start_disk_info():
    clear_main_screen()
    info_label = ctk.CTkTextbox(main_screen,font=font.font_2,fg_color=font.fg_color_2,corner_radius=0)
    info_label.pack(fill="both",expand=True)
    info_label.insert("0.0",wmii.get_wmi_info(c.Win32_DiskDrive,"Win32_DiskDrive"))
    info_label.configure(state="disabled")
    sidebar_storage_button.configure(fg_color=font.clicked_color_1)

def start_cpu_info():
    global cpu_lock
    if cpu_lock.locked():
        return
    
    clear_main_screen()
    sidebar_cpu_button.configure(fg_color=font.clicked_color_1)
    info_label = ctk.CTkTextbox(main_screen,font=font.font_2,fg_color=font.fg_color_2,corner_radius=0)
    info_label.pack(fill="both",expand=True)
    info_label.insert("0.0","Loading...")

    def cpu_start():
        with cpu_lock:    
            pythoncom.CoInitialize()
            cpu_wmi = wmi.WMI()
            data = wmii.get_wmi_info(cpu_wmi.Win32_Processor,"Win32_Processor")

            def update_gui ():
                try: 
                    if str(info_label) in main.tk.call("winfo","children",str(main_screen)):
                        info_label.insert("0.0",data)
                        info_label.configure(state="disabled")
                except Exception:
                    pass
            main.after(0, update_gui)
        
    threading.Thread(target=cpu_start,daemon=True).start()
        

def start_ram_info():
    clear_main_screen()
    sidebar_ram_button.configure(fg_color=font.clicked_color_1)
    info_label = ctk.CTkTextbox(main_screen,font=font.font_2,fg_color=font.fg_color_2,corner_radius=0)
    info_label.pack(fill="both",expand=True)
    info_label.insert("0.0",wmii.get_wmi_info(c.Win32_PhysicalMemory,"Win32_PhysicalMemory"))
    info_label.configure(state="disabled")

def start_gpu_info():
    clear_main_screen()
    sidebar_gpu_button.configure(fg_color=font.clicked_color_1)
    info_label = ctk.CTkTextbox(main_screen,font=font.font_2,fg_color=font.fg_color_2,corner_radius=0)
    info_label.pack(fill="both",expand=True)
    info_label.insert("0.0",wmii.get_wmi_info(c.Win32_VideoController,"Win32_VideoController"))
    info_label.configure(state="disabled")

def start_mb_info():
    clear_main_screen()
    sidebar_motherboard_button.configure(fg_color=font.clicked_color_1)
    info_label = ctk.CTkTextbox(main_screen,font=font.font_2,fg_color=font.fg_color_2,corner_radius=0)
    info_label.pack(fill="both",expand=True)
    info_label.insert("0.0",wmii.get_wmi_info(c.Win32_BaseBoard,"Win32_BaseBoard"))
    info_label.configure(state="disabled")

def start_bios_info():
    clear_main_screen()
    sidebar_bios_button.configure(fg_color=font.clicked_color_1)
    info_label = ctk.CTkTextbox(main_screen,font=font.font_2,fg_color=font.fg_color_2,corner_radius=0)
    info_label.pack(fill="both",expand=True)
    info_label.insert("0.0",wmii.get_wmi_info(c.Win32_BIOS,"Win32_BIOS"))
    info_label.configure(state="disabled")

def start_users_info():
    clear_main_screen()
    sidebar_users_button.configure(fg_color=font.clicked_color_1)
    info_label = ctk.CTkTextbox(main_screen,font=font.font_2,fg_color=font.fg_color_2,corner_radius=0)
    info_label.pack(fill="both",expand=True)
    info_label.insert("0.0",wmii.get_wmi_info(c.Win32_UserAccount,"Win32_UserAccount"))
    info_label.configure(state="disabled")
    

def start_net_info():
    global net_lock
    if net_lock.locked():
        return
    clear_main_screen()
    sidebar_network_button.configure(fg_color=font.clicked_color_1)
    info_label = ctk.CTkTextbox(main_screen,font=font.font_2,fg_color=font.fg_color_2,corner_radius=0)
    info_label.pack(fill="both",expand=True)
    info_label.insert("0.0","Loading...")


    def net_start():
        with net_lock:
            pythoncom.CoInitialize()
            net_wmi =wmi.WMI()
            data = wmii.get_wmi_info(net_wmi.Win32_NetworkAdapterConfiguration,"Win32_NetworkAdapterConfiguration")
            def update_net_gui ():
                try: 
                    if str(info_label) in main.tk.call("winfo","children",str(main_screen)):
                        info_label.insert("0.0",data)
                        info_label.configure(state="disabled")
                except Exception:
                    pass
            
            main.after(0,update_net_gui)
    threading.Thread(target=net_start,daemon=True).start()
    

def start_audio_info():
    clear_main_screen()
    sidebar_audio_button.configure(fg_color=font.clicked_color_1)
    info_label = ctk.CTkTextbox(main_screen,font=font.font_2,fg_color=font.fg_color_2,corner_radius=0)
    info_label.pack(fill="both",expand=True)
    info_label.insert("0.0",wmii.get_wmi_info(c.Win32_SoundDevice,"Win32_SoundDevice"))
    info_label.configure(state="disabled")
    

def start_windows_info():
    clear_main_screen()
    sidebar_windows_button.configure(fg_color=font.clicked_color_1)
    info_label = ctk.CTkTextbox(main_screen,font=font.font_2,fg_color=font.fg_color_2,corner_radius=0)
    info_label.pack(fill="both",expand=True)
    info_label.insert("0.0",wmii.get_wmi_info(c.Win32_OperatingSystem,"Win32_OperatingSystem"))
    info_label.configure(state="disabled")
    

def start_battery_info():
    clear_main_screen()
    sidebar_battery_button.configure(fg_color=font.clicked_color_1)
    info_label = ctk.CTkTextbox(main_screen,font=font.font_2,fg_color=font.fg_color_2,corner_radius=0)
    info_label.pack(fill="both",expand=True)
    info_label.insert("0.0",wmii.get_wmi_info(c.Win32_Battery,"Win32_Battery"))
    info_label.configure(state="disabled")
    

def start_display_info():
    clear_main_screen()
    sidebar_displays_button.configure(fg_color=font.clicked_color_1)
    info_label = ctk.CTkTextbox(main_screen,font=font.font_2,fg_color=font.fg_color_2,corner_radius=0)
    info_label.pack(fill="both",expand=True)
    info_label.insert("0.0",wmii.get_wmi_info(c.Win32_DesktopMonitor,"Win32_DesktopMonitor"))
    info_label.configure(state="disabled")
    

def start_input_info():
    clear_main_screen()
    sidebar_input_button.configure(fg_color=font.clicked_color_1)
    info_label = ctk.CTkTextbox(main_screen,font=font.font_2,fg_color=font.fg_color_2,corner_radius=0)
    info_label.pack(fill="both",expand=True)
    info_label.insert("0.0",wmii.get_wmi_info(c.Win32_Keyboard,"Win32_Keyboard")+ "\n")
    info_label.insert("0.0",wmii.get_wmi_info(c.Win32_PointingDevice,"Win32_PointingDevice")+ "\n")
    info_label.configure(state="disabled")
    

def start_startup_cmd_info():
    clear_main_screen()
    sidebar_startup_cmd_button.configure(fg_color=font.clicked_color_1)
    info_label = ctk.CTkTextbox(main_screen,font=font.font_2,fg_color=font.fg_color_2,corner_radius=0)
    info_label.pack(fill="both",expand=True)
    info_label.insert("0.0",wmii.get_wmi_info(c.Win32_StartupCommand,"Win32_StartupCommand")+ "\n")
    info_label.configure(state="disabled")



def refresh_side_bar ():
    global sidebar_system_button,sidebar_cpu_button,sidebar_ram_button
    global sidebar_storage_button,sidebar_gpu_button,sidebar_motherboard_button,sidebar_bios_button
    global sidebar_users_button,sidebar_network_button,sidebar_windows_button,sidebar_battery_button
    global sidebar_startup_cmd_button,sidebar_audio_button,sidebar_displays_button,sidebar_input_button

    for widget in side_bar.winfo_children():
        widget.destroy()
    sidebar_system_button = ctk.CTkButton(side_bar,text="System",fg_color=font.fg_color_1,font=font.font_1, corner_radius=font.corner_radius_1,width=side_bar_width,hover_color=font.hover_color_1,command=start_sys_info,border_width  = 0,)
    sidebar_system_button.pack(fill="x", anchor="w", )

    sidebar_cpu_button = ctk.CTkButton(side_bar,text="CPU",fg_color=font.fg_color_1,font=font.font_1, corner_radius=font.corner_radius_1,width=side_bar_width,hover_color=font.hover_color_1,command=start_cpu_info)
    sidebar_cpu_button.pack(pady=side_bar_button_pady)

    sidebar_ram_button = ctk.CTkButton(side_bar,text="RAM",fg_color=font.fg_color_1,font=font.font_1, corner_radius=font.corner_radius_1,width=side_bar_width,hover_color=font.hover_color_1,command=start_ram_info)
    sidebar_ram_button.pack(pady=side_bar_button_pady)

    sidebar_storage_button = ctk.CTkButton(side_bar,text="Storage",fg_color=font.fg_color_1,font=font.font_1, corner_radius=font.corner_radius_1,width=side_bar_width,hover_color=font.hover_color_1,command=start_disk_info)
    sidebar_storage_button.pack(pady=side_bar_button_pady)

    sidebar_gpu_button = ctk.CTkButton(side_bar,text="GPU",fg_color=font.fg_color_1,font=font.font_1, corner_radius=font.corner_radius_1,width=side_bar_width,hover_color=font.hover_color_1,command=start_gpu_info)
    sidebar_gpu_button.pack(pady=side_bar_button_pady)

    sidebar_motherboard_button = ctk.CTkButton(side_bar,text="Motherboard",fg_color=font.fg_color_1,font=font.font_1, corner_radius=font.corner_radius_1,width=side_bar_width,hover_color=font.hover_color_1,command=start_mb_info)
    sidebar_motherboard_button.pack(pady=side_bar_button_pady)

    sidebar_bios_button = ctk.CTkButton(side_bar,text="Bios",fg_color=font.fg_color_1,font=font.font_1, corner_radius=font.corner_radius_1,width=side_bar_width,hover_color=font.hover_color_1,command=start_bios_info)
    sidebar_bios_button.pack(pady=side_bar_button_pady)

    sidebar_users_button = ctk.CTkButton(side_bar,text="Users",fg_color=font.fg_color_1,font=font.font_1, corner_radius=font.corner_radius_1,width=side_bar_width,hover_color=font.hover_color_1,command=start_users_info)
    sidebar_users_button.pack(pady=side_bar_button_pady)

    sidebar_network_button = ctk.CTkButton(side_bar,text="Network",fg_color=font.fg_color_1,font=font.font_1, corner_radius=font.corner_radius_1,width=side_bar_width,hover_color=font.hover_color_1,command=start_net_info)
    sidebar_network_button.pack(pady=side_bar_button_pady)

    sidebar_windows_button = ctk.CTkButton(side_bar,text="Windows",fg_color=font.fg_color_1,font=font.font_1, corner_radius=font.corner_radius_1,width=side_bar_width,hover_color=font.hover_color_1,command=start_windows_info)
    sidebar_windows_button.pack(pady=side_bar_button_pady)

    sidebar_battery_button = ctk.CTkButton(side_bar,command=start_battery_info,text="Battery",fg_color=font.fg_color_1,font=font.font_1, corner_radius=font.corner_radius_1,width=side_bar_width,hover_color=font.hover_color_1)
    sidebar_battery_button.pack(pady=side_bar_button_pady)

    sidebar_startup_cmd_button = ctk.CTkButton(side_bar,command=start_startup_cmd_info,text="Startup cmd",fg_color=font.fg_color_1,font=font.font_1, corner_radius=font.corner_radius_1,width=side_bar_width,hover_color=font.hover_color_1)
    sidebar_startup_cmd_button.pack(pady=side_bar_button_pady)

    sidebar_audio_button = ctk.CTkButton(side_bar,text="Audio",fg_color=font.fg_color_1,font=font.font_1, corner_radius=font.corner_radius_1,width=side_bar_width,hover_color=font.hover_color_1,command=start_audio_info)
    sidebar_audio_button.pack(pady=side_bar_button_pady)

    sidebar_displays_button = ctk.CTkButton(side_bar,command=start_display_info,text="Displays",fg_color=font.fg_color_1,font=font.font_1, corner_radius=font.corner_radius_1,width=side_bar_width,hover_color=font.hover_color_1)
    sidebar_displays_button.pack(pady=side_bar_button_pady)

    sidebar_input_button = ctk.CTkButton(side_bar,command=start_input_info,text="Input",fg_color=font.fg_color_1,font=font.font_1, corner_radius=font.corner_radius_1,width=side_bar_width,hover_color=font.hover_color_1)
    sidebar_input_button.pack(pady=side_bar_button_pady)
    


refresh_side_bar ()

start_welcome_info()

main.mainloop()