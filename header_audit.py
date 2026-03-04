import requests

# The target URL
URL = "http://localhost:8000"  # Cambia esto si es necesario

REQUIRED_HEADERS = {
    "X-Frame-Options": "DENY",
    "X-Content-Type-Options": "nosniff",
    "Strict-Transport-Security": "max-age=31536000; includeSubDomains",
}

def run_audit():
    try:
        response = requests.get(URL, timeout=10)
    except requests.exceptions.RequestException as e:
        print(f"Error connecting to {URL}: {e}")
        return

    print(f"Scanning {URL}")
    print(f"Status: {response.status_code}\n")

    score = 0
    max_score = len(REQUIRED_HEADERS)

    for header, _expected_value in REQUIRED_HEADERS.items():
        value = response.headers.get(header)

        if value:
            # Check if value roughly matches expectation
            print(f"[OK] {header}: {value}")
            score += 1
        else:
            print(f"[MISSING] {header}")

    print(f"\nSecurity Score: {score}/{max_score}")

if __name__ == "__main__":
    run_audit()