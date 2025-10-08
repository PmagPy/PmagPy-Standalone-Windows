## A workflow that worked on 2/16/2023 for Yiming Zhang for Windows 10

Made a new conda enviroment 

```conda create -n pmag_gui_compile python=3.9.13```

Activated that conda environment:

```conda activate pmag_gui_compile```

```conda install future matplotlib numpy scipy pandas```

- Use pip to install wxPython
  - `pip install --upgrade -f https://wxpython.org/Phoenix/snapshot-builds/ wxPython`

- Use pip to install Pyinstaller
  - `pip install git+https://github.com/pyinstaller/pyinstaller.git`

Compiled the program:

```pyinstaller pmag_gui.spec```

I used essentially the same pmag_gui.spec in the ```PmagPy``` repository to generate the executable file. Minor changes were necessary in the ```hiddenimports``` section where I had to add a few scipy modules in order for the excutable to initialize without crashing. That version of .spec file is saved here.

## A workflow that workedon 10/7/2025 for Tony Pivarunas on Windows 10

Made a new conda environment.

```C:\Users\apiv9>mamba create -n pmag_gui_compile python=3.9.13```

Activated the environment.

```C:\Users\apiv9>mamba activate pmag_gui_compile```

Used mamba to install required packages in two waves.

```(pmag_gui_compile) C:\Users\apiv9>mamba install matplotlib numpy scipy pandas```

```(pmag_gui_compile) C:\Users\apiv9>mamba install wxPython pyinstaller```

Changed into my cloned PmagPy directory

```cd developer```

```cd Pmagpy```

I used the pmag_gui.spec that is in *this* repository (NB: different than the one in the PmagPy repo).

```pyinstaller pmag_gui.spec```

And, voila. Popped up in a few minutes.