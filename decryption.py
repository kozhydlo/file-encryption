import pyAesCrypt
import os

# Функція дешифрування файла
def decryption(file, password):
    # Задаємо розмір буфера
    buffer_size = 512 * 1024
    
    # Визиваємо метод дешифрування
    pyAesCrypt.decryptFile(
        str(file),
        str(os.path.splitext(file)[0]),
        password,
        buffer_size
    )
    
    # Щоб бачити результат, виводимо на печать ім'я дешифрованого файлу
    print("[Файл '" + str(os.path.splitext(file)[0]) + "' дешифрований]")
    
    # Видаляємо зашифрований файл
    os.remove(file)

# Функція сканування деректорії
def walking_by_dirs(dir, password):
    # Перебираємо всі піддеректорії в заданій деректорії
    for name in os.listdir(dir):
        path = os.path.join(dir, name)
        
        # Якщо находимо файл, то дешифруємо його
        if os.path.isfile(path):
            try:
                decryption(path, password)
            except Exception as ex:
                print(ex)
                
        # Якщо находимо деректорію, то повторюємо цикл в пошуках файлів
        else:
            walking_by_dirs(path, password)

password = input("Введіть пароль для дешифрування: ")
walking_by_dirs("C:/Users/Mark/Desktop", password)
