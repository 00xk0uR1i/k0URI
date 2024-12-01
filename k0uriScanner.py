import requests
import argparse
import pyfiglet
from rich.console import Console
from shodan import Shodan
import subprocess
import importlib.util
import os

# Configuration
SHODAN_API_KEY = "your_shodan_api_key"
ZOOMEYE_API_KEY = "your_zoomeye_api_key"
NUCLEI_PATH = "/path/to/nuclei"  # Path to Nuclei binary
NUCLEI_TEMPLATES = "/path/to/nuclei-templates"  # Path to Nuclei templates

console = Console()

def display_panel():
    """Display an ASCII art panel with author credits."""
    ascii_art = pyfiglet.figlet_format("WPExploitScanner")
    console.print(ascii_art, style="bold green")
    console.print("[bold cyan]Author: K0ur1i[/bold cyan]")
    console.print("[bold magenta]GitHub: https://github.com/00xk0uR1i[/bold magenta]")
    console.print("=" * 50, style="bold yellow")

def scan_with_shodan(query):
    """Search for WordPress sites using Shodan."""
    console.print("[bold yellow]Scanning with Shodan...[/bold yellow]")
    try:
        api = Shodan(SHODAN_API_KEY)
        results = api.search(query)
        for result in results['matches']:
            console.print(f"[bold blue]IP:[/bold blue] {result['ip_str']}, [bold blue]Port:[/bold blue] {result['port']}")
    except Exception as e:
        console.print(f"[bold red]Shodan error:[/bold red] {e}")

def scan_with_zoomeye(query):
    """Search for WordPress sites using ZoomEye."""
    console.print("[bold yellow]Scanning with ZoomEye...[/bold yellow]")
    try:
        # ZoomEye API example logic
        console.print(f"[bold cyan]Search ZoomEye for query: {query} (API usage required to implement fully).[/bold cyan]")
    except Exception as e:
        console.print(f"[bold red]ZoomEye error:[/bold red] {e}")

def scan_with_nuclei(target):
    """Scan a target site using Nuclei."""
    console.print(f"[bold yellow]Scanning {target} with Nuclei...[/bold yellow]")
    try:
        cmd = [
            NUCLEI_PATH,
            "-u", target,
            "-t", f"{NUCLEI_TEMPLATES}/cves/",
            "-t", f"{NUCLEI_TEMPLATES}/misconfiguration/",
            "-t", f"{NUCLEI_TEMPLATES}/wordpress/"
        ]
        result = subprocess.run(cmd, capture_output=True, text=True)
        console.print(result.stdout)
    except Exception as e:
        console.print(f"[bold red]Nuclei error:[/bold red] {e}")

def load_and_execute_exploit(file_path, target):
    """Dynamically load and execute an exploit script."""
    console.print(f"[bold yellow]Importing exploit from {file_path}...[/bold yellow]")
    try:
        # Dynamically load the Python script as a module
        spec = importlib.util.spec_from_file_location("custom_exploit", file_path)
        exploit_module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(exploit_module)
        
        # Check if the exploit script has a run_exploit function
        if hasattr(exploit_module, "run_exploit"):
            console.print(f"[bold green]Running exploit on {target}...[/bold green]")
            exploit_module.run_exploit(target)
        else:
            console.print("[bold red]Error: Exploit script must define a `run_exploit(target)` function.[/bold red]")
    except Exception as e:
        console.print(f"[bold red]Failed to execute exploit:[/bold red] {e}")

def auto_exploit(domain):
    """Automatically exploit known vulnerabilities."""
    console.print(f"[bold yellow]Attempting auto-exploitation on {domain}...[/bold yellow]")
    # Example exploit: WordPress REST API Content Injection
    known_exploits = [
        {
            "name": "WordPress Admin Shell Upload",
            "endpoint": f"{domain}/wp-admin/",
            "payload": {"malicious": "payload"}
        }
    ]
    for exploit in known_exploits:
        try:
            console.print(f"[bold blue]Exploiting: {exploit['name']}[/bold blue]")
            response = requests.post(exploit["endpoint"], data=exploit["payload"])
            if response.status_code == 200:
                console.print("[bold green]Exploit successful![/bold green]")
            else:
                console.print("[bold red]Exploit failed.[/bold red]")
        except Exception as e:
            console.print(f"[bold red]Error during exploitation: {e}[/bold red]")

def check_wordpress_vulnerabilities(domain):
    """Check WordPress vulnerabilities."""
    console.print(f"[bold yellow]Scanning WordPress site:[/bold yellow] {domain}")
    try:
        response = requests.get(f"{domain}/wp-json")
        if response.status_code != 200:
            console.print("[bold red]Site does not appear to be running WordPress or API is restricted.[/bold red]")
            return

        wordpress_version = response.json().get('generator', {}).get('version', 'unknown')
        console.print(f"[bold green]Detected WordPress version:[/bold green] {wordpress_version}")

        # Query WPScan Vulnerability Database (if available)
        vulnerabilities_url = f"https://wpscan.com/api/v3/cmses/wordpress/versions/{wordpress_version}?api_token=your_wpscan_api_key"
        vuln_response = requests.get(vulnerabilities_url)
        if vuln_response.status_code == 200:
            data = vuln_response.json()
            if "vulnerabilities" in data:
                console.print("[bold red]Vulnerabilities found:[/bold red]")
                for vuln in data["vulnerabilities"]:
                    console.print(f"- [bold cyan]{vuln['title']}[/bold cyan]: {vuln.get('description', 'No description provided.')}")
            else:
                console.print("[bold green]No vulnerabilities found.[/bold green]")
        else:
            console.print("[bold red]Failed to fetch vulnerabilities from WPScan.[/bold red]")
    except Exception as e:
        console.print(f"[bold red]Error:[/bold red] {e}")

if __name__ == "__main__":
    display_panel()

    parser = argparse.ArgumentParser(description="Multi-tool WordPress vulnerability scanner with exploitation capabilities")
    parser.add_argument("--target", help="Target WordPress site URL")
    parser.add_argument("--shodan", help="Shodan search query", action="store_true")
    parser.add_argument("--zoomeye", help="ZoomEye search query", action="store_true")
    parser.add_argument("--nuclei", help="Target for Nuclei scan", action="store_true")
    parser.add_argument("--exploit", help="Automatically exploit known vulnerabilities", action="store_true")
    parser.add_argument("--import-exploit", help="Path to a Python exploit script")

    args = parser.parse_args()

    if args.target:
        check_wordpress_vulnerabilities(args.target)

    if args.shodan:
        query = "http.html:'wp-login'"
        scan_with_shodan(query)

    if args.zoomeye:
        query = "app:\"WordPress\""
        scan_with_zoomeye(query)

    if args.nuclei and args.target:
        scan_with_nuclei(args.target)

    if args.exploit and args.target:
        auto_exploit(args.target)

    if args.import_exploit and args.target:
        if os.path.exists(args.import_exploit):
            load_and_execute_exploit(args.import_exploit, args.target)
        else:
            console.print(f"[bold red]Exploit script not found at {args.import_exploit}[/bold red]")
