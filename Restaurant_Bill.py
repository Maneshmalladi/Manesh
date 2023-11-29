
import sys, random,datetime

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

billnum=0
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
                plate = int(input(f"Enter how many plates of '{tiffin_name}' you want: "))
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
        print()
        print('-------------------------------------------------')
        date = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        print("TODAY DATE ", date)
        print('-------------------------------')
        billnum += 1

        print("Billnum=", billnum)
        print('-------------------------------')
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