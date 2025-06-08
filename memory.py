class MemoryCell:
    def __init__(self, address, raw_data, encoded_data):
        self.address = address
        self.raw_data = raw_data 
        self.encoded_data = encoded_data  
    
    def introduce_error(self, bit_position):
        """Belirtilen bit konumunda hatalı veri oluştur (0-indexli)"""
        if 0 <= bit_position < len(self.encoded_data):
            self.encoded_data[bit_position] ^= 1  # biti tersle
            return True
        return False

    def get_encoded_string(self):
        return ''.join(str(bit) for bit in self.encoded_data)

class Memory:
    def __init__(self):
        self.cells = []
        self.next_address = 0

    def add(self, raw_data, encoded_data):
        """Yeni veri ekle ve otomatik adres ata"""
        cell = MemoryCell(self.next_address, raw_data, encoded_data)
        self.cells.append(cell)
        self.next_address += 1

    def get(self, address):
        """Adrese göre veriyi getir"""
        for cell in self.cells:
            if cell.address == address:
                return cell
        return None
    
    def get_cell_data(self, address):
        for cell in self.cells:
            if cell.address == address:
                return cell.get_encoded_string()
        return None


    def get_all(self):
        """Bellekteki tüm verileri döndür"""
        return self.cells

    def reset(self):
        """Belleği temizle"""
        self.cells.clear()
        self.next_address = 0