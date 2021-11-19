# Download Osu players most played songs

## What you'll need

### This git repository
* Download in the top right as a zip file, or type the git clone url in the same place into your powershell/cmd .
### Osu players ID
* Go to their (or your own) profile and in the URL, take the number
### Number of songs you want to download from their top songs
* Self explanatory
### Python 3
* https://www.python.org/downloads/
### requests library
* Once python is installed, open powershell and type: `pip install requests`

## I'm ready
* Run python script in powershell/cmd by changing to that directory and typing `python .\OsuDownloader.py`
* Enter everything you got ready earlier, it should download the songs into the directory `.\songs\`

## What does it look like?
The output should look something like this as it downloads the songs:

```
There will be a 2 second delay between each download to prevent error for too many requests

-------362718-------
https://beatconnect.io/b/362718/
ssibal download joong: 1. IM A BELIEVER

-------264819-------
https://beatconnect.io/b/264819/
ssibal download joong: 2. Chameleon Love  feat.Kano

-------147177-------
https://beatconnect.io/b/147177/
ssibal download joong: 3. Idola no Circus

-------104801-------
https://beatconnect.io/b/104801/
ssibal download joong: 4. Zetsubousei Hero Chiryouyaku (TV Size)

-------264819-------
https://beatconnect.io/b/264819/
ssibal download joong: 5. Chameleon Love  feat.Kano

-------147962-------
https://beatconnect.io/b/147962/
ssibal download joong: 6. Omega Rhythm
```
