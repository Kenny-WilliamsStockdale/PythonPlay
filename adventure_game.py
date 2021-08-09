# Start adventure at the forest - can go left to the mountain or right to the castle. Which way do you want to go?
# variable choice 
# if choice is = input something
# elif the other choice
#print final outcome for choices

import PySimpleGUI as sg
"""
    Demo - 2 simultaneous windows using read_all_window

    Window 1 launches window 2
    BOTH remain active in parallel

    Both windows have buttons to launch popups.  The popups are "modal" and thus no other windows will be active

    Copyright 2020 PySimpleGUI.org
"""

def make_win1():
    layout = [[sg.Text('You start your adventure in the forest.\nYou need to get home and it will be dark soon,\ndo you go left to the mountain pass or right to the castle?'), sg.Text('      ', k='-OUTPUT-')],
              [sg.Button('Left'), sg.Button('Right'), sg.Button('End')]]
    return sg.Window('Window Title', layout, finalize=True)


def make_win2():
    layout = [[sg.Text('You end up at the mountian pass. Do you take the path or the off beaten track?')],
              [sg.Button('Path'), sg.Button('Track'), sg.Button('End')]]
    return sg.Window('Second Window', layout, finalize=True)

def make_win3():
    layout = [[sg.Text('Arriving at the castle you are greeted warmly by some friends.\nDo you spend the night or say you must be on your way home?')],
              [sg.Button('Go'), sg.Button('Stay'), sg.Button('End')]]
    return sg.Window('Second Window', layout, finalize=True)

def make_win4():
    layout = [[sg.Text('You feel tired after the long trek but you make it home just in time for dinner.')],
              [sg.Button('End')]]
    return sg.Window('Second Window', layout, finalize=True)

def make_win5():
    layout = [[sg.Text('You end up falling off the mountain to your death.')],
              [sg.Button('End')]]
    return sg.Window('Second Window', layout, finalize=True)

def make_win6():
    layout = [[sg.Text('You get lost on your way and with it getting dark you fear you will never make it home.')],
              [sg.Button('End')]]
    return sg.Window('Second Window', layout, finalize=True)

def make_win6():
    layout = [[sg.Text('You spend a joyous night with your friends. In the morning they offer to give a ride in the carriage home.')],
              [sg.Button('End')]]
    return sg.Window('Second Window', layout, finalize=True)

window1, window2 = make_win1(), None 
window3 = None
window4 = None 
# start off with 1 window open
while True:             # Event Loop
    window, event, values = sg.read_all_windows()
    if event == sg.WIN_CLOSED or event == 'End':
        window.close()
        if window == window2:       # if closing win 2, mark as closed
            window2 = None
        elif window == window1:     # if closing win 1, exit program
            break
        
    elif event == 'Left' and not window2:
        window2 = make_win2()
        window = window.close()
    elif event == 'Right' and not window2:
        window2 = make_win3()
        window = window.close()
    elif event == 'Path' and not window3:
        window3 = make_win4()
        window2 = window.close()
    elif event == 'Track' and not window3:
        window3 = make_win5()
        window2 = window.close()
    elif event == 'Go' and not window4:
        window4 = make_win6()
        window2 = window.close()
    elif event == 'Stay' and not window4:
        window4 = make_win6()
        window2 = window.close()
window.close()


def story() :
 
    choice1 = input('You start your adventure in the forest. You need to get home and it will be dark soon, do you go left to the mountain pass or right to the castle? \n Choose Left or Right')   
    if choice1 == ('Left') : 
           choice2 = input('You end up at the mountian pass. Do you take the path or the off beaten track? \n Path / Track')
           if choice2 == ('Track'): 
            print('You end up falling off the mountain to your death.') 
           elif choice2 == ('Path'):
               print('You feel tired after the long trek but you make it home just in time for dinner.') 
    elif choice1 == ('Right'):
            choice3 = input('Arriving at the castle you are greeted warmly by some friends. Do you spend the night or say you must be on your way home? \n Stay / Go')
            if choice3 == ('Go'):
                print('You get lost on your way and with it getting dark you fear you will never make it home.')
            elif choice3 ==('Stay'):
                print('You spend a joyous night with your friends. In the morning they offer to give a ride in the carriage home.')

if __name__ == "__main__":
    #  story()
    make_win1()
    make_win2()