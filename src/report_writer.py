import json
from rich.console import Console
from rich.table import Table
from datetime import datetime

console = Console()

def save_report(data):
    ts = datetime.now().strftime("%Y%m%d-%H%M%S")
    path = f"incident_report_{ts}.json"
    with open(path, "w") as f:
        json.dump(data, f, indent=2)
    console.print(f"[green]Report saved as {path}[/green]")

def display_summary(data):
    table = Table(title="Incident Response Summary")
    table.add_column("Category", style="cyan")
    table.add_column("Findings", style="magenta")
    for key, value in data.items():
        table.add_row(key, str(value))
    console.print(table)
