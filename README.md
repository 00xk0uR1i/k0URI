# WP Exploit Scanner

WP Exploit Scanner is a multi-functional tool for scanning, detecting, and exploiting vulnerabilities in WordPress websites. It integrates multiple features such as Shodan and ZoomEye queries, Nuclei scanning, and auto-exploitation. Additionally, it allows users to import custom Python exploit scripts for dynamic execution.

Features
WordPress Vulnerability Scanning: Detect vulnerabilities in WordPress sites using APIs and known methods.
Shodan Integration: Search for WordPress-related systems using the Shodan API.
ZoomEye Integration: Query ZoomEye for WordPress-related systems.
Nuclei Scanning: Use Nuclei templates to scan for CVEs, misconfigurations, and WordPress-specific issues.
Auto-Exploitation: Exploit known vulnerabilities automatically.
Custom Exploit Import: Import and execute Python-based exploit scripts dynamically.

Requirements
Python Dependencies
Install the required Python libraries:

pip install requests pyfiglet rich shodan

Additional Tools
Shodan API Key
ZoomEye API Key
Nuclei:
Download and install Nuclei.
Configure the NUCLEI_PATH and NUCLEI_TEMPLATES variables in the script.

Installation
Clone the repository:

git clone https://github.com/yourusername/wp-exploit-scanner.git
cd wp-exploit-scanner
Configure the script:

Add your Shodan API key:
SHODAN_API_KEY = "your_shodan_api_key"
Add your ZoomEye API key (if applicable).
Configure the Nuclei path and templates.
Run the script:

python scanner.py --help
Usage
General Syntax
python scanner.py [OPTIONS]
Options
--target: Specify the target WordPress site URL.
--shodan: Perform a Shodan search for WordPress-related systems.
--zoomeye: Perform a ZoomEye search for WordPress-related systems.
--nuclei: Scan the target with Nuclei.
--exploit: Attempt to auto-exploit known vulnerabilities.
--import-exploit: Import and execute a custom Python exploit script.
Examples
Scan a WordPress site for vulnerabilities:

python scanner.py --target "http://example.com"
Perform a Shodan search for WordPress sites:

python scanner.py --shodan
Scan with Nuclei:

python scanner.py --target "http://example.com" --nuclei
Automatically exploit vulnerabilities:

python scanner.py --target "http://example.com" --exploit
Import and run a custom exploit script:

python scanner.py --target "http://example.com" --import-exploit "/path/to/exploit.py"
Example Exploit Script
Below is an example of a custom exploit script that can be imported:

def run_exploit(target):
    print(f"Running custom exploit on {target}")
    # Add exploit logic here (e.g., sending malicious payloads)
    response = requests.get(f"{target}/vulnerable_endpoint")
    if response.status_code == 200:
        print(f"Exploit succeeded! Response: {response.text}")
    else:
        print("Exploit failed.")
Ethical Usage
This tool is intended for ethical use only. Unauthorized testing or exploitation is illegal and may result in severe consequences. Use it only on systems you own or have explicit permission to test.

License
This project is licensed under the MIT License.

Author
k0ur1i

GitHub
LinkedIn
Would you like to include additional sections, such as API configuration or troubleshooting?






