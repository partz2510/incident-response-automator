import psutil

def collect_process_info():
    processes = []
    for p in psutil.process_iter(['pid', 'name', 'cpu_percent', 'username']):
        try:
            proc = p.info
            if proc['cpu_percent'] > 10:
                proc['alert'] = 'High CPU'
            processes.append(proc)
        except Exception:
            continue
    return processes

def collect_network_info():
    connections = []
    for conn in psutil.net_connections(kind='inet'):
        try:
            laddr = f"{conn.laddr.ip}:{conn.laddr.port}"
            raddr = f"{conn.raddr.ip}:{conn.raddr.port}" if conn.raddr else "-"
            connections.append({
                "pid": conn.pid,
                "local": laddr,
                "remote": raddr,
                "status": conn.status
            })
        except Exception:
            continue
    return connections
