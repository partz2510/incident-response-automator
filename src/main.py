import json
from ir_collector import collect_process_info, collect_network_info
from vt_lookup import vt_hash_lookup
from report_writer import save_report, display_summary


def main():
    processes = collect_process_info()
    net = collect_network_info()
    sample_hash = "44d88612fea8a8f36de82e1278abb02f"  # test (EICAR)
    vt_result = vt_hash_lookup(sample_hash)

    report = {
        "Processes": len(processes),
        "Network Connections": len(net),
        "VirusTotal Lookup": vt_result.get("data", {}).get("attributes", {}).get("reputation", "N/A")
    }

    display_summary(report)
    save_report(report)

if __name__ == "__main__":
    main()
