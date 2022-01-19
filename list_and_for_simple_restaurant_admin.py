def lihat_produk(barang, stok, harga):
    print('-' * 25)
    print('|' + ' PRODUK ' + '|' + ' STOK ' + '|' + ' HARGA ' + '|')
    print('-' * 25)

    for i in range(len(barang)):
        print(barang[i] + ' ' * 7 + str(stok[i]) + ' ' * 7 + str(harga[i]))

    print('-' * 25)

def input_produk(barang, stok, harga):
    input_barang, input_stok, input_harga = input('Masukkan data produk baru (nama stok harga): ').split()
    print('Silahkan input nama barang: ', input_barang)
    print('Silahkan input jumlah stok: ', input_stok)
    print('Silahkan input harga: ', input_harga)

    barang.append(input_barang)
    stok.append(input_stok)
    harga.append(input_harga)

    print('-' * 25)
    print('|' + ' PRODUK ' + '|' + ' STOK ' + '|' + ' HARGA ' + '|')
    print('-' * 25)

    for i in range(len(barang)):
        print(barang[i] + ' ' * 7 + str(stok[i]) + ' ' * 7 + str(harga[i]))
    
    print('-' * 25)

def edit_produk(barang, stok, harga):
    print('Berikut adalah data produk Anda sekarang:')
    print('-' * 30)
    print('|' + ' NO ' + '|' + ' PRODUK ' + '|' + ' STOK ' + '|' + ' HARGA ' + '|')
    print('-' * 30)

    n = 0
    for i in range(len(barang)):
        print(str(n) + '.' + ' ' * 4 + barang[i] + ' ' * 7 + str(stok[i]) + ' ' * 6 + str(harga[i]))
        n += 1
    print('-' * 30)

    up_no = int(input('Masukkan nomor produk yang ingin diedit: '))
    barang[up_no] = input('Edit nama barang: ')
    stok[up_no] = int(input('Edit jumlah stok: '))
    harga[up_no] = int(input('Edit harga produk: '))

    print('Berikut adalah hasil update: ')

    print('-' * 30)
    print('|' + ' NO ' + '|' + ' PRODUK ' + '|' + ' STOK ' + '|' + ' HARGA ' + '|')
    print('-' * 30)

    n = 0
    for i in range(len(barang)):
        print(str(n) + '.' + ' ' * 4 + barang[i] + ' ' * 7 + str(stok[i]) + ' ' * 6 + str(harga[i]))
        n += 1
    print('-' * 30)

def hapus_produk(barang, stok, harga):
    print('Berikut adalah data produk Anda sekarang:')
    print('-' * 30)
    print('|' + ' NO ' + '|' + ' PRODUK ' + '|' + ' STOK ' + '|' + ' HARGA ' + '|')
    print('-' * 30)

    n = 0
    for i in range(len(barang)):
        print(str(n) + '.' + ' ' * 4 + barang[i] + ' ' * 7 + str(stok[i]) + ' ' * 6 + str(harga[i]))
        n += 1
    print('-' * 30)

    del_no = int(input('Masukkan nomor produk yang ingin dihapus: '))
    barang.remove(barang[del_no])
    stok.remove(stok[del_no])
    harga.remove(harga[del_no])

    print('Berikut adalah hasil terupdate: ')

    print('-' * 30)
    print('|' + ' NO ' + '|' + ' PRODUK ' + '|' + ' STOK ' + '|' + ' HARGA ' + '|')
    print('-' * 30)

    n = 0
    for i in range(len(barang)):
        print(str(n) + '.' + ' ' * 4 + barang[i] + ' ' * 7 + str(stok[i]) + ' ' * 6 + str(harga[i]))
        n += 1
    print('-' * 30)


barang = ['Bayam', 'Nanas', 'Apple']
stok = [90, 50, 60]
harga = [4000, 5000, 9000]

print('=' * 40)
print('TOKO SINAR FAJAR')
print('=' * 40)

print('1. Lihat Produk')
print('2. Input Produk')
print('3. Edit Produk')
print('4. Hapus Produk')

print('=' * 40)

input_user = int(input('Silahkan pilih menu: '))

if input_user == 1:
    lihat_produk(barang, stok, harga)
elif input_user == 2:
    input_produk(barang, stok, harga)
elif input_user == 3:
    edit_produk(barang, stok, harga)
elif input_user == 4:
    hapus_produk(barang, stok, harga)

