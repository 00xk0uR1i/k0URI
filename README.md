<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>WP Exploit Scanner</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
            margin: 20px;
        }
        h1, h2, h3 {
            color: #2c3e50;
        }
        code {
            background-color: #f4f4f4;
            padding: 4px;
            border-radius: 4px;
            font-family: monospace;
        }
        pre {
            background-color: #f4f4f4;
            padding: 10px;
            border-radius: 4px;
            overflow-x: auto;
        }
        a {
            color: #3498db;
            text-decoration: none;
        }
        a:hover {
            text-decoration: underline;
        }
        .code-block {
            background-color: #272822;
            color: #f8f8f2;
            padding: 10px;
            border-radius: 5px;
            overflow-x: auto;
        }
        .note {
            color: #e74c3c;
            font-weight: bold;
        }
    </style>
</head>
<body>
    <h1>WP Exploit Scanner</h1>
    <p>
        <strong>WP Exploit Scanner</strong> is a multi-functional tool for scanning, detecting, and exploiting vulnerabilities in WordPress websites. It integrates multiple features such as Shodan and ZoomEye queries, Nuclei scanning, and auto-exploitation. Additionally, it allows users to import custom Python exploit scripts for dynamic execution.
    </p>

    <h2>Features</h2>
    <ul>
        <li><strong>WordPress Vulnerability Scanning:</strong> Detect vulnerabilities in WordPress sites using APIs and known methods.</li>
        <li><strong>Shodan Integration:</strong> Search for WordPress-related systems using the Shodan API.</li>
        <li><strong>ZoomEye Integration:</strong> Query ZoomEye for WordPress-related systems.</li>
        <li><strong>Nuclei Scanning:</strong> Use Nuclei templates to scan for CVEs, misconfigurations, and WordPress-specific issues.</li>
        <li><strong>Auto-Exploitation:</strong> Exploit known vulnerabilities automatically.</li>
        <li><strong>Custom Exploit Import:</strong> Import and execute Python-based exploit scripts dynamically.</li>
    </ul>

    <h2>Requirements</h2>
    <h3>Python Dependencies</h3>
    <pre><code>pip install requests pyfiglet rich shodan</code></pre>

    <h3>Additional Tools</h3>
    <ul>
        <li><a href="https://developer.shodan.io/" target="_blank">Shodan API Key</a></li>
        <li><a href="https://www.zoomeye.org/" target="_blank">ZoomEye API Key</a></li>
        <li><a href="https://github.com/projectdiscovery/nuclei" target="_blank">Nuclei</a>: Download and install Nuclei, and configure the <code>NUCLEI_PATH</code> and <code>NUCLEI_TEMPLATES</code> variables in the script.</li>
    </ul>

    <h2>Installation</h2>
    <ol>
        <li>Clone the repository:
            <pre><code>git clone https://github.com/yourusername/wp-exploit-scanner.git
cd wp-exploit-scanner</code></pre>
        </li>
        <li>Configure the script:
            <ul>
                <li>Add your Shodan API key:
                    <pre><code>SHODAN_API_KEY = "your_shodan_api_key"</code></pre>
                </li>
                <li>Add your ZoomEye API key (if applicable).</li>
                <li>Configure the Nuclei path and templates.</li>
            </ul>
        </li>
        <li>Run the script:
            <pre><code>python scanner.py --help</code></pre>
        </li>
    </ol>

    <h2>Usage</h2>
    <h3>General Syntax</h3>
    <pre><code>python scanner.py [OPTIONS]</code></pre>

    <h3>Options</h3>
    <ul>
        <li><code>--target</code>: Specify the target WordPress site URL.</li>
        <li><code>--shodan</code>: Perform a Shodan search for WordPress-related systems.</li>
        <li><code>--zoomeye</code>: Perform a ZoomEye search for WordPress-related systems.</li>
        <li><code>--nuclei</code>: Scan the target with Nuclei.</li>
        <li><code>--exploit</code>: Attempt to auto-exploit known vulnerabilities.</li>
        <li><code>--import-exploit</code>: Import and execute a custom Python exploit script.</li>
    </ul>

    <h3>Examples</h3>
    <ul>
        <li>Scan a WordPress site for vulnerabilities:
            <pre><code>python scanner.py --target "http://example.com"</code></pre>
        </li>
        <li>Perform a Shodan search for WordPress sites:
            <pre><code>python scanner.py --shodan</code></pre>
        </li>
        <li>Scan with Nuclei:
            <pre><code>python scanner.py --target "http://example.com" --nuclei</code></pre>
        </li>
        <li>Automatically exploit vulnerabilities:
            <pre><code>python scanner.py --target "http://example.com" --exploit</code></pre>
        </li>
        <li>Import and run a custom exploit script:
            <pre><code>python scanner.py --target "http://example.com" --import-exploit "/path/to/exploit.py"</code></pre>
        </li>
    </ul>

    <h2>Example Exploit Script</h2>
    <pre><code>def run_exploit(target):
    print(f"Running custom exploit on {target}")
    response = requests.get(f"{target}/vulnerable_endpoint")
    if response.status_code == 200:
        print(f"Exploit succeeded! Response: {response.text}")
    else:
        print("Exploit failed.")</code></pre>

    <h2>Ethical Usage</h2>
    <p class="note">
        This tool is intended for ethical use only. Unauthorized testing or exploitation is <strong>illegal</strong> and may result in severe consequences. Use it only on systems you own or have explicit permission to test.
    </p>

    <h2>License</h2>
    <p>This project is licensed under the <a href="LICENSE">MIT License</a>.</p>

    <h2>Author</h2>
    <p>
        <strong>Your Name Here</strong><br>
        <a href="https://github.com/yourusername" target="_blank">GitHub</a> | 
        <a href="https://linkedin.com/in/yourprofile" target="_blank">LinkedIn</a>
    </p>
</body>
</html>
