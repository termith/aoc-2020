"""
Each line gives the password policy and then the password.
The password policy indicates the lowest and highest number of times a given letter must appear for the password to be valid.
For example, 1-3 a means that the password must contain a at least 1 time and at most 3 times.

P1 How many passwords are valid according to their policies?
"""
import abc


class Policy:
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def validate(self, password: str) -> bool:
        raise NotImplementedError


class MinMaxPolicy(Policy):

    def __init__(self, str_policy: str) -> None:
        splitted = str_policy.split()
        self.letter = splitted[1]
        minmax = splitted[0]
        self.min_count, self.max_count = map(int, minmax.split('-'))

    def validate(self, password):
        letter_count = 0
        for l in password:
            if l == self.letter:
                letter_count += 1
                if letter_count > self.max_count:
                    return False
        return letter_count >= self.min_count


class PositionPolicy(Policy):

    def __init__(self, str_policy: str) -> None:
        splitted = str_policy.split()
        self.letter = splitted[1]
        positions = splitted[0]
        self.first_position, self.second_position = map(lambda x: int(x) - 1, positions.split('-'))

    def validate(self, password: str) -> bool:
        return (password[self.first_position] == self.letter and password[self.second_position] != self.letter) or (
                    password[self.second_position] == self.letter and password[self.first_position] != self.letter)


with open('input') as f:
    data = f.readlines()

count = 0

for line in data:
    policy_str, password = line.split(':')
    count += int(MinMaxPolicy(policy_str).validate(password.strip()))
print(count)
count = 0

for line in data:
    policy_str, password = line.split(':')
    count += int(PositionPolicy(policy_str).validate(password.strip()))

print(count)
