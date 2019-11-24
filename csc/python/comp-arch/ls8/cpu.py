"""CPU functionality."""

import sys
# decalre operands
LDI = 0b10000010
PRN= 0b01000111
HLT = 0b00000001
MUL = 0b10100010 # MUL
PUSH = 0b01000101 # PUSH R0
POP = 0b01000110 # POP R2
CALL = 0b01010000
RET = 0b00010001
ADD = 0b10100000 # ADD R0,R0
class CPU:
    """Main CPU class."""

    def __init__(self):
        """Construct a new CPU."""
        # pass
        self.ram = [0]*256
        self.reg = [0]*8
        self.pc = 0
        self.sp = 7
        self.reg[self.sp] = 0xF4
        self.op_pc = False
        self.branchtable = {}
        self.branchtable[LDI] = self.handle_LDI
        self.branchtable[PRN] = self.handle_PRN
        self.branchtable[HLT] = self.handle_HLT
        self.branchtable[MUL] = self.handle_MUL
        self.branchtable[PUSH] = self.handle_PUSH
        self.branchtable[POP] = self.handle_POP
        self.branchtable[CALL] = self.handle_CALL
        self.branchtable[RET] = self.handle_RET
        self.branchtable[ADD] = self.handle_ADD

    def ram_read(self, address):
        return self.ram[address]

    def ram_write(self, address, data):
        self.ram[address] = data

    def load(self):
        """Load a program into memory."""

        address = 0

        # For now, we've just hardcoded a program:

        # program = [
        #     # From print8.ls8
        #     0b10000010, # LDI R0,8
        #     0b00000000,
        #     0b00001000,
        #     0b01000111, # PRN R0
        #     0b00000000,
        #     0b00000001, # HLT
        # ]
        # program = []
        # check if filename is passed as argument in command line
        if len(sys.argv) != 2:
            print("usage: ls8.py <filename>")
            sys.exit(1)

        try:
            with open(sys.argv[1]) as f:
                for line in f:
                # deal with comments
                # split before and after any comment symbol '#'
                    comment_split = line.split("#")

                # convert the pre-comment portion (to the left) from binary to a value
                # extract the first part of the split to a number variable
                # and trim whitespace
                    num = comment_split[0].strip()

                # ignore blank lines / comment only lines
                    if len(num) == 0:
                        continue

                # set the number to an integer of base 2
                    value = int(num, 2)
                    # program.append(value)
                    self.ram_write(address, value)
                    address += 1
                # print the value in binary and in decimal
                    print(f"{value:08b}: {value:d}")

            # for instruction in program:
            #     self.ram_write(address, instruction)
            #     address += 1
        except FileNotFoundError:
            print(f"{sys.argv[0]}: {sys.argv[1]} not found")
            sys.exit(2)


    def alu(self, op, reg_a, reg_b):
        """ALU operations."""

        if op == "ADD":
            self.reg[reg_a] += self.reg[reg_b]
        #elif op == "SUB": etc
        elif op == "MUL":
            self.reg[reg_a] *= self.reg[reg_b]
        else:
            raise Exception("Unsupported ALU operation")

    def trace(self):
        """
        Handy function to print out the CPU state. You might want to call this
        from run() if you need help debugging.
        """

        print(f"TRACE: %02X | %02X %02X %02X |" % (
            self.pc,
            #self.fl,
            #self.ie,
            self.ram_read(self.pc),
            self.ram_read(self.pc + 1),
            self.ram_read(self.pc + 2)
        ), end='')

        for i in range(8):
            print(" %02X" % self.reg[i], end='')

        print()

    def run(self):
        """Run the CPU."""
        # pass
        IR = self.ram_read(self.pc)
        operand_a = self.ram_read(self.pc + 1)
        operand_b = self.ram_read(self.pc + 2)
        
        running = True
        while running:
            IR = self.ram_read(self.pc)
            operand_a = self.ram_read(self.pc + 1)
            operand_b = self.ram_read(self.pc + 2)
            if IR in self.branchtable:
                self.branchtable[IR](operand_a, operand_b)
            else:
                print(f"Unknown Instruction")
                sys.exit(1)

    
    def handle_LDI(self, op_id1, op_id2):
        self.reg[op_id1] = op_id2
        self.op_pc = False
        if not self.op_pc:
            self.pc += 3 # move to next MAR

    def handle_PRN(self, op_id1, op_id2):
        print(self.reg[op_id1])
        self.op_pc = False
        if not self.op_pc:
            self.pc += 2

    def handle_MUL(self, op_id1, op_id2):
        self.alu("MUL",op_id1, op_id2)
        self.op_pc = False
        if not self.op_pc:
            self.pc += 3 # move to next MAR
    
    def handle_ADD(self, op_id1, op_id2):
        self.alu("ADD",op_id1, op_id2)
        self.op_pc = False
        if not self.op_pc:
            self.pc += 3 # move to next MAR
    
    def handle_PUSH(self, op_id1, op_id2):
        # EXECUTE
        # SETUP
        # PUSH
        self.reg[self.sp] -= 1
        self.ram[self.reg[self.sp]] = self.reg[op_id1]
        self.op_pc = False
        if not self.op_pc:
            self.pc += 2

    def handle_POP(self, op_id1, op_id2):
        # EXECUTE
        # SETUP
        # POP
        self.reg[op_id1] = self.ram_read(self.reg[self.sp])
        self.reg[self.sp] += 1
        self.op_pc = False
        if not self.op_pc:
            self.pc += 2

    def handle_HLT(self, op_id1, op_id2):
        sys.exit()

   
    def handle_CALL(self, op_id1, op_id2):
        # EXECUTE
        # SETUP
        # reg = memory[pc + 1]

        # CALL
        self.reg[self.sp] -= 1 # Decrement Stack Pointer
        # memory[register[SP]] = pc + 2 # Push PC + 2 on to the stack
        self.ram[self.reg[self.sp]] = self.pc + 2

        # set pc to subroutine
        # pc = register[reg]
        self.pc = self.reg[op_id1]
        self.op_pc = True
    def handle_RET(self, op_id1, op_id2):
        self.pc = self.ram_read(self.reg[self.sp])
        self.reg[self.sp] += 1
        self.op_pc = True
