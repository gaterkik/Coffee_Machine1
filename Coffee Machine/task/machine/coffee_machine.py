tlncontent = {
    'money': 550,
    'water': 400,
    'milk': 540,
    'beans': 120,
    'cups': 9
}
espresso = {
    'money': 4,
    'water': -250,
    'milk': 0,
    'beans': -16,
    'cups': -1
}
latte = {
    'money': 7,
    'water': -350,
    'milk': -75,
    'beans': -20,
    'cups': -1
}
cappuccino = {
    'money': 6,
    'water': -200,
    'milk': -100,
    'beans': -12,
    'cups': -1
}

price = [0, espresso, latte, cappuccino]

def conversion(dic):
    for item in dic:
        content[item] += dic[item]


def enough(dic):
    for item in dic:
        if dic[item] + content[item] < 0:
            return False
    return True


def diagnostics(dic):
    stock = []
    for item in dic:
        if dic[item] + content[item] < 0:
            stock.append(item)
    print(f'Sorry, not enough {", ".join(stock)}!')


def print_status():
    print()
    print('The coffee machine has:')
    print(f'{content["water"]} of water')
    print(f'{content["milk"]} of milk')
    print(f'{content["beans"]} of coffee beans')
    print(f'{content["cups"]} of disposable cups')
    print(f'{content["money"]} of money')
    print()


while True:
    change_dic = dict()
    print('Write action (buy, fill,  take, remaining, exit):')
    action = input('> ')

    if action == 'fill':
        print('Write how many ml of water do you want to add:')
        change_dic['water'] = int(input('> '))
        print('Write how many ml of milk do you want to add:')
        change_dic['milk'] = int(input('> '))
        print('Write how many grams of coffee beans do you want to add:')
        change_dic['beans'] = int(input('> '))
        print('Write how many disposable cups of coffee do you want to add:')
        change_dic['cups'] = int(input('> '))

    elif action == 'buy':
        print('What do toy want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:')
        choice = input('> ')
        if choice == 'back':
            continue
        else:
            choice = int(choice)
        if enough(price[choice]):
            print('I have enough resources, making you a coffee!')
            print()
            change_dic = price[choice]
        else:
            diagnostics(price[choice])

    elif action == 'take':
        print(f'I gave you ${content["money"]}')
        change_dic['money'] = - content["money"]

    elif action == 'remaining':
        print_status()

    elif action == 'exit':
        break

    conversion(change_dic)


