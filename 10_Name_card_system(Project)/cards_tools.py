# save all cards in
card_list = []


def show_function():
    """show function"""
    print("*" * 50)
    print("Welcome to [Name card system] V1.0\n")
    print("1: Create name card")
    print("2: Show all")
    print("3: Search name card")
    print("")
    print("0: Quit")
    print("*" * 50)


def new_card():
    """create new card"""
    print("-" * 50)
    print("Add card")
    name_str = input("Name: ")
    phone_str = input("Phone number: ")
    email_str = input("Email: ")
    card_dict = {"name": name_str,
                 "phone": phone_str,
                 "email": email_str}
    card_list.append(card_dict)
    print("Successfully add")


def show_all():
    """show all card"""
    print("-" * 50)
    if len(card_list) == 0:
        print("No name card now")
        return
    for i in ["Name", "Phone", "Email"]:
        print(i, end="\t\t")
    print()
    print("=" * 50)
    for card in card_list:
        print("{}\t\t{}\t\t{}".format(card["name"],
                                      card["phone"],
                                      card["email"]))


def search_card():
    """search card"""
    print("-" * 50)
    find_name = input("Enter the name you want to search: ")
    for card in card_list:
        if card["name"] == find_name:
            for i in ["Name", "Phone", "Email"]:
                print(i, end="\t\t")
            print()
            print("=" * 50)
            print("{}\t\t{}\t\t{}".format(card["name"],
                                          card["phone"],
                                          card["email"]))
            deal_card(card)
            break
    else:
        print("Sorry, can not find")


def deal_card(find_dict):
    """deal card information

    :param find_dict: found dict
    """
    action_str = input("[1]: Change [2]: Delete [0]: Go back ")
    if action_str == "1":
        find_dict["name"] = input_new(find_dict["name"], "Name: ")
        find_dict["phone"] = input_new(find_dict["phone"], "Phone: ")
        find_dict["email"] = input_new(find_dict["email"], "Email: ")
        print("Change successfully")
    elif action_str == "2":
        card_list.remove(find_dict)
        print("Delete successfully")


def input_new(dict_value, message):
    """ add card information

    :param dict_value: original dict_value
    :param message: input message
    :return: if user input, return input, else return the original value
    """
    result_str = input(message)
    if len(result_str) > 0:
        return result_str
    else:
        return dict_value
