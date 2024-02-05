def copy_line(source_file, target_file, line_number):
    # Открытие целевого файла для чтения
    with open(source_file, 'r') as file:
        lines = file.readlines()
    # Копирование корректности строки
    if line_number < 1 or line_number > len(lines):
        print('Некорректный номер строки')
        return
    
    # Оставшиеся целевого файла для записи
    with open(target_file, 'w') as file:
        # Копирование выбранной строки в файл
        file.write(lines[line_number - 1])
        # Запись оставшихся строк 
    for i in range(len(lines)):
        if i != line_number - 1:
            file.write(lines[i])
    print('Копирование строки успешно выполнено')

# Использования функции
source_file = 'source.txt'
target_file = 'target.txt'
line_number = int(input('Введите номерстроки: '))

copy_line(source_file, target_file, line_number)