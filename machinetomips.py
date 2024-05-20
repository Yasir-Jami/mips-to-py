# Determine the mips instruction from an encoded machine instruction (in hex)
# Provided machine code must be in hex
def machine_to_mips(code, type):
  #hexlist = []
  #for i in range(2, len(code)):
  #  hexlist.append(code[i])
  code = bin(code[2:])  # Convert hex value to bin

  ops = {
    # when opcode is 000000, op determined by other fields
    "000010": "j",
    "000011": "jal",
    "000100": "baq",
    "000101": "bne",
    "000110": "blez",
    "000111": "bgta",
    "001000": "addi",
    "001001": "addiu",
    "001010": "situ",
    "001011": "sltiu",
    "001100": "andi",
    "001101": "ori",
    "001110": "xori",
    "001111": "lui",

    "100000": "lb",
    "100001": "lh",
    "100010": "lwl",
    "100011": "lw",
    "100100": "lbu",
    "100101": "lhu",
    "100110": "lwr",
    "100111": "", # unknown/blank/reserved (not sure what this is)
    "101000": "sb",
    "101001": "sh",
    "101010": "swl",
    "101011": "sw"
    }
  
  registers = {
    "00000": "$zero",
    # Skip $at, reserved for assembler
    "00010": "$v0",
    "00011": "$v1",
    "00100": "$a0",
    "00101": "$a1",
    "00110": "$a2",
    "00111": "$a3",
    "01000": "$t0",
    "01001": "$t1",
    "01010": "$t2",
    "01011": "$t3",
    "01100": "$t4",
    "01101": "$t5",
    "01110": "$t6",
    "01111": "$t7",
    "10000": "$s0",
    "10001": "$s1",
    "10010": "$s2",
    "10011": "$s3",
    "10100": "$s4",
    "10101": "$s5",
    "10110": "$s6",
    "10111": "$s7",
    "11000": "$t8",
    "11001": "$t9",
    # Skip $k0 and $k1 (reserved for OS)
    "11100": "$gp",
    "11101": "$sp",
    "11110": "$fp",
    "11111": "$ra"
  }

  # funct field "000000": "",
  functs = {
    "000000": "sll",
    "000010": "",
    "000100": "srl",
    "000110": "sra",
    "001000": "sllv",
    "000000": "",
    "000000": "",
    "000000": "",
    "000000": "",
    "000000": "",
    "000000": "",

  }

  opcode = code[0:7]  # 6 bits for all types
  # Register type
  # 6 bits - op code
  # 5 bits - rs
  # 5 bits - rt
  # 5 bits - rd
  # 5 bits - shamt
  # 6 bits - funct  
  if type == "r":
    print("Register type")
    # 5 bit field reserved for registers
    rs = code[7:13]
    rt = code[13:19]
    rd = code[19:25]
    #if opcode == "000000":
    #  funct = code[0] # change this
    #  print()

    print(ops[opcode], )

  # Immediate type
  # 6 bits - op code
  # 5 bits - rs
  # 5 bits - rt
  # 16 bits - immediate
  elif type == "i":
    print("Immediate type")

  # Jump type
  # 6 bits - opcode
  # 26 bits - target address
  elif type == "j":
    print("Jump type")

def user_input():
  machine_code = str(input("Enter a value in the format 0x00000000): "))
  while True:
    if machine_code[0:2] != "0x" or machine_code[2:] not in "0123456789ABCDEF":
      machine_code = str(input("Try again. Enter a value in the format 0x00000000): "))
    else:
      break

  type = input("Enter the instruction type (r/i/j): ")
  while True:
    if type not in "rij":
      machine_code = str(input("Try again. Enter the instruction type (r/i/j): "))
    else:
      break
  return machine_code, type

if __name__ == "__main__":
    pass
    # Register type, branch type, immediate type
    #code, type = user_input()
    #machine_to_mips(code, type)

    # Test with : 0x000a2021 (addu $4, $0, $10 OR move $a0, $t2)