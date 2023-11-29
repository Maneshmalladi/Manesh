#same program but in this it print tiffin numbers instead of tiffin names so dont use


'''import sys

# Prices of tiffins
tiffin_prices = {
    1: 20,  # Idly
    2: 25,  # Plan Dosa
    3: 30,  # Puri
    4: 25,  # Vada
    5: 30,  # Chappati
    6: 30,  # Onion Dosa
    7: 25   # Bajji


}

def menu():
    print("="*30)
    print("\tItems of Tiffins")
    print("="*30)
    print("\t 1.Idly--$20")
    print("\t 2.Plan Dosa--$25")
    print("\t 3.Puri--- $30")
    print("\t 4.Vada---$25")
    print("\t 5.Chappati---$30")
    print("\t 6.Onion Dosa----$30")
    print("\t 7.Maysur Bajji---$25")
    print("\t 8.Exit")

while True:
    try:
        # Initialize order dictionary to store the quantities of each tiffin
        order = {}
        total_cost = 0  # Initialize total cost

        menu()
        while True:
            ch = int(input("Enter tiffin number (0 to finish ordering): "))
            if ch == 0:
                break
            elif ch in tiffin_prices:

                plate = int(input(f"Enter how many plates of Tiffin {ch} you want: "))
                order[ch] = plate  # Store the quantity of the tiffin
                total_cost += plate * tiffin_prices[ch]  # Update the total cost
            elif ch==8:
                print("Thanks for Eating! Visit Again \U0001F60B")
                sys.exit()
            else:
                print("wrong try again")



        # Display the bill for each tiffin
        for tiffin_num, quantity in order.items():
            price = tiffin_prices[tiffin_num]
            print(f"Cost of Tiffin {tiffin_num}: ${price}")
            print(f"Number of plates: {quantity}")
            print(f"Total: {price} x {quantity} = ${price * quantity}")
            print()

        print(f"Total bill: ${total_cost}")

    except ValueError:
        print("Invalid input. Please enter a valid number.")

    except Exception as e:
        print("Something went wrong:", str(e))'''

#==========================================================================================================================



#it prints tiffin names


import sys

# Prices of tiffins
tiffin_prices = {
    1: {"name": "Idly", "price": 20},
    2: {"name": "Plan Dosa", "price": 25},
    3: {"name": "Puri", "price": 30},
    4: {"name": "Vada", "price": 25},
    5: {"name": "Chappati", "price": 30},
    6: {"name": "Onion Dosa", "price": 30},
    7: {"name": "Maysur Bajji", "price": 25}
}

def menu():
    print("="*30)
    print("\tItems of Tiffins")
    print("="*30)
    for tiffin_num, tiffin_info in tiffin_prices.items():
        print(f"\t {tiffin_num}.{tiffin_info['name']}--${tiffin_info['price']}")
    print("\t 8.Exit")

while True:
    try:
        # Initialize order dictionary to store the quantities of each tiffin
        order = {}
        total_cost = 0  # Initialize total cost

        menu()
        while True:
            ch = int(input("Enter tiffin number (0 to finish ordering): "))
            if ch == 0:
                break
            elif ch in tiffin_prices:
                tiffin_name = tiffin_prices[ch]["name"]
                plate = int(input(f"Enter how many plates of {tiffin_name} you want: "))
                if plate>0:
                      order[ch] = plate  # Store the quantity of the tiffin
                      total_cost += plate * tiffin_prices[ch]["price"]  # Update the total
                else:
                    print("dont enter negative numbers")
                    break
            elif ch == 8:
                print("Thanks for Eating! Visit Again \U0001F60B")
                sys.exit()
            else:
                print("Your selection is wrong. Try again.")

        # Display the bill for each tiffin
        for tiffin_num, quantity in order.items():
            tiffin_name = tiffin_prices[tiffin_num]["name"]
            price = tiffin_prices[tiffin_num]["price"]
            print()
            print(f"Cost of {tiffin_name}: ${price}")
            print(f"Number of plates: {quantity}")
            print(f"Total: {price} x {quantity} = ${price * quantity}")
            print()
        print(" = "*20)
        print(f"Total bill: ${total_cost}")
        print(" = "*20)


    except ValueError:
        print("Invalid input. Please enter a valid number.")
    except ZeroDivisionError:
        print("dont enter -ves")

    except Exception as e:
        print("Something went wrong:", str(e))
