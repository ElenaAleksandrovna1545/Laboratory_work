# TODO Найдите количество книг, которое можно разместить на дискете
disk_size_mb = 1.44
pages = 100
lines_per_page = 50
chars_per_line = 25
bytes_per_char = 4

disk_size_bytes = disk_size_mb * 1024 * 1024
total_chars_in_book = pages * lines_per_page * chars_per_line
book_size_bytes = total_chars_in_book * bytes_per_char
book_on_disk = disk_size_bytes // book_size_bytes

print("Количество книг, помещающихся на дискету:", round(book_on_disk))
