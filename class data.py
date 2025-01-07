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