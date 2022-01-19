class mahasiswa():
    def __init__(self, name, nim):
        self.name = name
        self.nim = nim

class dospem(object):
    def __init__(self, dospem_name):
        self.dospem_name = dospem_name

class data_dospem_mahasiswa(mahasiswa, dospem):
    def __init__(self, name, nim, dospem_name, college_year):
        self.college_year = college_year
        mahasiswa.__init__(self, name, nim)
        dospem.__init__(self, dospem_name)
        print(f"Name: {self.name}"+ f" NIM: {self.nim}" + f" Nama Dosen Pembimbing: {self.dospem_name}" + f" Tahun Masuk: {self.college_year}")

input_name = input('Namamu: ')
input_nim = input('NIM Anda: ')
input_dospem = input('Nama dosen pembimbing Anda: ')
input_year = input('Tahun masuk kuliah: ')

output = data_dospem_mahasiswa(input_name, input_nim, input_dospem, input_year)

