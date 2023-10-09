import random

def welcome():
    print("Ласкаво просимо до цієї гри!")
    print("Виберіть свога персонажа:")
    print("1. Лицар")
    print("2. Маг")
    print("3. Розбійник")
    choice = input()
    return choice
def main():
    choice = welcome()
    if choice == '1':
        character = "Лицар"
    elif choice == '2':
        character = "Маг"
    else:
        character = "Розбійник"
    
    print("Ви вибрали персонажа: {character}")
    print("Ви вирушаєте в опасну подорож!")
    health = 100
    gold = 0
    
    while True:
        print("Оберіть локацію:")
        print("1.Піти в ліс")
        print("2.Піти в пещеру")
        print("3.Перевірити мій стан")
        print("4.Закінчити ігру")
        choice = input()
        
        if choice == '1':
            print("Ви вирішили піти в ліс і знайшли скарби")
            gold += 50
        elif choice == '2':
            print("Ви вирішили піти в пещеру і зустріли монстра!")
            damage = random.randint(1, 30)
            if health <= 0:
                print("Ви приграли ігру. Песонаж помер.")
                break
            else:
                print(f"Ви завдали {damage} пошкоджень монстру")
        elif choice == '3':
          print(f"Стан персонажа: Здоров'я: {health}, Золото {gold} ")  
        elif choice == '4':
            print("Гра завершена. Дякую за участь!")
            break
        else:
            print("Будь ласка, виберіть правильну дію.")
if __name__ == "__main__":
    main()