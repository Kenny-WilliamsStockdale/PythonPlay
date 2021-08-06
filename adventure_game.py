# Start adventure at the forest - can go left to the mountain or right to the castle. Which way do you want to go?
# variable choice 
# if choice is = something
# else the other choice
def story() :
 
    choice1 = input('You start your adventure in the forest. You need to get home and it will be dark soon, do you go left to the mountain pass or right to the castle? \n Choose Left or Right')   
    if choice1 == ('Left') : 
           choice2 = input('You end up at the mountian pass. Do you take the path or the off beaten track? \n Path / Track')
           if choice2 == ('Track'): 
            print('You end up falling off the mountain to your death.') 
           elif choice2 == ('Path'):
               print('You feel tired after the long trek but you make it home just in time for dinner.') 
    elif choice1 == ('Right'):
            choice3 = input('Arriving at the castle you are greeted warmly by some friends. Do you spend the night or say you must be on your way? \n Stay / Go')
            if choice3 == ('Go'):
                print('You get lost on your way and with it getting dark you fear you will never make it home.')
            elif choice3 ==('Stay'):
                print('You spend a joyness night with your friends. In the morning they offer to give a ride in the carriage home.')

if __name__ == "__main__":
    story()