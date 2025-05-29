# physics-2025

## Установка окружения и зависимостей

1. **Создайте и активируйте виртуальное окружение**:

   * На Windows:

     ```bash
     python -m venv venv
     .\venv\Scripts\activate
     ```
   * На macOS/Linux:

     ```bash
     python3 -m venv venv
     source venv/bin/activate
     ```

2. **Установите зависимости**:

   * Если у вас есть файл `requirements.txt`:

     ```bash
     pip install -r requirements.txt
     ```
   * Если `requirements.txt` отсутствует, создайте его из текущего окружения:

     ```bash
     pip freeze > requirements.txt
     ```

     Затем установите:

     ```bash
     pip install -r requirements.txt
     ```

## Предварительные требования

* Python 3.10 или выше
* Библиотеки:

  * numpy
  * matplotlib

## Инструкция по запуску `mod1.py`

1. **Запустите скрипта**:

   ```bash
   python mod1.py
   ```

