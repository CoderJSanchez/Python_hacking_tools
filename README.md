# Python Hacking Tools

## scan_ssh_keys.py

### Description

`scan_ssh_keys.py` is a Python script designed to scan your system for files containing SSH key-related terms. This tool is useful for quickly identifying files that may contain SSH keys or related information, aiding in security assessments and audits.

### Features

- Scans the entire file system for files containing SSH key-related terms.
- Outputs the paths of relevant files.

### Prerequisites

- Python 3.x
- Required permissions to read files on the system (may need to run as root for comprehensive scanning).

### Usage

1. **Clone the repository:**

    ```bash
    git clone https://github.com/CoderJSanchez/Python_hacking_tools.git
    cd Python_hacking_tools
    ```

2. **Run the script:**

    ```bash
    python3 scan_ssh_keys.py /path/to/scan
    ```

    You may need to use `sudo` to ensure the script has the necessary permissions:

    ```bash
    sudo python3 scan_ssh_keys.py
    ```

### Example

```bash
$ sudo python3 scan_ssh_keys.py /path/to/scan
Scanning for files containing SSH key-related terms...
Found: /home/user/.ssh/id_rsa
Found: /etc/ssh/ssh_config
...
