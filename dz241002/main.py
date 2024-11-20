import os
import time
import datetime


class FileContextManager():
    def __init__(self, type_open: str = "w") -> None:
        self.type_open: str = type_open

    def __enter__(self):
        if self.type_open == "r": # проверка доп. параметра класса
            self.file = open('file.log', "r", encoding='utf-8') # открытие файла на чтение
        else:
            if os.path.exists('file.log'): # проверка, существует ли файл с таким названием
                self.file = open("file.log", "a", encoding='utf-8') # открытие файла на добавление
                self.file.write(f"open {datetime.datetime.now()}\n")
            else:
                self.file = open("file.log", "w", encoding='utf-8') # открытие файла на запись
                self.file.write(f"open {datetime.datetime.now()}\n")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.type_open == "r": # проверка доп. параметра класса
            self.file.close()
        else:
            self.file.write(f"close {datetime.datetime.now()}\n")
            self.file.close()

    def write(self,s: str): # метод для класса, который записывает в файл строку s
        self.file.write(s)

    def readlines(self) -> list[str]: # метод для класса, который считывает строки файла
        return self.file.readlines()

if __name__ == "__main__":

    with FileContextManager() as f:
        f.write("запись 1\n")
        time.sleep(2)

    time.sleep(10)

    with FileContextManager() as f:
        f.write("запись 2\n")
        time.sleep(5)

    time.sleep(2)

    with FileContextManager() as f:
        f.write("запись 3\n")
        time.sleep(5)

    with FileContextManager("r") as f:
        for line in f.readlines():
            print(line.strip())
