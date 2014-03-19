from time import time
from datetime import datetime
from glob import glob

def take(name, price, orders):
    if name in orders:
        orders[name] += price
    else:
        orders[name] = price
    print("Taking order %s for %.2d" % (name, price))

def status(orders):
    orders_as_string = []
    for key in orders:
        orders_as_string.append("%s - %.2d" % (key, orders[key]))
    return "\n".join(orders_as_string)

def save(orders):
    ts = time()
    stamp = datetime.fromtimestamp(ts).strftime('%Y_%m_%d_%H_%M_%S')
    current_orders_file = open("orders_" + stamp, "w")
    current_orders_file.write(status(orders))
    current_orders_file.close()
    print("Saved the current order to orders_" + stamp)

def list():
    filenames = glob("orders_*")
    for i in range(len(filenames)):
        print("[" + str(i + 1) + "] - " + filenames[i])

def load(number, orders):
    filenames = glob("orders_*")

    file = open(filenames[number - 1], "r")
    content = file.read()
    file.close()

    list_of_orders = map(lambda x: x.split(" - "), content.split("\n"))
    orders = {}

    for item in list_of_orders:
        orders[item[0]] = float(item[1])
    print("Loading " + filenames[number - 1])
    return orders

def unknown_command():
    print("Unknown command!")
    print("Try one of the following:")
    print("take <name> <price>")
    print("status")
    print("save")
    print("list")
    print("load <number>")
    print("finish")

def get_command(command):
    return command.split(" ")

def main():
    orders = {}
    commands = []
    is_saved = False
    while True:
        command = input("Enter command> ")
        command_split = get_command(command)

        if command_split[0] == "take":
            if len(command_split) == 3:
                take(command_split[1], float(command_split[2]), orders)
                commands.append("take")
                is_saved = False
            else:
                unknown_command()
                commands.append("unknown")
        elif command_split[0] == "status":
            print(status(orders))
            commands.append("status")
        elif command_split[0] == "save":
            save(orders)
            commands.append("save")
            is_saved = True
        elif command_split[0] == "list":
            list()
            commands.append("list")
        elif command_split[0] == "load":
            if commands[len(commands) - 1] == "list" and is_saved and len(command_split) == 2:
                orders = load(int(command_split[1]), orders)
            elif not is_saved:
                    print("You have not saved the current order.")
                    print("If you wish to discard it, type load <number> again.")
                    is_saved = True
            else:
                print("Use list command before loading")
            commands.append("load")

        elif command_split[0] == "finish":
            if not is_saved:
                print("You have not saved your order.")
                print("If you wish to continue, type finish again.")
                print("If you want to save your order, type save")
                is_saved = True
                commands.append("finish")
            else:
                print("Finishing order. Bye!")
                break
        else:
            unknown_command()

if __name__ == '__main__':
    main()