import modification_module

print("Выберите действие:")
print("1 - Изменить размер изображения")
print("2 - Повернуть изображение")

user_selection = input("Введите 1 или 2: ")
picture_way = input("Введите путь к изображению: ")

if user_selection == "1":
    width = int(input("Введите новую ширину: "))
    length = int(input("Введите новую высоту: "))
    result_way = modification_module.resize_picture(picture_way, width, length)
    print('Сохранено в папку Python313: {result_way}')
if user_selection == "2":
    corner = int(input('Введите угол поворота (например, 90): '))
    result_way = modification_module.rotate_picture(picture_way, corner)
    print('Сохранено в папку Python313: {result_way}')

