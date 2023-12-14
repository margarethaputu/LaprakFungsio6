from PIL import Image, ImageDraw, ImageFont

# TODO 0: Import library lain yang dibutuhkan

# TODO 1: Lakukan load image pada variabel berikut
# hint: kalian bisa gunakan fungsi open()
gambarku = Image.open('C:\\Users\\Asus\\OneDrive\\Documents\\KULIAH\\SEMESTER 5\\Pemrograman Fungsional\\Modul 6\\Tahu2.jpg')
# TODO 2: Ubah gambar menjadi hitam-putih
# hint: kalian bisa gunakan fungsi convert()
gambarBW = gambarku.convert("L")

# TODO 3: Tambahkan text sesuai kriteria.
direktoriFont = (
    'C:\Users\Asus\OneDrive\Documents\KULIAH\SEMESTER 5\Pemrograman Fungsional\Modul 6\Font/arial'
)
draw = ImageDraw.Draw(gambarBW)

font = ImageFont.truetype(direktoriFont, 24)
text = "Ni Putu Margaretha - 202110370311149"

# Use textbbox on the ImageDraw object to get the bounding box
text_bbox = draw.textbbox((0, 0), text, font)

# Extract width and height from the bounding box
text_width = text_bbox[2] - text_bbox[0]
text_height = text_bbox[3] - text_bbox[1]

text_x = (gambarBW.width - text_width) // 2
text_y = (gambarBW.height - text_height) // 2

draw.text((text_x, text_y), text, font=font, fill='blue')


# TODO 4: Simpan gambar hasil edit menggunakan fungsi save()
gambarBW.save("per1.jpg")

# TODO 5: Tampilkan hasil akhir gambar
gambarBW.show()
