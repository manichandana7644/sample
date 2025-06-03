import os
import platform
import subprocess

def print_system_uptime():
    system = platform.system()
    uptime = ""
    if system == "Windows":
        # Windows: use 'net stats srv' and parse output
        try:
            output = subprocess.check_output("net stats srv", shell=True, text=True)
            for line in output.splitlines():
                if "Statistics since" in line:
                    uptime = line
                    break
        except Exception as e:
            uptime = f"Error fetching uptime: {e}"
    elif system == "Linux":
        # Linux: use 'uptime -p'
        try:
            uptime = subprocess.check_output("uptime -p", shell=True, text=True).strip()
        except Exception as e:
            uptime = f"Error fetching uptime: {e}"
    elif system == "Darwin":
        # macOS: use 'uptime'
        try:
            uptime = subprocess.check_output("uptime", shell=True, text=True).strip()
        except Exception as e:
            uptime = f"Error fetching uptime: {e}"
    else:
        uptime = "Unsupported OS for uptime retrieval."
    
    print("System Uptime:")
    print(uptime)

if __name__ == "__main__":
    print_system_uptime()`
