# showmap.py - Open a map in the browser using command-line input or clipboard text.

import webbrowser
import sys
import pyperclip
import urllib.parse

def get_address():
    """Return the address from the command line or clipboard."""
    if len(sys.argv) > 1:
        return ' '.join(sys.argv[1:]).strip()
    return pyperclip.paste().strip()

def main():
    address = get_address()
    if not address:
        print("No address provided or found in clipboard.")
        return

    encoded_address = urllib.parse.quote(address)
    url = f"https://www.openstreetmap.org/search?query={encoded_address}"
    webbrowser.open(url)

if __name__ == "__main__":
    main()

