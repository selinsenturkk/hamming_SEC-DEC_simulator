def calculate_parity_bits(data_len):
    r = 0
    while (2 ** r) < (data_len + r + 1):
        r += 1
    return r

def insert_parity_positions(data_bits):
    r = calculate_parity_bits(len(data_bits))
    total_len = len(data_bits) + r
    result = []
    j = 0  # data bit index

    for i in range(1, total_len + 1):
        if (i & (i - 1)) == 0:  # 2^n konumlar = parite bitleri
            result.append(0)
        else:
            result.append(int(data_bits[j]))
            j += 1
    return result

def set_parity_bits(bits):
    n = len(bits)
    r = 0
    while (2 ** r) <= n:
        r += 1
    for i in range(r):
        pos = 2 ** i
        if pos - 1 >= n:
            continue
        parity = 0
        for j in range(1, n + 1):
            if j & pos:
                parity ^= bits[j - 1]
        bits[pos - 1] = parity
    return bits

def add_overall_parity(bits):
    overall = sum(bits) % 2
    return bits + [overall] 

def encode(data_bits_str):
    if len(data_bits_str) not in [8, 16, 32]:
        raise ValueError("Yalnızca 8, 16 veya 32 bit veri destekleniyor.")

    data_bits = [int(b) for b in data_bits_str]
    with_parity = insert_parity_positions(data_bits)
    with_parity = set_parity_bits(with_parity)
    full_code = add_overall_parity(with_parity)
    return full_code

def calculate_overall_parity(bits):
    return sum(bits) % 2

from hamming import set_parity_bits, add_overall_parity

def decode(hamming_code):
    original = hamming_code.copy()
    n = len(original) - 1  # overall parity hariç uzunluk
    data_with_parity = original[:n]
    overall_received = original[-1]
    overall_calculated = sum(data_with_parity) % 2

    # Parity bit sayısını hesapla
    r = 0
    while (2 ** r) <= n:
        r += 1

    # Sendromu hesapla (bitwise shift ile)
    syndrome = 0
    for i in range(r):
        val = 0
        bit_mask = 2 ** i
        for j in range(1, n + 1):
            if j & bit_mask:
                val ^= data_with_parity[j - 1]  # Burada normal indeksleme kullandım
        syndrome |= (val << i)  # bitwise OR ile gönderilen bit konumu

    error_position = syndrome
    corrected_data = data_with_parity.copy()

    if error_position == 0 and overall_received == overall_calculated:
        error_type = "Hata yok"
    elif error_position != 0 and overall_received != overall_calculated:
        error_type = "Tek bit hatası"
        bit_index = error_position - 1
        if 0 <= bit_index < len(corrected_data):
            corrected_data[bit_index] ^= 1
    elif error_position == 0 and overall_received != overall_calculated:
        error_type = "Overall parity bitinde hata"
        overall_received ^= 1
    elif error_position != 0 and overall_received == overall_calculated:
        error_type = "Çift bit hatası (düzeltilemez)"
    else:
        error_type = "Tanımsız hata"

    return {
        "corrected_code": corrected_data + [overall_received],
        "error_position": error_position,
        "error_type": error_type
    }

