class ValidatorCPF(object):
    def __init__(self, cpf):
        self.old_cpf = cpf

    def check_cpf_is_valid(self):
        old_cpf = self.old_cpf
        cpf = old_cpf[:9]

        if not self.get_cpf_in_list(old_cpf):
            rest = self.first_cpf_sum(cpf)
            new_cpf = self.second_cpf_sum(rest, cpf)

            return bool(new_cpf == old_cpf)

    def get_cpf_in_list(self, old_cpf):
        cpf_list = [
            "00000000000",
            "11111111111",
            "22222222222",
            "33333333333",
            "44444444444",
            "55555555555",
            "66666666666",
            "77777777777",
            "88888888888",
            "99999999999",
        ]

        if old_cpf in cpf_list:
            return True
        return False

    def first_cpf_sum(self, cpf):
        count = 10
        sum = 0
        for digit in cpf:
            sum += count * int(digit)
            count -= 1

        rest = sum % 11

        if rest > 2:
            rest = 11 - rest

        return rest

    def second_cpf_sum(self, rest, cpf):
        cpf_concat = cpf + str(rest)
        count_with_rest = 11
        sum_with_rest = 0
        for digit in cpf_concat:
            sum_with_rest += count_with_rest * int(digit)
            count_with_rest -= 1

        rest = sum_with_rest % 11

        if rest < 2:
            rest = 0

        else:
            rest = 11 - rest

        new_cpf = cpf_concat + str(rest)

        return new_cpf
