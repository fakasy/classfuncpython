
print("class function") 

class manusia:
    def __init__(self, nama, umur, alamat):
    
        self.nama = input("masukkan nama: ")
        self.umur = input("masukkan umur: ")
        self.alamat = input("masukkan alamat: ")

    def perkenalan(self):
        print("halo, ", self.nama, "umurmu", self.umur, "tua banget jir. alamat kamu di", self.alamat, "selamat kamu terkena OSINT")

manusia1 = manusia("joko", 20, "sukabumi")

manusia1.perkenalan()


#dalam satu file sama yg kemarin ditambah class function⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️
#dalam satu file sama yg kemarin ditambah class function⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️
#dalam satu file sama yg kemarin ditambah class function⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️
#dalam satu file sama yg kemarin ditambah class function⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️
#dalam satu file sama yg kemarin ditambah class function⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️


class Buah:
    def __init__(self, nama_buah):
        self.nama = nama_buah
    
    def cek_nama(self):
        if self.nama in ["apel", "jeruk", "mangga", "pisang", "anggur"]:
            print("Buah", self.nama, "ada di daftar buah.")
        else:
            print("Buah", self.nama, "tidak ada di daftar buah.")


class Looping:
    def __init__(loop, x):
        loop.x = x
    
    def looping_while(loop):
        while loop.x < 21:
            print(loop.x, "pizza chicken lion")
            loop.x += 1


class BreakContinue:
    def __init__(bc):
        pass
    
    def break_continue(bc):
        for i in range(1, 11):
            if i == 5:
                break
            print(i)
        for i in range(1, 11):
            if i == 5:
                continue
            print(i)


class SwitchCase:
    def __init__(sc, x):
        sc.x = x
    
    def switch_case(sc):
        try:
            if sc.x == 1:
                print("Anda memilih angka 1")
            elif sc.x == 2:
                print("Anda memilih angka 2")
            elif sc.x == 3:
                print("Anda memilih angka 3")
            else:
                print("Anda memilih angka lain")
        except ValueError:
            print("Input harus berupa angka.")


buat_buah = Buah(input("Masukkan nama buah: "))
buat_buah.cek_nama()

buat_looping = Looping(int(input("Masukkan angka: ")))
buat_looping.looping_while()

buat_break_continue = BreakContinue()
buat_break_continue.break_continue()

buat_switch_case = SwitchCase(int(input("Masukkan angka: ")))
buat_switch_case.switch_case()

