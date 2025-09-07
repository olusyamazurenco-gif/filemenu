import os
import webbrowser

def menu():
    filename = None
    content = ""

    while True:
        print("\n===== МЕНЮ =====")
        print("1. Открыть файл")
        print("2. Редактировать файл")
        print("3. Сделать файл .html и открыть")
        print("4. Выход")
        choice = input("Выберите пункт: ")

        if choice == "1":
            path = input("Введите путь к файлу: ")
            if os.path.exists(path):
                filename = path
                with open(filename, "r", encoding="utf-8") as f:
                    content = f.read()
                print(f"\n✅ Файл '{filename}' открыт.\n")
                print(content)
            else:
                print("⚠️ Файл не найден!")

        elif choice == "2":
            print("\nВведите новый текст (в конце нажмите Enter + Ctrl+D / Ctrl+Z):")
            lines = []
            try:
                while True:
                    line = input()
                    lines.append(line)
            except EOFError:
                pass
            content = "\n".join(lines)
            print("✅ Файл отредактирован.")

        elif choice == "3":
            if not content.strip():
                print("⚠️ Нет содержимого для сохранения!")
                continue
            html_path = "output.html"
            with open(html_path, "w", encoding="utf-8") as f:
                f.write(content)
            webbrowser.open("file://" + os.path.abspath(html_path))
            print(f"✅ Файл сохранён как {html_path} и открыт в браузере.")

        elif choice == "4":
            print("👋 Выход из программы.")
            break

        else:
            print("⚠️ Неверный пункт, попробуйте снова.")
