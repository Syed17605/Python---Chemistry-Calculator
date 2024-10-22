from nicegui import ui
from display import Display

# Required by niceGUI
# __mp_main__ is from multiprocesor coding
if __name__ in {'__main__', '__mp_main__'}:
    display = Display()
    ui.run()