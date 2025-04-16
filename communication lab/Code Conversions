#hexadecimal to binary
def hex_to_binary(hex_num):
    binary_num=bin(int(hex_num,16))[2:]
    return binary_num
a=hex_to_binary("B24D")
print("Corresponding binary:",a)

#octal to binary
def oct_to_binary(oct_num):
    binary__num=bin(int(oct_num,8))[2:]
    return binary__num
b=oct_to_binary("41")
print("correspondig binary:",b)

#binary to gray
def binary_to_gray(binary):
    gray = binary[0]  # First bit remains the same
    for i in range(1, len(binary)):
        gray += str(int(binary[i-1]) ^ int(binary[i]))  # XOR of consecutive bits
    return gray
decimal_number = 20220919  # Example decimal number
binary_representation = bin(decimal_number)[2:]  # Convert to binary (remove '0b' prefix)
gray = binary_to_gray(binary_representation)  # Convert binary to Gray code

print(f"Decimal: {decimal_number}")
print(f"Binary: {binary_representation}")
print(f"Gray Code: {gray}")

#decimal to BCD
def decimal_to_bcd(decimal_num):
    bcd = ''
    for digit in str(decimal_num):
        bcd_digit = bin(int(digit))[2:].zfill(4)  # Convert each digit to 4-bit binary
        bcd += bcd_digit+" "
    return bcd.strip()
num=41
bcd=decimal_to_bcd(num)
print(bcd)

#decimal to excess 3
def decimal_to_excess3(decimal_num):
    excess3 = ''
    for digit in str(decimal_num):
        xs3_value = int(digit) + 3
        xs3_bin = bin(xs3_value)[2:].zfill(4)
        excess3 += xs3_bin + " "
    return excess3.strip()
