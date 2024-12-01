# WPEXpl0itScann3r

```
██████╗ ██╗    ██╗███████╗ ██████╗ █████╗ ███╗   ██╗███╗   ███╗███████╗██████╗ 
██╔══██╗██║    ██║██╔════╝██╔════╝██╔══██╗████╗  ██║████╗ ████║██╔════╝██╔══██╗
██████╔╝██║ █╗ ██║█████╗  ██║     ███████║██╔██╗ ██║██╔████╔██║█████╗  ██████╔╝
██╔═══╝ ██║███╗██║██╔══╝  ██║     ██╔══██║██║╚██╗██║██║╚██╔╝██║██╔══╝  ██╔═══╝ 
██║     ╚███╔███╔╝███████╗╚██████╗██║  ██║██║ ╚████║██║ ╚═╝ ██║███████╗██║     
╚═╝      ╚══╝╚══╝ ╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝     ╚═╝╚══════╝╚═╝     
Author: k0ur1i
GitHub: https://github.com/00xk0uR1i
==================================================
Importing exploit from /path/to/example.py...00xk0uR1i
Running exploit on http://example.com...00xk0uR1i
Running custom exploit on http://example.com
Exploit succeeded! Response: Exploit Successful!

```
<img src="[IMG_LINK](https://github-production-user-asset-6210df.s3.amazonaws.com/101189469/391305173-3eeadcaf-7c76-46cc-b49a-3d7c8e6f66c6.jpg)" width="100" height="100"/>




##  WPExploitScanner is a multi tool for scanning, detecting, and exploiting vulnerabilities in WordPress websites. It integrates multiple features such as Shodan and ZoomEye queries, Nuclei scanning, and auto-exploitation. Additionally, it allows users to import custom Python exploit scripts for dynamic execution.
## Features
1. WordPress Vulnerability Scanning: Detect vulnerabilities in WordPress sites using APIs and known methods.
2. Shodan Integration: Search for WordPress-related systems using the Shodan API.
3. ZoomEye Integration: Query ZoomEye for WordPress-related systems.
4. Nuclei Scanning: Use Nuclei templates to scan for CVEs, misconfigurations, and WordPress-specific issues.
5. Auto-Exploitation: Exploit known vulnerabilities automatically.
6. Custom Exploit Import: Import and execute Python-based exploit scripts dynamically.

## Install and run

1. pip install requests pyfiglet rich shodan. 
2. ```git clone https://github.com/00xk0uR1i/k0URI ```
3. Run the script:
    - `python k0ur1iScan.py --help`
    - `python k0ur1iScan.py [OPTIONS]` ✨ new ✨
    - `python k0ur1iScan.py --target "http://example.com"` ✨ new ✨
    - `python k0ur1iScan.py --shodan`
    - `python k0ur1iScan.py --target "http://example.com" --nuclei`
    - `python k0ur1iScan.py --target "http://example.com" --exploit` ✨ new ✨
    - `python k0ur1iScan.py --target "http://example.com" --import-exploit "/path/to/exploit.py"`

This tool is intended for ethical use only. Unauthorized testing or exploitation is illegal and may result in severe consequences. Use it only on systems you own or have explicit permission to test. **Note**: They might not get updated frequently and are kept for legacy reasons:

- `Configure the script` (Add your Shodan API key:
SHODAN_API_KEY = "your_shodan_api_key")
- `Add your ZoomEye API key (if applicable).
   Configure the Nuclei path and templates.` (legacy)

## Example Exploit Script

```

Example Exploit Script
def run_exploit(target):
    print(f"Running custom exploit on {target}")
    response = requests.get(f"{target}/vulnerable_endpoint")
    if response.status_code == 200:
        print(f"Exploit succeeded! Response: {response.text}")
    else:
        print("Exploit failed.")

```


Note:

## This tools for ethical hacker I am Not responsible for any bad use .

## License
# This project is licensed under the MIT License.

>thanks for all 
