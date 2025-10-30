import tkinter as tk
from tkinter import messagebox


def pokaz_dane():
    # Pobieranie danych z Entry
    imie = pole_imie.get()

    # Pobieranie stanu Checkbutton
    czy_aktywny = stan_aktywny.get()
    status_aktywny = "Aktywny" if czy_aktywny == 1 else "Nieaktywny"

    # Pobieranie stanu Radiobutton
    wybrany_kolor = stan_kolor.get()

    # Tworzenie komunikatu
    komunikat = f"Imię: {imie}\nStatus: {status_aktywny}\nWybrany Kolor: {wybrany_kolor}"

    # Wyświetlenie komunikatu w oknie dialogowym
    messagebox.showinfo("Podsumowanie", komunikat)

def convert():
    imie = pole_imie.get()
    imie = float(imie)

    imie = imie/0.3048

    wynik.configure(text=imie)

# 1. Inicjalizacja głównego okna
root = tk.Tk()
root.title("Przykładowe Kontrolki Tkinter")
root.geometry("400x350")

# 2. Definicja zmiennych Tkinter
stan_aktywny = tk.IntVar()
stan_kolor = tk.StringVar(value="Czerwony")  # Ustawienie domyślnej wartości

# --- Kontrolki ---

# Label dla imienia
tk.Label(root, text="Wprowadź wartość (metry):").grid(row=0, column=0, padx=10, pady=10, sticky="w")

# Entry dla imienia
pole_imie = tk.Entry(root, width=30)
pole_imie.grid(row=0, column=1, padx=10, pady=10)

'''
przycisk_aktywny = tk.Checkbutton(root, text="Czy użytkownik jest aktywny?", variable=stan_aktywny)
przycisk_aktywny.grid(row=1, column=0, columnspan=2, pady=5, sticky="w")

# Label dla Radiobutton
tk.Label(root, text="Wybierz kolor:").grid(row=2, column=0, padx=10, pady=5, sticky="w")

# Radiobuttons (muszą mieć tę samą zmienną 'stan_kolor')
tk.Radiobutton(root, text="Czerwony", variable=stan_kolor, value="Czerwony").grid(row=3, column=0, sticky="w", padx=20)
tk.Radiobutton(root, text="Zielony", variable=stan_kolor, value="Zielony").grid(row=4, column=0, sticky="w", padx=20)
tk.Radiobutton(root, text="Niebieski", variable=stan_kolor, value="Niebieski").grid(row=5, column=0, sticky="w",
                                                                                    padx=20)
'''
# Button
przycisk_akcja = tk.Button(root, text="Konwertuj na stopy", command=convert, bg="#4CAF50", fg="white",
                           font=('Arial', 10, 'bold'))
przycisk_akcja.grid(row=6, column=0, columnspan=2, pady=20)

wynik = tk.Label(root, text="Wynik: 0.0 stóp")
wynik.grid(row=7, column=0, columnspan=2, pady=20)

# Uruchomienie pętli głównej
root.mainloop()