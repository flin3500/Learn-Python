#! /usr/local/bin/python3

import LN_02_cards_tools
while True:

    """# TODO(Lin/lin.acandc@gmail.com) show Function"""
    LN_02_cards_tools.show_function()
    action = input("Please choose what you want to do ")
    print("What you choose is {}".format("[" + action + "]"))

    if action in ["1", "2", "3"]:
        if action == "1":
            LN_02_cards_tools.new_card()
        elif action == "2":
            LN_02_cards_tools.show_all()
        else:
            LN_02_cards_tools.search_card()
    elif action == "0":
        print("Thank you")
        break
    else:
        print("Incorrect, choose again")
