# REST API for Wikipedia
## Summary
This API is used for getting quick summaries of Wikipedia articles. It uses Flask to simulate the server-client interface. The Wikipedia API is managed by [wikipedia](https://github.com/goldsmith/Wikipedia). Kudos to [goldsmith](https://github.com/goldsmith).

## Usage
**- Always remember to [run](https://www.freecodecamp.org/news/how-to-setup-virtual-environments-in-python/) Python scripts in a virtual environment.**
- Navigate to the folder where you have cloned the repository.
- Download app requirements: `$ pip install -r requirements.txt`.
- Run the Flask server: `$ python3 app.py` (On Windows, run PowerShell as admin or use `$ Set-ExecutionPolicy -Scope CurrentUser Unrestricted`).
### Linux
- After that, you are ready to test the API in your terminal or browser. In your terminal, you can use the command `curl`.
  - The structure of the URL is `curl <URL address of your Flask server>/wiki/<search_term>`.
  - Optionally, you can specify from which language you want to get results via the [language code](https://en.wikipedia.org/wiki/List_of_ISO_639_language_codes) using `$ curl <IP address of your Flask server>/wiki/<search_term>?Accept-Language="<symbol for your language>"`. Without this argument, the API will automatically search the Czech Wikipedia.
- Examples:
  - `$ curl http://127.0.0.1:5000/wiki/rum`
  - `$ curl http://127.0.0.1:5000/wiki/vodka?Accept-Language="en"`
  - `$ curl http://127.0.0.1:5000/wiki/"Vin rosé"?Accept-Language="fr"`
### Windows
- After that, you are ready to test the API in your terminal or browser. In your terminal, you can use `Invoke-WebRequest`.
  - The structure of the URL is `$ Invoke-WebRequest -URI <URL address of your Flask server>/wiki/<search_term> | Select-Object -Expand Content`.
  - Optionally, you can specify from which language you want to get results via the [language code](https://en.wikipedia.org/wiki/List_of_ISO_639_language_codes) using `$ Invoke-WebRequest -URI <IP address of your Flask server>/wiki/<search_term>?Accept-Language="<symbol for your language>" | Select-Object -Expand Content`. Without this argument, the API will automatically search the Czech Wikipedia.
- Examples:
  - `$ Invoke-WebRequest -URI http://127.0.0.1:5000/wiki/rum | Select-Object -Expand Content`
  - `$ Invoke-WebRequest -URI http://127.0.0.1:5000/wiki/vodka?Accept-Language="en" | Select-Object -Expand Content`
  - `$ Invoke-WebRequest -URI http://127.0.0.1:5000/wiki/"Vin rosé"?Accept-Language="fr" | Select-Object -Expand Content`
## Installation
### Linux
- Python3
  - Check if you have Python3 installed:
    - `$ python3 --version`
  - Download Python3 via the repository:
    - Debian/Ubuntu-based:
      - `$ sudo apt-get update`
      - `$ sudo apt-get install python3`
    - Fedora:
      - `$ sudo dnf install python3`
    - Arch:
      - `$ sudo pacman -Syu`
      - `$ sudo pacman -Sy python-pip`
  - Download pip:
    - Debian/Ubuntu-based:
      - `$ sudo apt-get install python-pip`
    - Fedora:
      - `$ sudo dnf install python3-pip`
    - Arch:
      - `$ sudo pacman -Sy python-pip`
- Clone the repository:
  - Check if you have Git installed: `$ git --version` ([installing Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git))
  - Navigate to the folder where you want to download the repository.
  - `$ git clone https://github.com/TMLowKey/wiki-API.git`
### Windows 10/11 (PowerShell)
- Python3
  - Check if you have Python3 installed by running `$ python --version` in PowerShell.
  - Download Python3 via the official [website](https://www.python.org/downloads/windows/).
- Clone the repository:
  - Check if you have Git installed: `$ git --version` ([installing Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git))
  - Navigate to the folder where you want to download the repository.
  - `$ git clone https://github.com/TMLowKey/wiki-API.git`
## Unit Test
- To run tests, you can use `$ python -m unittest test.py`.
