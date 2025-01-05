# uas_oop

LINK YT:


### DATA CLASS ###

class Data:
    def __init__(self):
        # Inisialisasi list untuk menyimpan data
        self.records = []

    def add_record(self, name, age, major):
        """
        Menambahkan data baru ke dalam records.

        :param name: Nama mahasiswa (string)
        :param age: Umur mahasiswa (integer)
        :param major: Jurusan mahasiswa (string)
        """
        self.records.append({"Name": name, "Age": age, "Major": major})

    def get_all_records(self):
        """
        Mengembalikan semua data yang tersimpan dalam records.

        :return: List of dictionary berisi data mahasiswa.
        """
        return self.records

### CLASS VIEW

class View:
    @staticmethod
    def display_table(records):
        """
        Menampilkan data dalam bentuk tabel ASCII.

        :param records: List of dictionary yang berisi data mahasiswa.
        """
        if not records:
            print("No data available.")
            return

        # Header tabel
        print("+----------------+-----+---------------+")
        print("| Name           | Age | Major         |")
        print("+----------------+-----+---------------+")
        
        # Baris data
        for record in records:
            print(f"| {record['Name']:<14} | {record['Age']:<3} | {record['Major']:<13} |")
        
        # Footer tabel
        print("+----------------+-----+---------------+")

### CLASS PROCESS

class Process:
    def __init__(self):
        # Membuat instance class Data untuk menyimpan data
        self.data = Data()

    def get_input(self):
        """
        Mengambil input dari pengguna, melakukan validasi, dan menyimpannya ke class Data.
        """
        while True:
            try:
                # Input nama
                name = input("Enter name: ")
                if not name.strip():
                    raise ValueError("Name cannot be empty.")

                # Input umur
                age = input("Enter age: ")
                if not age.isdigit() or int(age) <= 0:
                    raise ValueError("Age must be a positive integer.")

                # Input jurusan
                major = input("Enter major: ")
                if not major.strip():
                    raise ValueError("Major cannot be empty.")

                # Menambahkan data ke dalam class Data
                self.data.add_record(name, int(age), major)

                # Menanyakan apakah ingin menambahkan data lagi
                more = input("Add another record? (y/n): ").lower()
                if more != 'y':
                    break
            except ValueError as e:
                print(f"Error: {e}")

    def display_data(self):
        """
        Menampilkan data menggunakan class View.
        """
        View.display_table(self.data.get_all_records())
