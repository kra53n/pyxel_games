from screeninfo import get_monitors


def get_monitor_resolution():
    monitor = get_monitors()[0]
    return monitor.width, monitor.height