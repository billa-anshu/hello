try:
    import tkinter
    tkinter._test()
except ImportError:
    print("Tkinter is not installed")
