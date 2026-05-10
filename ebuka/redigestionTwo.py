#def digit_adder(words):
#    sum_total = 0
#    for char in words:
#        if char == "1" or char == "2" or char == "3" or char == "4" or char == "5" or char == "6" or char == "7" or char == "8" or char == "9":
#            sum_total = sum_total + int(char)
#    return sum_total



def digit_adder(words):
    digits = "123456789"
    total = 0
    for word in words:
        if word in digits:
            total += int(word)

    return total
