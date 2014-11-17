1) Create a python installer in Windows


We will use pyinstaller, to install execute the next command
    prompt> pip install pyinstaller

2) Please install pywin32
    a) Download correct pywin32 depening on your python installation:
            http://sourceforge.net/projects/pywin32/files/pywin32/Build%20219/

        Check your python version and arch.

    b) Execute downloaded file


3) Once dependencies are installed, execute the next command:

    a) prompt> pyinstaller gui.py


    If you get the next error:
        Error loading Python DLL: C:\Users\Uyuni\GOOGLE~1\GitHub\proyecto-final-fundamentos\build\gui\python27.dll (error code 126)

    Please execute the previous command in an administrator command line.

