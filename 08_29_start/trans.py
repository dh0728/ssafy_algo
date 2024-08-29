
def dec_to_bin(num):
    bin_number=''

    if num==0:
        return '0'

    while num > 0:
        remainer = num % 2
        bin_number = str(remainer) + bin_number
        num = num // 2

    return bin_number

def dec_to_hex(num):
    hex_digits = '0123456789ABCDEF'
    hex_number = ''

    if num ==0:
        return '0'

    while num > 0:
        remainer = num % 16
        hex_number = str(hex_digits[remainer])+hex_number
        num //= 16
    return hex_number


decimal_num = 26
binary_num = dec_to_bin(decimal_num) # 10진수을 2진수로
hex_num = dec_to_hex(decimal_num)    # 10진수을 16진수로

print(f"{decimal_num} - 2진수: {binary_num}")
print(f"{decimal_num} - 16진수: {hex_num}")