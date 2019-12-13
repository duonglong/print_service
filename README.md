A AWSGI for printing service

**RUN**

`python PDFPrinting.py`

**BUILD TO EXE**

`python build.py`

The compiled files will be put under **./dist** directory

**CREATE INSTALLER**

- Run _installer/innosetup-5.6.1.exe_ to install Inno Setup
- Open _SetupSocker.iss_ using Inno Setup then click Run to create installer
- The installer will be put under user's **Documents** folder by default
 
 **NOTE**: Fore unknown reason pyinstaller won't consider empty folder as resource so need to add 2 followings folders to **dist/PDFPrinting** manually: **pdf** and **logs**