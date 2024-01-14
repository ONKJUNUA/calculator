def dodawanie(a, b):
    return a + b

def odejmowanie(a, b):
    return a - b

def mnozenie(a, b):
    return a * b

def dzielenie(a, b):
    if b != 0:
        return a / b
    else:
        return "Błąd: Nie można dzielić przez zero."

while True:
    print("Wybierz operację:")
    print("1. Dodawanie")
    print("2. Odejmowanie")
    print("3. Mnożenie")
    print("4. Dzielenie")
    print("5. Zakończ program")

    wybor = input("Podaj numer operacji (1/2/3/4/5): ")

    if wybor == '5':
        print("Koniec programu.")
        break

    if wybor in ('1', '2', '3', '4'):
        liczba1 = float(input("Podaj pierwszą liczbę: "))
        liczba2 = float(input("Podaj drugą liczbę: "))

        if wybor == '1':
            print(f"Wynik: {dodawanie(liczba1, liczba2)}")
        elif wybor == '2':
            print(f"Wynik: {odejmowanie(liczba1, liczba2)}")
        elif wybor == '3':
            print(f"Wynik: {mnozenie(liczba1, liczba2)}")
        elif wybor == '4':
            print(f"Wynik: {dzielenie(liczba1, liczba2)}")
    else:
        print("Błąd: Nieprawidłowy wybór operacji. Wybierz ponownie.")
