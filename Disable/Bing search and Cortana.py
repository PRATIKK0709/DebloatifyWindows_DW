import winreg

def set_registry_value(key_path, value_name, value_data, value_type=winreg.REG_DWORD):
    try:
        key = winreg.CreateKey(winreg.HKEY_CURRENT_USER, key_path)
        winreg.SetValueEx(key, value_name, 0, value_type, value_data)
        print(f"Registry value '{value_name}' set to '{value_data}' in '{key_path}'.")
        winreg.CloseKey(key)
    except Exception as e:
        print("An error occurred:", e)

set_registry_value(r"SOFTWARE\Microsoft\Windows\CurrentVersion\Search", "BingSearchEnabled", 0)

set_registry_value(r"SOFTWARE\Policies\Microsoft\Windows\Windows Search", "AllowCortana", 0)
print("Disabled BingSearch and Cortana.")
