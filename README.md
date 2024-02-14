# REST API for wikipedia
## Summary
This API is used for GETing quick summary of Wikipedia article. Using Flask for simulating server-client interface. Wikipedia API is managed by [wikipedia][https://github.com/goldsmith/Wikipedia] kuddos to [goldsmith][https://github.com/goldsmith].

## Usage
## Installation
### Linux
- Python3
  - Check if you have python3 installed
    - ```$ python3 --version ```
  - Download python3 via repository
    -  Debian/Ubuntu based
      -  ```$ sudo apt-get update```
      -  ```$ sudo apt-get install python3```
    -  Fedora
      -  ```$ sudo dnf install python3```
    -  Arch
      -  ```$ sudo pacman -Syu```
      -  ```$ sudo pacman -Sy python-pip```
  -  Download pip
    -  Debian/Ubuntu based
      -  ```$ sudo apt-get install python-pip```
    -  Fedora
      -  ```$ sudo dnf install python3-pip```
    -  Arch
      -  ```$ sudo pacman -Sy python-pip```
- Clone repository
  -  Check if you have git ```$ git --version``` [installing git][https://git-scm.com/book/en/v2/Getting-Started-Installing-Git]
  -  Navigate in folder where you want to download repository
  -  ```$ git clone https://github.com/TMLowKey/wiki-API.git```
### Windows 10/11 (powershell)
- Python3
  -  Check if you have Python3 installed by running ```$ python --version``` in PowerShell.
  -  Download python3 via offical [website][https://www.python.org/downloads/windows/]
- Clone repository
  -  Check if you have git ```$ git --version``` [installing git][https://git-scm.com/book/en/v2/Getting-Started-Installing-Git]
  -  Navigate in folder where you want to download repository
  -  ```$ git clone https://github.com/TMLowKey/wiki-API.git```
## Usage
**- Remember always [run][https://www.freecodecamp.org/news/how-to-setup-virtual-environments-in-python/] python script in virtual enviroment**
- Navigate in folder where you have cloned repository
- Download app requirements ```$ pip install -r requirements.txt```$
- Run flask server ```$ python3 app.py``` (on windows run Powershell as admin or use ```$ Set-ExecutionPolicy -Scope CurrentUser Unrestricted```
### Linux
- After that you are ready to test api in your terminal or browser, in your terminal you can command curl
  - Structure of url is ```curl <url address of your flask server>/wiki/<search_term>``` 
  - Optionaly you can add specify from which language you want to get results via [language code][https://en.wikipedia.org/wiki/List_of_ISO_639_language_codes] ```$ curl <IP address of your flask server>/wiki/<search_term>?Accept-Language="<symbol for your language>``` without this argument API will automaticly search on czech wiki.
- Examples 
  - ```$ curl http://127.0.0.1:5000/wiki/rum```
  - ```$ curl http://127.0.0.1:5000/wiki/vodka?Accept-Language="en"```
  - ```$ curl http://127.0.0.1:5000/wiki/"Vin rosé"?Accept-Language="fr"```
### Windows
- After that you are ready to test api in your terminal or browser, in your terminal you can command Invoke-WebRequest
  - Structure of url is ```$ Invoke-WebRequest -URI <url address of your flask server>/wiki/<search_term> | Select-Object -Expand Content``` 
  - Optionaly you can add specify from which language you want to get results via [language code][https://en.wikipedia.org/wiki/List_of_ISO_639_language_codes] ```$ Invoke-WebRequest -URI <IP address of your flask server>/wiki/<search_term>?Accept-Language="<symbol for your language> | Select-Object -Expand Content``` without this argument API will automaticly search on czech wiki.
- Examples 
  - ```$ Invoke-WebRequest -URI http://127.0.0.1:5000/wiki/rum | Select-Object -Expand Content```
  - ```$ Invoke-WebRequest -URI http://127.0.0.1:5000/wiki/vodka?Accept-Language="en" | Select-Object -Expand Content```
  - ```$ Invoke-WebRequest -URI http://127.0.0.1:5000/wiki/"Vin rosé"?Accept-Language="fr" | Select-Object -Expand Content```
  - 

## Unit test
- for running test you can use ```python -m unittest test.py```
