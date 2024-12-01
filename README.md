WP Exploit Scanner by k0ur1i
WP Exploit Scanner is a comprehensive tool for scanning, detecting, and exploiting vulnerabilities in WordPress websites. It integrates multiple functionalities, including Shodan and ZoomEye searches, Nuclei scanning, auto-exploitation, and the ability to import custom exploit scripts.

Features
WordPress Vulnerability Scanning: Detect vulnerabilities in WordPress installations.
Shodan Integration: Search for WordPress-related systems using Shodan.
ZoomEye Integration: Search for WordPress-related systems using ZoomEye.
Nuclei Scanning: Use Nuclei templates to identify CVEs, misconfigurations, and WordPress-specific issues.
Auto-Exploitation: Automatically exploit known vulnerabilities.
Custom Exploit Import: Dynamically import and execute Python exploit scripts.


Requirements :
Python Dependencies :
- Install the necessary Python libraries:

- pip install requests pyfiglet rich shodan
Additional Tools
Shodan API Key
ZoomEye API Key
Nuclei:
Install Nuclei and configure its path in the script.



Installation
Clone the repository:

git clone https://github.com/00xk0uR1i/k0URI.git
cd wpk0ur1i-Exploiter
Configure the script:

Add your Shodan API key:
SHODAN_API_KEY = "your_shodan_api_key"
Add your ZoomEye API key (if applicable).
Configure the Nuclei path and templates.



Run the script:

python k0ur1i.py --help
Usage
General Syntax
python k0ur1i.py [OPTIONS]
Options
--target: Specify the target WordPress site URL.
--shodan: Perform a Shodan search for WordPress-related systems.
--zoomeye: Perform a ZoomEye search for WordPress-related systems.
--nuclei: Scan the target with Nuclei.
--exploit: Attempt to auto-exploit known vulnerabilities.
--import-exploit: Import and execute a custom Python exploit script.


Examples:
Scan a WordPress site for vulnerabilities:

python k0uR1i.py --target "http://example.com"
Perform a Shodan search for WordPress sites:

python k0ur1i.py --shodan
Scan with Nuclei:

python k0ur1i.py --target "http://example.com" --nuclei
Automatically exploit vulnerabilities:

python k0ur1i.py --target "http://example.com" --exploit
Import and run a custom exploit script:

python k0ur1i.py --target "http://example.com" --import-exploit "/path/to/exploit.py"


Example Exploit Script
Here’s an example of a custom exploit script that can be imported and executed:

def run_exploit(target):
    print(f"Running custom exploit on {target}")
    # Add exploit logic here
    response = requests.get(f"{target}/vulnerable_endpoint")
    if response.status_code == 200:
        print(f"Exploit succeeded! Response: {response.text}")
    else:
        print("Exploit failed.")






        
Ethical Usage
This tool is intended for ethical and authorized testing only. Unauthorized testing or exploitation is illegal. Use this tool only on systems you own or have explicit permission to test.






License
This project is licensed under the MIT License.

Author
created by k0ur1iTN

GitHub
LinkedIn
Save this as README.md in your repository's root. Would you like to add badges, screenshots, or other GitHub-specific elements?






