import winreg

def set_registry_value(key_path, value_name, value_data, value_type=winreg.REG_DWORD):
    try:
        key = winreg.CreateKey(winreg.HKEY_CURRENT_USER, key_path)
        winreg.SetValueEx(key, value_name, 0, value_type, value_data)
        print(f"Registry value '{value_name}' set to '{value_data}' in '{key_path}'.")
        winreg.CloseKey(key)
    except Exception as e:
        print("An error occurred:", e)

# Disable tips, tricks, and suggestions in Start, Settings, and Notifications
set_registry_value(r"SOFTWARE\Microsoft\Windows\CurrentVersion\ContentDeliveryManager", "SystemPaneSuggestionsEnabled", 0)
set_registry_value(r"SOFTWARE\Microsoft\Windows\CurrentVersion\ContentDeliveryManager", "SubscribedContent-338393Enabled", 0)
set_registry_value(r"SOFTWARE\Microsoft\Windows\CurrentVersion\ContentDeliveryManager", "OemPreInstalledAppsEnabled", 0)

# Disable ads in Windows Explorer
set_registry_value(r"SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\Advanced", "ShowSyncProviderNotifications", 0)

# Disable ads on the lock screen
set_registry_value(r"SOFTWARE\Policies\Microsoft\Windows\Personalization", "NoLockScreenAds", 1)

# Disable fun facts, tips, and more from Windows and Cortana on the lock screen
set_registry_value(r"SOFTWARE\Microsoft\Windows\CurrentVersion\ContentDeliveryManager", "SubscribedContent-338387Enabled", 0)
set_registry_value(r"SOFTWARE\Microsoft\Windows\CurrentVersion\ContentDeliveryManager", "RotatingLockScreenOverlayEnabled", 0)

print("Tips, tricks, suggestions, ads, and lock screen content disabled successfully.")
