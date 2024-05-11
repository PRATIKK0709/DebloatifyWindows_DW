import winreg

def set_registry_value(key_path, value_name, value_data, value_type=winreg.REG_DWORD):
    try:
        key = winreg.CreateKey(winreg.HKEY_CURRENT_USER, key_path)
        winreg.SetValueEx(key, value_name, 0, value_type, value_data)
        print(f"Registry value '{value_name}' set to '{value_data}' in '{key_path}'.")
        winreg.CloseKey(key)
    except Exception as e:
        print("An error occurred:", e)

# Disable Copilot button on taskbar
set_registry_value(r"Software\Microsoft\Windows\CurrentVersion\Explorer\Advanced", "ShowCopilotButton", 0)

# Disable Copilot service for current user
set_registry_value(r"Software\Policies\Microsoft\Windows\WindowsCopilot", "TurnOffWindowsCopilot", 1)
print("Windows Copilot service disabled for the current user.")

# Disable Copilot service for all users
set_registry_value(r"SOFTWARE\Policies\Microsoft\Windows\WindowsCopilot", "TurnOffWindowsCopilot", 1, value_type=winreg.REG_DWORD)
print("Windows Copilot service disabled for all users.")
