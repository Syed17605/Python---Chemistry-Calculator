from nicegui import ui

from display import Display


# Runs the code
if __name__ in {'__main__', '__mp_main__'}:
    display = Display()
    ui.run()