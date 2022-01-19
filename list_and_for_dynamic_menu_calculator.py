class restaurant_menu(object):
    def __init__(self, name, price):
        self.name = name
        self.price = price
    
    def getprice(self):
        return self.price
    
    def __str__(self):
        return self.name + ' : ' + 'Rp ' + str(self.getprice())
  
def print_menu(menu_list, costs):
    menu = []
    for i in range(len(menu_list)):
        menu.append(restaurant_menu(menu_list[i], costs[i]))
    return menu

def get_order():
    my_order=[]
    order_cost=[]
    jlh_order = []
    while True:
        order = input('Silahkan input pesanan Anda: ')
        jlh = int(input('Berapa porsi?: '))
        if order in menu_list:
            my_order.append(order)
            order_cost.append(costs[menu_list.index(order)])
            jlh_order.append(jlh)
        else:
            print('Maaf, pesanan Anda tidak tersedia')
            continue
        if is_order_done():
            print('-' * 38)
            print('|' + ' PRODUK ' + '|' + ' JUMLAH ' + '|' + ' HARGA ' + '|' + ' SUBTOTAL ' + '|')
            print('-' * 38)
            subtotal = []
            for i in range(len(my_order)):
                subtotal.append(int(jlh_order[i])*int(order_cost[i]))
                print(my_order[i] + ' ' * 10 + str(jlh_order[i]) + ' ' *5 + str(order_cost[i])  + ' ' * 5 + str(subtotal[i]))
            print('-' * 38)
            total_order = sum(jlh_order)
            total_harga = sum(subtotal)
            print('TOTAL: ' + ' ' * 8 + str(total_order) + ' ' * 5 + '-' * 3 + ' ' * 6 + str(total_harga))

def is_order_done():
    rechoose = input('Apakah ada pesanan lain? (y/n): ')
    if rechoose == 'y':
        return False
    elif rechoose == 'n':
        return True
    else:
        raise Exception("Invalid input!")

def print_my_order(order_list):
    print('Pesanan Anda adalah:')
    for order in order_list:
        print(order)
            
menu_list = ['Bayam', 'Nanas', 'Apple']
costs = [4000, 5000, 9000]

Foods = print_menu(menu_list, costs)

nama_pembeli = input('Siapakah nama Anda?: ')
print('=' * 20)
print('Hello', nama_pembeli)
print('=' * 20)

print('====== LIST STOK TERSEDIA ======')
n = 1
for no in Foods:
    print(n,'.', no)
    n = n + 1

order = get_order()
print_my_order(order)

