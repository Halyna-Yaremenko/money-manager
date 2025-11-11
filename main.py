def add_item(shopping_list):
    name = input("Введіть назву товару: ")
    quantity = int(input("Введіть кількість: "))
    price = float(input("Введіть ціну за одиницю: "))

    item = {
         "name": name,
         "quantity": quantity,
         "price": price
    }  
    shopping_list.append(item)  

    print(f"✅ {name} додано до списку!")
           
def show_list(shopping_list):
    #   for i in range(len(shopping_list)):
    #        print(f"{i+1} {shopping_list[i]["name"]} - {shopping_list[i]["quantity"]} X {shopping_list[i]["price"]}$")    
   
    if not shopping_list:
        print("\nList is empty")
        return

    print("\nYour list: ", shopping_list)
    for i, item in enumerate(shopping_list, start=1):
        print(f"{i}. {item["name"]} - {item["quantity"]} X {item["price"]}$")    
         
def count_total(shopping_list):   
    total = 0
    for item in shopping_list: 
        total += item["quantity"] * item["price"]
    print(f"Total price: {total:.2f}$")
           
def save_to_file(shopping_list):
    # "w" - перезаписує файл якщо файл існує, або створює новий
    # "a" - дописує (за замовчуванням у кінці файлу) у уже існуючий файл, якщо файлу немає - помилка!!!

    # file = open("text.txt", "w", encoding="utf-8")
    # file.write("Ok")
    # file.write("2 linie")
    # file.write("newlinie")
    # file.close()

    # with open("text.txt", "w", encoding="utf-8") as f:
    #     f.write("Ok")
    #     f.write("2 linie")
    #     f.write("newlinie")

    with open("text.txt", "w", encoding="utf-8") as f:
        for i, item in enumerate(shopping_list, start=1):
            f.write(f"{i}. {item["name"]} - {item["quantity"]} X {item["price"]}$\n")  
    print("shopping_list save to text.txt")

def load_from_file():
    shopping_list = []
    with open("text.txt", "r", encoding="utf-8") as f:
        for line in f:
            line_list = line.strip()[:-1].split()
            # for i in range(1, len(line_list), 2):
            name, quantity, price = line_list[1], line_list[3], line_list[5]
            item = {
                "name": name,
                "quantity": int(quantity),
                "price": float(price)
            }  
            shopping_list.append(item)  
    return shopping_list
print(load_from_file())
    
def main():
    print("🛒 Вітаю у менеджері покупок!")
    shopping_list = []
    
    while True:
        print('''
Меню:
1. Додати покупку
2. Переглянути список
3. Порахувати загальну суму
4. Зберегти у файл
5. Завантажити з файлу
6. Вихід
        ''')
        
        try:
            choice = int(input("Ваш вибір: "))

            match choice:
                case 1:
                    try:
                        add_item(shopping_list)  
                    except ValueError:
                         print("Error!")         
                case 2:
                    show_list(shopping_list)  
                case 3:
                    count_total(shopping_list)  
                case 4:
                    save_to_file(shopping_list)  
                case 5:
                    load_from_file()  
                case 6:
                    print("See you!")
                    break  
                case _:
                    print("Error! Enter number 1-6!")

        except ValueError:
             print("Error! Enter number 1-6!")

if __name__ == "__main__":
     main()




