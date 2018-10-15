import cx_Freeze
import os

os.environ['TCL_LIBRARY'] = r'C:\Users\Admin\AppData\Local\Programs\Python\Python36-32\tcl\tcl8.6'
os.environ['TK_LIBRARY'] = r'C:\Users\Admin\AppData\Local\Programs\Python\Python36-32\tcl\tk8.6'


executables = [cx_Freeze.Executable("MainGame.py")]

cx_Freeze.setup(
    name="Dodge The Missiles",
    options={"build_exe": {"packages":["pygame","random","sys"],
                           "include_files":["gameover.wav","crash.wav","rocket.wav","intro.wav","boom.png","Car2.png","rocket.png","bg.jpg","bg1.jpg","exit.jpg","Car.png","obstacle2.png","hello.otf"]}},
    executables = executables

    )
