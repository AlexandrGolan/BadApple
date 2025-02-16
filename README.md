# Bad Apple v.1.1.0 (Alpha)

Bad Apple is a utility for managing Wi-Fi networks using `hostapd`, as well as retrieving device information and public IP.

## Key Features:
- **mknetwork `<SSID>`**: Create a Wi-Fi network with the specified SSID.
- **rmnetwork `<SSID>`**: Remove the Wi-Fi network with the specified SSID.
- **setpass `<PASSWORD>` `<SSID>`**: Set a password for the Wi-Fi network.
- **rmpass `<SSID>`**: Remove the password for the Wi-Fi network.
- **getinfo**: Display device information (OS, model, username, public IP).
- **BadAppleSong**: Open the "Bad Apple" song on YouTube.
- **exit**: Exit the application.

## Requirements:
- Python 3.x
- Modules: `requests`, `termcolor`
- `hostapd` installed on the system (for Wi-Fi network management)

## Installation:
1. Clone the repository:
    ```bash
    git clone <https://github.com/AlexandrGolan/BadApple>
    cd BadApple
    ```
2. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage:
```bash
sudo python3 BadApple.py
