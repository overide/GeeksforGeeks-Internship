# Certificate Generator
This Script will take a xlsx sheet and extract the names from the target column and generate the certificates for those name using provided certificate template

## Project Structure
* **Assets**: This folder can contain certificate template, font file(in .ttf format), excel sheet of names and any other file. It's not necessary though, you can place files anywhere you want but make sure to set file paths in setting.py

* **Certificates**: This folder holds generated certificate (on sample is already there). You can choose different location also, just add the path to new location in setting.py

* **settings.py**: Use this file for configuring your settings like - 
  * Font size
  * Font color
  * Text template
  * Line spacing
  * Column to extract
  * Path to font file
  * Path to image template
  * Path to xlsx file
  * Path to target folder etc.

## Usages
This script depends on few 3rd party libraries, so first install them -
```
$ pip install -r requirments.txt
```
After configuring *settings.py*, execute *generate_certificate.py* like this-
```
$ python generate_certificate.py
```
## Note
It is assumed that - 
* Columns in excel sheet are zero indexed (0..n)
* Columns have headers, so for example name column have **Names** colum header, thus it is omitted by script.
