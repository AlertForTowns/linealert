import psutil

def get_system_summary():
    """
    Returns a dictionary with CPU, memory, and disk usage information.
    """
    cpu_percent = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory().percent
    disk = psutil.disk_usage('/').percent
    
    return {
        'CPU Usage (%)': cpu_percent,
        'Memory Usage (%)': memory,
        'Disk Usage (%)': disk
    }
