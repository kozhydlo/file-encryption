import pyAesCrypt
import os

# Функція шифрування файла
def encryption(file, password):
    # Задаємо розмір буфера
    buffer_size = 512 * 1024
    
    # Визиваємо метод шифрування
    pyAesCrypt.encryptFile(
        str(file),
        str(file) + ".crp",
        password,
        buffer_size
    )
    
    # Щоб бачити результат виводимо на печать ім'я зашифрованого файлу
    print("[Файл '" + str(os.path.splitext(file)[0]) + "' зашифрований]")

    # Видаляємо поточний файл
    os.remove(file)

# Функція сканування деректорії
def walking_by_dirs(dir, password):
    # Перебираємо всі піддеректорії в заданій деректорії
    for name in os.listdir(dir):
        path = os.path.join(dir, name)
        
        # Якщо находимо файл, то шифруємо його
        if os.path.isfile(path):
            try:
                encryption(path, password)
            except Exception as ex:
                print(ex)
                
        # Якщо находимо деректорію, то повторюємо цикл в пошуках файлів
        else:
            walking_by_dirs(path, password)

password = input("Введіть пароль для шифрування: ")
walking_by_dirs("C:/Users/Mark/Desktop", password)
