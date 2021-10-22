class ValidatorCPF:
    def __init__(self, cpf):
        self.cpf = cpf

    def validate_cpf(self):
        cpf = "082338729"

        count = 1
        sum = 0
        for digit in cpf:
            sum += count * int(digit)
            count += 1
            print(sum)
