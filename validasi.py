class Data:
    def __init__(self):
        # Inisialisasi list untuk menyimpan data
        self.records = []

    def add_record(self, name, age, major, nim, score):
        """
        Menambahkan data baru ke dalam records.

        :param name: Nama mahasiswa (string)
        :param age: Umur mahasiswa (integer)
        :param major: Jurusan mahasiswa (string)
        :param nim: Nomor Induk Mahasiswa (string)
        :param score: Nilai mahasiswa (float)
        """
        self.records.append({
            "Name": name,
            "Age": age,
            "Major": major,
            "NIM": nim,
            "Score": score
        })

    def get_all_records(self):
        """
        Mengembalikan semua data yang tersimpan dalam records.

        :return: List of dictionary berisi data mahasiswa.
        """
        return self.records


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
        print("+----------------+-----+---------------+-----------+-------+")
        print("| Name           | Age | Major         | NIM       | Score |")
        print("+----------------+-----+---------------+-----------+-------+")
        
        # Baris data
        for record in records:
            print(f"| {record['Name']:<14} | {record['Age']:<3} | {record['Major']:<13} | {record['NIM']:<9} | {record['Score']:<5.2f} |")
        
        # Footer tabel
        print("+----------------+-----+---------------+-----------+-------+")


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
                # Validasi nama
                name = input("Enter name: ")
                if not name.strip():
                    raise ValueError("Name cannot be empty.")
                if not name.isalpha():
                    raise ValueError("Name should only contain letters.")

                # Validasi umur
                age = input("Enter age: ")
                if not age.isdigit():
                    raise ValueError("Age must be a number.")
                if int(age) <= 0 or int(age) > 120:
                    raise ValueError("Age must be between 1 and 120.")

                # Validasi jurusan
                major = input("Enter major: ")
                if not major.strip():
                    raise ValueError("Major cannot be empty.")
                if not major.replace(" ", "").isalpha():
                    raise ValueError("Major should only contain letters and spaces.")

                # Validasi NIM
                nim = input("Enter NIM: ")
                if not nim.strip():
                    raise ValueError("NIM cannot be empty.")
                if not nim.isdigit():
                    raise ValueError("NIM must be numeric.")

                # Validasi nilai
                score = input("Enter score: ")
                if not score.replace(".", "").isdigit():
                    raise ValueError("Score must be a number.")
                score = float(score)
                if score < 0 or score > 100:
                    raise ValueError("Score must be between 0 and 100.")

                # Menambahkan data ke dalam class Data
                self.data.add_record(name, int(age), major, nim, score)

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


# Program Utama
if __name__ == "__main__":
    process = Process()  # Membuat instance dari class Process
    process.get_input()  # Mengambil input pengguna
    process.display_data()  # Menampilkan data
