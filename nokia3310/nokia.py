def main_menu(): # main menu
    print("-----------------------------")
    print("----Welcome to nokia menu----")
    print("-----------------------------")
    print("1. Phone book")
    print("2. Messages")
    print("3. Chat")
    print("4. Call register")
    print("5. Tones")
    print("6. Settings")
    print("7. Call divert")
    print("8. Games")
    print("9. Calculator")
    print("10. Reminder")    
    print("11. Clock")
    print("12. Profiles")
    print("13. SIM services")
    print("0. Power Off")
    
###############################################################################

def phone_book(): # case 1 of main menu
    print("-----------------------------")
    print("Phone Book")
    print("-----------------------------")
    print("1. Search")
    print("2. Service No")
    print("3. Add name")	
    print("4. Erase")
    print("5. Edit")
    print("6. Assign tone")
    print("7. Send b'card")
    print("8. Options")
    print("9. Speed dials")
    print("10. Voice tags")
    print("0. Back") 
    
def options(): # case 8 for phone book 
    print("-----------------------------")
    print("Options")
    print("-----------------------------")
    print("1. Type of view")
    print("2. Memory status")
    print("0. Back")

###############################################################################

def messages(): #case 2 of main menu
    print("Messages")
    print("1. Write messages")
    print("2. Inbox")
    print("3. Outbox")
    print("4. Picture messages")
    print("5. Templates")
    print("6. Smileys")
    print("7. Message settings")
    print("8. Info service")
    print("9. Voice service")
    print("10. Service command editor")
    print("0. Back")
    
def message_setting(): # case 7 of messages
    print("Message settings")
    print("1.Set 1")
    print("2.Common")
    print("0. Back")
    
def set_one(): # case 1 for message setting
    print("Set 1")
    print("1.Message centre number")
    print("2.Messages sent as")
    print("3. Message validity")
    print("0. Back")   
    
def common(): # case 2 for message setting
    print("Common")
    print("1.Delivery reports")
    print("2.Reply via same centre")
    print("3. Character support")
    print("0. Back")  
    
###############################################################################

def chat(): # case 3 of main menu
    print("Chat")
    print("0. Back")
    
###############################################################################

def call_register(): # case 4 of main menu
    print("Call Register")
    print("1. Missed calls")
    print("2. Received calls")
    print("3. Dialed numbers")
    print("4. Erase recent call list")
    print("5. Show call duration")
    print("6. Show call costs")
    print("7. Call cost settings")
    print("8. Prepaid credit")
    print("0. Back")

def show_call_duration(): # case 5 of call register
    print("Show call duration")
    print("1. Last call")
    print("2. All calls")
    print("3. Received")
    print("4. Dialled")
    print("5. Clear timers")
    print("0. Back")
    
def show_call_costs(): # case 6 of call register
    print("Show call costs")
    print("1. Last cost")
    print("2. All cost")
    print("3. Clear counters")
    print("0. Back")
    
def call_cost_setting(): # case 7 of call register
    print("Call cost settings")
    print("1. Call cost limit")
    print("2. Show costs in")
    print("0. Back")
    
###############################################################################
    
def tones(): # case 5 of main menu
    print("Tones")
    print("1. Ringing tone")
    print("2. Ringing volume")
    print("3. Incoming call alert")
    print("4. Composer")
    print("5. Message alert tone")
    print("6. Keypad tones")
    print("7. Warning and game tones")
    print("8. Vibrating alert")
    print("9. Screen saver")
    print("0. Back")
    
###############################################################################

def settings(): # case 6 of main menu
    print("Settings")
    print("1. Call settings")
    print("2. Phone settings")
    print("3. Security settings")
    print("4. Restore factory settings")
    print("0. Back")
    
def call_settings(): # case 1 for settings
    print("Call settings")
    print("1. Redial")
    print("2. Speed dial")
    print("3. Call waiting")
    print("4. Own number")
    print("5. Line use")
    print("6. Auto answer")
    print("0. Back")
    
def phone_settings(): # case 2 for settings
    print("Phone settings")
    print("1. Language")
    print("2. Cell info")
    print("3. Welcome note")
    print("4. Network selection")
    print("5. Lights")
    print("6. Confirm SIM actions")
    print("0. Back")
    
def security_settings(): # case 3 for settings
    print("security settings")
    print("1. PIN code request")
    print("2. Call barring service")
    print("3. Fixed dialing")
    print("4. Closed user group")
    print("5. Phone security")
    print("6. Change access codes")
    print("0. Back")
    
###############################################################################

def call_divert(): # case 7 of main menu
    print("Call divert")
    print("0. Back")
    
###############################################################################
    
def games(): # case 8 of main menu
    print("games")
    print("0. Back")
    
###############################################################################
    
def calculator(): # case 9 for main menu
    print("Calculator")
    print("0. Back")
    
###############################################################################

def reminder(): # case 10 for main menu
    print("Reminder")
    print("0. Back")

###############################################################################

def clock(): # case 11 for main menu
    print("Clock")
    print("1. Alarm clock")
    print("2. Clock settings")
    print("3. Date settings")
    print("4. Stopwatch")
    print("5. Countdown timer")
    print("6. Auto update")
    print("0. Back")
    
###############################################################################
    
def profiles(): # case 12 for main menu
    print("Profiles")
    print("0. Back")
    
###############################################################################
    
def sim_service(): # case 13 for main menu
    print("SIM services")
    print("0. Back")






while True:
    main_menu()
    menu_option = int(input("Select an option from main menu: "))

    match menu_option:
        case 1:
            while True: 
                phone_book()
                phone_book_option = int(input("Select an option from phone book: "))
                
                match phone_book_option:
                    case 8:
                        while True:
                            options()
                            options_option = int(input("Select from options: "))
                            if options_option == 0:
                                break 
                    case 0:
                        break 
                    case _:
                        print("No current available input")

        case 2:
            messages()
            
        case 3:
            messages()
            
        case 4:
            call_register()
            
        case 5:
            tones()
            
        case 6:
            settings()
            
        case 7:
            call_divert()
            
        case 8:
            games()
            
        case 9:
            calculator()
            
        case 10:
            reminder()
            
        case 11:
            clock()
            
        case 12:
            profiles()
            
        case 13:
            sim_service()
        
                    
        case 0:
            break
            
        case _:
            print("Invalid selction")

print("Power off.......")



















