
# **Steps**
## **Step 1. System requirements (Skip to step 2 if you already have the right requirements)**

### Linux (Ubuntu or Debian-based systems): 

*Install Python*
```bash
sudo apt update
sudo apt install python3
```
*Install pip*
```bash
sudo apt install python3-pip
```
*Install pytube & ffmpeg*
```bash
sudo apt install ffmpeg
pip install pytube
```
*Install git*
```bash
sudo apt install git
```

### MacOS (Intel or Apple silicon):

*Install brew*
```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```
*Install Python*
```bash
brew install python3
```
*Install pip*
```bash
python3 -m ensurepip
```
*Install pytube & ffmpeg*
```bash
brew install ffmpeg
pip install pytube
```
*Install git*
```bash
brew install git
```

## **Step 2. Clone the files and select your path**
```bash
git clone https://github.com/westag/Clips-Generator
cd YOURPATH
```

## **Step 3. Edit the directories (File locations)**

Open clipgen.py then edit every variable where it says 'Set', but don't edit any other code if you don't know what you're doing. (I recommend you to create different folders so you don't get confused but you can choose not to)

## **Step 4. Run it and enjoy**
```bash
python3 clipgen.py
```
Once you run it, you'll get asked to enter a YouTube url, make sure you write the full url and not the shorten one. Once you wrote it, press enter and wait for the code to do its work.
