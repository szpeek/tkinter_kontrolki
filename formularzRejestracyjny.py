import tkinter as tk
from tkinter import messagebox



def submit_form():
    imie = pole_imie.get()
    email = emailEntry.get()
    wiek = wiekWartosc.get()
    uwagi_text = uwagi.get("1.0", 'end-1c')

    zainteresowania = []
    if ksiazki_var.get():
        zainteresowania.append("Ksiazki")
    if sport_var.get():
        zainteresowania.append("Sport")

    zainteresowania_text = ', '.join(zainteresowania) if zainteresowania else "Brak"

    messagebox.showinfo(
        "Dane uzytkownika",
        f"Imię :{imie}\nEmail: {email}\nWiek: {wiek}\nZainteresowania: {zainteresowania_text}\nUwagi: {uwagi_text}"
    )


root = tk.Tk()
root.title("Formularz Rejestracyjny")
root.geometry("500x600")
root.grid_columnconfigure(0, minsize=120)

# --- Kontrolki ---
wiekWartosc = tk.StringVar()
ksiazki_var = tk.BooleanVar()
sport_var = tk.BooleanVar()

# Label dla imienia
tk.Label(root, text="Imię :").grid(row=0, column=0, padx=10,pady=5, sticky="w")

# Entry dla imienia
pole_imie = tk.Entry(root, width=30)
pole_imie.grid(row=0, column=1, padx=10, pady=10, sticky="w")

tk.Label(root, text="Email :").grid(row=1, column=0, padx=10, pady=5, sticky="w")

emailEntry = tk.Entry(root, width=30)
emailEntry.grid(row=1, column=1, padx=10, pady=10, sticky="w")

tk.Label(root, text="Wiek :").grid(row=2, column=0, padx=10, pady=5, sticky="w")

tk.Radiobutton(root, text="18-30", variable=wiekWartosc,  value="18-30").grid(row=2, column=1, sticky="w", padx=20)
tk.Radiobutton(root, text="31-50",variable=wiekWartosc, value="31-50").grid(row=3, column=1, sticky="w", padx=20)
tk.Radiobutton(root, text="50+", variable=wiekWartosc, value="50+").grid(row=4, column=1, sticky="w", padx=20)

tk.Label(root, text="Zainteresowania :").grid(row=5, column=0, padx=10, pady=5, sticky="w")

przycisk_zainteresowanie = tk.Checkbutton(root, text="Książki", variable=ksiazki_var)
przycisk_zainteresowanie.grid(row=5, column=1, padx=21, pady=1, sticky="w")
przycisk_zainteresowanie1 = tk.Checkbutton(root, text="Sport", variable=sport_var)
przycisk_zainteresowanie1.grid(row=6, column=1, padx=21, pady=1, sticky="w")

tk.Label(root, text="Uwagi: ").grid(row=7, column=0, padx=10, pady=5, sticky="nw")
uwagi = tk.Text(root, width=25, height=6)
uwagi.grid(row=7, column=1, padx=10, pady=10, sticky="w")

submit = tk.Button(root, text="Zarejestruj", command=submit_form)
submit.grid(row=8, column=1, padx=10, pady=10, sticky="w")

# Uruchomienie pętli głównej
root.mainloop()