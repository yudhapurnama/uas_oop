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