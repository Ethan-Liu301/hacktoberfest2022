while True:
    try:
        r = float(input("Give me any radius and I will calculate the circle's area: "))
        a = (r * r) * 3.14159
        print("A=%0.4f" % a)
        break  # Exit the loop if the input is valid
    except:
        print("Please enter an actual number.")
