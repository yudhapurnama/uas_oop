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
