from nicegui import ui

"""
This is here as a very simple example of niceGUI
I will slowly convert the files to niceGUI over the next day or two, it will be pretty simple
I just wanted this here for a basic understanding of how it works
Read all the comments, specifically the last group to understand how to run the file
If you have any questions I will explain everything on wednesday or thursday
"""

# Labels are used to display text
# can either put text in the label like so or 
# use .set_text method like shown in comment
ui.label("What would you like to do?")
# ui.label().set_text("What would you like to do?")

# This is the group of buttons
# Can use either a group of buttons like so or buttons individually
# A group is all together and individually are not together
# Everything is put in order of how it should be displayed
# since I have no main function it is in order of the file
buttons = ui.button_group()

# This is a container
# I use this for displaying the text for each of the buttons when they are pressed
# As you would guess this is a column but can use row or other options
display_constainer = ui.column()

# This are functions, one for each button
# Very simple and I'll kinda rushed the names bc I didn't want to type of full names
def convert_temp():
    display_constainer.clear() # Clears the container. For this instance makes it so only one of these labels is displayed at a time

    # This is how you add something to a container or button group as shown below
    # You put whatever you want to add to the container
    with display_constainer:
        ui.label("convert Temper")

def convert_mass(): # Not commenting all these since they all the same just different label text
    display_constainer.clear()
    with display_constainer:
        ui.label("mass")

def convert_vol():
    display_constainer.clear()
    with display_constainer:
        ui.label("colume")

def convert_press():
    display_constainer.clear()
    with display_constainer:
        ui.label("pressure")

def mass_and_molar_mass():
    display_constainer.clear()
    with display_constainer:
        ui.label("MM and MAss")

def molarity():
    display_constainer.clear()
    with display_constainer:
        ui.label("Molarity Calculations")

def equation():
    display_constainer.clear()
    with display_constainer:
        ui.label("Equation Balance")



# This is how to add buttons to a button group
# This is put here but could also be put at the top where i declared it
# put here to show that only where it is declared matters
# could also do this without declaring the buttons group by saying:
# with ui.button_group:
with buttons:
    ui.button(text="Convert Temperature", on_click=convert_temp)
    ui.button(text="Convert Mass", on_click=convert_mass)
    ui.button(text="Convert Volume", on_click=convert_vol)
    ui.button(text="Convert Pressure", on_click=convert_press)
    ui.button(text="Convert Mass and Molar Mass", on_click=mass_and_molar_mass)
    ui.button(text="Molarity Calculations", on_click=molarity)
    ui.button(text="Equation Balancer", on_click=equation)

# This is a very simple example of a text box with a label as the constantly updating result
ui.input(label='Text', placeholder='start typing',
         on_change=lambda e: result.set_text('you typed: ' + e.value),
         validation={'Input too long': lambda value: len(value) < 20})
result = ui.label()


# This is what runs this file
# When run in terminal it will automatically open the website
# The qebsite constantly updates so all you have to do is save the file 
# and then go back to the website and it will be updated with whatever you changed
# This is also the last object
# Uncomment the next line and save the file if you want to see it update
# ui.label("This was commented")
ui.run()


# To end the program press ctrl+C in terminal