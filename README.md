WP Exploit Scanner by k0ur1i
WP Exploit Scanner is a comprehensive tool for scanning, detecting, and exploiting vulnerabilities in WordPress websites. It integrates multiple functionalities, including Shodan and ZoomEye searches, Nuclei scanning, auto-exploitation, and the ability to import custom exploit scripts.



Requirements :
Python Dependencies :
- Install the necessary Python libraries:

- pip install requests pyfiglet rich shodan
- Additional Tools
Shodan API Key
ZoomEye API Key
Nuclei:
Install Nuclei and configure its path in the script.



- Installation
- Clone the repository:

git clone https://github.com/00xk0uR1i/k0URI.git


- Run the script:

- python k0ur1i.py --help
Usage
- General Syntax
- python k0ur1i.py [OPTIONS]
Options
--target: Specify the target WordPress site URL.
--shodan: Perform a Shodan search for WordPress-related systems.
--zoomeye: Perform a ZoomEye search for WordPress-related systems.
--nuclei: Scan the target with Nuclei.
--exploit: Attempt to auto-exploit known vulnerabilities.
--import-exploit: Import and execute a custom Python exploit script.


- Examples:
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

       
Ethical Usage
This tool is intended for ethical and authorized testing only. Unauthorized testing or exploitation is illegal. Use this tool only on systems you own or have explicit permission to test.






License
This project is licensed under the MIT License.

Author
created by k0ur1iTN

GitHub
LinkedIn





