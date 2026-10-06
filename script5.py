# ==========================================
# FILE: script5.py
# ==========================================
import datetime
import json
import math
import os
import random

import art
import bs4
import colorama
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from PIL import Image
import pydantic
import requests
import tabulate

# --- 5 ВБУДОВАНИХ БІБЛІОТЕК ---


def demo_math():
    return f"[math] Квадратний корінь з 16 = {math.sqrt(16)}"


def demo_datetime():
    return f"[datetime] Поточна дата та час: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"


def demo_random():
    return f"[random] Випадкове число від 1 до 100: {random.randint(1, 100)}"


def demo_os():
    return f"[os] Поточна робоча директорія: {os.getcwd()}"


def demo_json():
    data = {"project": "Lab 4", "status": "Success"}
    json_str = json.dumps(data)
    return f"[json] Серіалізований об'єкт: {json_str}"


# --- 10 СТОРОННІХ БІБЛІОТЕК ---


def demo_requests():
    try:
        response = requests.get(
            "https://httpbin.org/get", timeout=3
        )  # Тестовий запит
        return f"[requests] Статус-код відповіді: {response.status_code}"
    except Exception as e:
        return f"[requests] Запит виконано (помилка мережі: {e})"


def demo_numpy():
    arr = np.array([1, 2, 3, 4, 5])
    return f"[numpy] Середнє значення масиву {arr}: {np.mean(arr)}"


def demo_pandas():
    df = pd.DataFrame({"Назва": ["Товар A", "Товар B"], "Ціна": [100, 200]})
    return f"[pandas] Створено DataFrame (рядків: {len(df)})"


def demo_pillow():
    img = Image.new("RGB", (50, 50), color="blue")
    return f"[pillow] Створено тестове зображення формату {img.size}"


def demo_colorama():
    colorama.init(autoreset=True)
    return f"[colorama] {colorama.Fore.GREEN}Текст зеленого кольору{colorama.Style.RESET_ALL}"


def demo_pydantic():
    class Item(pydantic.BaseModel):
        id: int
        name: str

    item = Item(id=1, name="Laptop")
    return f"[pydantic] Валідована модель: {item}"


def demo_art():
    ascii_art = art.text2art("LAB 4", font="small")
    return f"[art] Генерування ASCII-арту:\n{ascii_art}"


def demo_tabulate():
    data = [["Товар 1", 150], ["Товар 2", 300]]
    table = tabulate.tabulate(
        data, headers=["Назва", "Ціна"], tablefmt="simple"
    )
    return f"[tabulate] Красива таблиця:\n{table}"


def demo_bs4():
    soup = bs4.BeautifulSoup("<html><body><h1>Hello</h1></body></html>", "html.parser")
    return f"[bs4] Парсинг тегу h1: {soup.h1.text}"


def demo_matplotlib():
    plt.figure(figsize=(2, 2))
    plt.plot([1, 2], [1, 2])
    plt.close()
    return "[matplotlib] Графік успішно згенеровано у пам'яті"


# --- ГОЛОВНА ФУНКЦІЯ ---


def main():
    print("=" * 50)
    print("          ЛАБОРАТОРНА РОБОТА №4")
    print("=" * 50)

    print("\n--- ВБУДОВАНІ БІБЛІОТЕКИ (5) ---")
    print(demo_math())
    print(demo_datetime())
    print(demo_random())
    print(demo_os())
    print(demo_json())

    print("\n--- СТОРОННІ БІБЛІОТЕКИ (10) ---")
    print(demo_colorama())
    print(demo_art())
    print(demo_requests())
    print(demo_numpy())
    print(demo_pandas())
    print(demo_pillow())
    print(demo_pydantic())
    print(demo_tabulate())
    print(demo_bs4())
    print(demo_matplotlib())

    print("\n" + "=" * 50)
    print("Усі 15 бібліотек успішно задіяно!")


if __name__ == "__main__":
    main()