import re
import sys
from pathlib import Path


def browse_catalogue(path: str | Path) -> None:
    path = Path(path)
    text = path.read_text(encoding='utf-8')
    domains = re.findall(r'##\s*(\d{2,}_\w+)', text)
    print("Top-Level Domains Found:")
    for domain in domains:
        print(f"- {domain}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python catalogue.py <module_catalogue.md>")
    else:
        browse_catalogue(sys.argv[1])
