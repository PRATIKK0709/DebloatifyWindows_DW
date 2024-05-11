import winreg

def set_registry_value(key_path, value_name, value_data, value_type=winreg.REG_DWORD):
    try:
        key = winreg.CreateKey(winreg.HKEY_CURRENT_USER, key_path)
        winreg.SetValueEx(key, value_name, 0, value_type, value_data)
        print(f"Registry value '{value_name}' set to '{value_data}' in '{key_path}'.")
        winreg.CloseKey(key)
    except Exception as e:
        print("An error occurred:", e)
# Windows 11 Taskbar Dashboard
set_registry_value(r"Software\Microsoft\Windows\CurrentVersion\Explorer\Advanced", "TaskbarDa", 0)

# Windows 10 Taskbar Feeds
set_registry_value(r"Software\Microsoft\Windows\CurrentVersion\Feeds", "ShellFeedsTaskbarViewMode", 2)

# Disable Widgets service
set_registry_value(r"SOFTWARE\Microsoft\PolicyManager\default\NewsAndInterests\AllowNewsAndInterests", "value", 0)
set_registry_value(r"SOFTWARE\Policies\Microsoft\Dsh", "AllowNewsAndInterests", 0)
