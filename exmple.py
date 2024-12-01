def run_exploit(target):
    print(f"Running custom exploit on {target}")
    # Add exploit logic here (e.g., sending malicious payloads)
    response = requests.get(f"{target}/vulnerable_endpoint")
    if response.status_code == 200:
        print(f"Exploit succeeded! Response: {response.text}")
    else:
        print("Exploit failed.")
