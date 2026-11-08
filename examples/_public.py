"""Small public-data HTTP helper. No credentials or local response archive."""
import json
import subprocess
from urllib.parse import urlencode

BASE = "https://withpanta.com"

def get(path, params=None):
    url = BASE + path + ("?" + urlencode(params) if params else "")
    result = subprocess.run(
        ["curl", "--fail-with-body", "--silent", "--show-error", "--max-time", "30", url],
        capture_output=True, text=True, check=False,
    )
    if result.returncode:
        raise SystemExit("Public request failed; inspect service status/rate limits before retrying. " + result.stderr.strip())
    return json.loads(result.stdout)
