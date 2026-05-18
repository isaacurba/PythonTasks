def get_number_of_slice(pizza_type):

    if pizza_type.lower == "sapa":
        return 4
    elif pizza_type.lower() == "odogwu":
        return 12
    elif pizza_type.lower() == "smallMoney":
        return 6
    elif pizza_type.lower() == "bigBoy":
        return 8
    else:
        raise ValueError("Invalid Pizza Type")
