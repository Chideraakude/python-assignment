def main():
    chideraCollector = input

    menu = """
    NOKIA - TECHTRIBE EDITION

    For Phonebook - Press 1
    For Messages - Press 2
    For Chat - Press 3
    For Call Register - Press 4
    For Tones - Press 5
    For Settings - Press 6
    For Call divert - Press 7
    For Games - Press 8
    For Calculator - Press 9
    For Reminder - Press 10
    For Clock - Press 11
    For Profiles - Press 12
    For SIM Services - Press 13
    """

    print(menu)
    generalMenuChoice = chideraCollector("")

    if generalMenuChoice == "1":
        print("Phone Book")

        phoneBook = """
             Press 1 - To Search
             Press 2 - To Service Nos
             Press 3 - To Add Name
             Press 4 - To Erase
             Press 5 - To Edit
             Press 6 - To Assign Tone
             Press 7 - To Send b card
             Press 8 - Option
             Press 9 - To Speed Dail
             Press 10 -To Voice Tag
             Press 0 - To Go Back To previous Menu
        """
        print(phoneBook)
        phoneBookChoice = chideraCollector("")

        if phoneBookChoice == "1":
            print("Search")
            searchMenu = """
             Press 1 - To Search
            """
            print(searchMenu)
            searchMenuChoice = chideraCollector("")

        elif phoneBookChoice == "2":
            print("Service")
            serviceMenu = """
             Press 1 - To Service
            """
            print(serviceMenu)
            serviceMenuChoice = chideraCollector("")

        elif phoneBookChoice == "3":
            print("AddName")
            addNameMenu = """
             Press 1 - To AddName
            """
            print(addNameMenu)
            addMenuChoice = chideraCollector("")

        elif phoneBookChoice == "4":
            print("Erase")
            eraseMenu = """
             Press 1 - To Erase
            """
            print(eraseMenu)
            eraseMenuChoice = chideraCollector("")

        elif phoneBookChoice == "5":
            print("Edit")
            editMenu = """
             Press 1 - To Edit
            """
            print(editMenu)
            editMenuChoice = chideraCollector("")

        elif phoneBookChoice == "6":
            print("AssignTone")
            assignTone = """
             Press 1 - To AssignTone
            """
            print(assignTone)
            assignToneMenuChoice = chideraCollector("")

        elif phoneBookChoice == "7":
            print("SendBCard")
            sendbCard = """
             Press 1 - To SendCard
            """
            print(sendbCard)
            sendCardMenuChoice = chideraCollector("")

        elif phoneBookChoice == "8":
            print("Options")
            option = """
             Press 1 - Type of view
             Press 2 - Memory status
            """
            print(option)
            optionMenuChoice = chideraCollector("")

            if optionMenuChoice == "1":
                print("TpyeOfView")
                typeOfView = """
                 Press 1 - Type of view
                """
                print(typeOfView)
                typeOfViewMenuChoice = chideraCollector("")

            elif optionMenuChoice == "2":
                print("MemoryStatus")
                memoryStatus = """
                 Press 1 - Memory Status
                """
                print(memoryStatus)
                memoryStatusMenuChoice = chideraCollector("")

        elif phoneBookChoice == "9":
            print("SpeedDials")
            speedDials = """
             Press 1 - To SpeedDials
            """
            print(speedDials)
            speedDialsMenuChoice = chideraCollector("")

        elif phoneBookChoice == "10":
            print("VoiceTag")
            voiceTag = """
             Press 1 - To SendCard
            """
            print(voiceTag)
            voiceTagMenuChoice = chideraCollector("")

        else:
            print("Mr Man be Careful!!!")
            beCareful = """
             Press 1 - To BeCareful
            """
            print(beCareful)
            beCarefulMenuChoice = chideraCollector("")


    elif generalMenuChoice == "2":
        print("Messages")

        message = """
             Press 1 - To WriteMessage
             Press 2 - To Inbox
             Press 3 - To Outbook
             Press 4 - To Picture Messages
             Press 5 - To Template
             Press 6 - To Smileys
             Press 7 - Message Sttings
             Press 8 - Info Service
             Press 9 - Voice Mail
             Press 10 -Service Command
        """
        print(message)
        messageChoice = chideraCollector("")


    elif generalMenuChoice == "3":
        print("Chat")
        chatMenu = """
             Press 1 - My Service Command
        """
        print(chatMenu)
        chatMenuChoice = chideraCollector("")

    elif generalMenuChoice == "4":
        print("Call Register")


    elif generalMenuChoice == "5":
        print("Tones")

    elif generalMenuChoice == "6":
        print("Settings")



    elif generalMenuChoice == "7":
        print("Call Divert")
        callDivert = """
             Press 1 - Call Divert
        """
        print(callDivert)
        callDivertChoice = chideraCollector("")


    elif generalMenuChoice == "8":
        print("Games")
        games = """
             Press 1 - Games
        """
        print(games)
        gamesChoice = chideraCollector("")


    elif generalMenuChoice == "9":
        print("Calculator")
        calculator = """
             Press 1 - Calculator
        """
        print(calculator)
        calculatorChoice = chideraCollector("")

    elif generalMenuChoice == "10":
        print("Reminder")
        reminder = """
             Press 1 - Reminder
        """
        print(reminder)
        reminderChoice = chideraCollector("")


    elif generalMenuChoice == "11":
        print("Clock")



    elif generalMenuChoice == "12":
        print("Profile")
        profile = """
             Press 1 - Profile
        """
        print(profile)
        profileChoice = chideraCollector("")


    elif generalMenuChoice == "13":
        print("Sim Services")
        simServices = """
             Press 1 - Sim Services
        """
        print(simServices)
        simServicesChoice = chideraCollector("")

    else:
        print("Invalid Input!!!!!!")


main()

