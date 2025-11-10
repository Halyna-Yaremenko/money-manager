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
        
        tickets_by_class = {}
        total = 0
       
        for name, (quantity, price) in shopping_list.items():
            revenue = quantity * price
            tickets_by_class[name] = revenue
            total += revenue

        return tickets_by_class, total
           
def save_to_file():
               pass
           
def load_from_file():
      pass

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
                    save_to_file()  
                case 5:
                    load_from_file()  
                case 6:
                    print("See you!")
                    break  
                case _:
                    print("Error! Enter number 1-6!")

        except ValueError:
             print("Error! Enter number 1-6!")

main()