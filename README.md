# Clash of Clans Auto-Match Bot

This Python script uses OCR (Optical Character Recognition) to extract text from a portion of the Clash of Clans screen, and performs automatic clicks based on the extracted text value. The script uses the `easyocr` and `cv2` libraries for OCR and image processing, and the `subprocess` library for interacting with the Android device via ADB.

## Requirements

- Python 3.6 or higher
- `easyocr` library
- `cv2` library
- Android device with Clash of Clans installed and ADB enabled
- USB cable to connect Android device

## Installation

To install COCAutoMatch, you need to have Python 3.6 or higher and pip installed on your system. Then, follow these steps:

1. Clone this repository or download the zip file.
2. Navigate to the project folder and run `pip install -r requirements.txt` to install the dependencies.
3. Run `python main.py` to start the bot.


## Usage

1. Connect your Android device to your computer via USB cable.
2. Enable ADB on your Android device.
3. Clone or download the repository from GitHub.
4. Install the `easyocr` and `cv2` libraries using `pip`.
5. Run the `COCAutoMatch.py` script using the command `python COCAutoMatch.py`.
6. Enter the IP address of your Android device when prompted.
7. The script will start scanning the Clash of Clans screen for the text values and performing automatic clicks as needed.

Note: This script is intended for educational purposes only and should not be used to gain an unfair advantage in Clash of Clans or any other game. Use at your own risk.



## License

COCAutoMatch is licensed under the MIT License. See [LICENSE](LICENSE) for more details.
