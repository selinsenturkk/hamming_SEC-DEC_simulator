import tkinter as tk
from tkinter import messagebox, ttk
from hamming import encode, decode
from memory import Memory
import random

memory = Memory()

class HammingSimulatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Hamming SEC-DED Simülatörü")

        # Giriş çerçevesi
        self.input_frame = tk.LabelFrame(root, text="Veri Girişi")
        self.input_frame.pack(padx=10, pady=10, fill="x")

        self.data_entry = tk.Entry(self.input_frame, width=40)
        self.data_entry.pack(side="left", padx=5)

        self.encode_button = tk.Button(self.input_frame, text="Kodla ve Belleğe Yaz", command=self.encode_data)
        self.encode_button.pack(side="left", padx=5)

        # Bellek tablosu
        self.table = ttk.Treeview(root, columns=("address", "raw", "encoded"), show="headings")
        self.table.heading("address", text="Adres")
        self.table.heading("raw", text="Veri")
        self.table.heading("encoded", text="Kodlanmış Veri")
        self.table.pack(padx=10, pady=10, fill="x")

        # Hata verme ve düzeltme
        self.error_frame = tk.LabelFrame(root, text="Yapay Hata ve Düzeltme")
        self.error_frame.pack(padx=10, pady=10, fill="x")

        self.address_entry = tk.Entry(self.error_frame, width=5)
        self.address_entry.pack(side="left", padx=5)
        self.address_entry.insert(0, "0")

        self.bit_entry = tk.Entry(self.error_frame, width=5)
        self.bit_entry.pack(side="left", padx=5)
        self.bit_entry.insert(0, "0")

        self.error_button = tk.Button(self.error_frame, text="Bit Hatası Oluştur", command=self.introduce_error)
        self.error_button.pack(side="left", padx=5)

        self.double_error = tk.Button(self.error_frame, text="Rastgele Double Bit Hatası Oluştur", command=self.double_error_generate)
        self.double_error.pack(side="left", padx=5)

        self.decode_button = tk.Button(self.error_frame, text="Analiz Et ve Düzelt", command=self.decode_data)
        self.decode_button.pack(side="left", padx=5)

    def encode_data(self):
        data = self.data_entry.get().strip()
        if len(data) not in [8, 16, 32] or not all(c in '01' for c in data):
            messagebox.showerror("Hatalı Giriş", "Lütfen sadece 8, 16 veya 32 bitlik 0 ve 1'lerden oluşan veri girin.")
            return

        try:
            coded = encode(data)
            memory.add(data, coded)
            self.update_table()
        except Exception as e:
            messagebox.showerror("Hata", str(e))

    def update_table(self):
        for i in self.table.get_children():
            self.table.delete(i)
        for cell in memory.get_all():
            self.table.insert("", "end", values=(cell.address, cell.raw_data, cell.get_encoded_string()))

    def introduce_error(self):
        try:
            addr = int(self.address_entry.get())
            bit_pos = int(self.bit_entry.get())
            cell = memory.get(addr)
            if cell and cell.introduce_error(bit_pos):
                self.update_table()
                messagebox.showinfo("Başarılı", f"{addr}. adresteki {bit_pos}. bit ters çevrildi.")
            else:
                messagebox.showerror("Hata", "Geçersiz adres veya bit konumu.")
        except ValueError:
            messagebox.showerror("Hata", "Lütfen sayısal adres ve bit konumu girin.")

    def double_error_generate(self):
        try:
            addr = int(self.address_entry.get())
            data = memory.get_cell_data(addr) 
            cell = memory.get(addr)
            data_len = len(data)
            randbit1 = random.randint(0,data_len-1)
            randbit2 = random.randint(0,data_len-1)
            while randbit2 == randbit1:
                randbit2 = random.randint(0,data_len-1)
            cell.introduce_error(randbit1)
            cell.introduce_error(randbit2)
            messagebox.showinfo("Başarılı", "2 adet rastgele bit çevirildi.")
        except:
            messagebox.showerror("Hata", "Adres değerini doğru giriniz.")
        self.update_table()        
            

    def decode_data(self):
        try:
            addr = int(self.address_entry.get())
            cell = memory.get(addr)
            if not cell:
                messagebox.showerror("Hata", "Bu adreste veri bulunamadı.")
                return

            result = decode(cell.encoded_data)
            
            cell.encoded_data = result["corrected_code"]

            self.update_table()
            if result['error_type'] == "Çift bit hatası (düzeltilemez)":
                msg = "Çift bit hatası (düzeltilemez)"
            else:
                msg = f"Hata Türü: {result['error_type']}\nHatalı Bit: {result['error_position']}\nDüzeltilmiş Kod: {''.join(str(b) for b in result['corrected_code'])}"
            messagebox.showinfo("Analiz Sonucu", msg)

        except Exception as e:
            messagebox.showerror("Hata", str(e))

if __name__ == "__main__":
    root = tk.Tk()
    app = HammingSimulatorApp(root)
    root.mainloop()
