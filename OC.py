import os
import platform
import socket
import json
from datetime import datetime
from getpass import getuser


data = {
    "operating_system": {
        "name": platform.system(),
        "version": platform.release(),
        "full_version": platform.version(),
        "architecture": platform.machine(),
        "processor": platform.processor()
    },

    "computer": {
        "hostname": socket.gethostname(),
        "username": getuser(),
        "cpu_count": os.cpu_count()
    },

    "python": {
        "version": platform.python_version(),
        "implementation": platform.python_implementation()
    },

    "environment": {
        "current_directory": os.getcwd(),
        "home_directory": os.path.expanduser("~")
    },

    "collection": {
        "date": datetime.now().isoformat()
    }
}

print("Операционная система:", data["operating_system"]["name"])
print("Версия:", data["operating_system"]["version"])
print("Архитектура:", data["operating_system"]["architecture"])
print("Имя компьютера:", data["computer"]["hostname"])

with open("os_info.json", "w", encoding="utf-8") as file:
    json.dump(data, file, ensure_ascii=False, indent=4)
    
    print("\nИнформация сохранена в файл os_info.json")
