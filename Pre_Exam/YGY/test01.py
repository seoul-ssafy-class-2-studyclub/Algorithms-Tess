from typing import List, Text # 힌트제공하는 라이브러리

# 2
class WordMachine:
    def __init__(self):
        self.stack = list()

    def peek(self):
        if len(self.stack):
            return self.stack[-1]
        else:
            raise StackUnderflowError()

    def number_range_check(self, number):
        if 0 <= number < 2 ** 20:
            return True
        else:
            raise UnsignedIntegerError()

    def add_number(self, number):
        if self.number_range_check(number):
            self.stack.append(number)

    def pop(self):
        if len(self.stack):
            return self.stack.pop()
        else:
            raise StackUnderflowError()

    def duplicate(self):
        self.stack.append(self.peek())

    def sum_number(self):
        plus_number = self.pop() + self.pop()
        if self.number_range_check(plus_number):
            self.stack.append(plus_number)

    def sub_number(self):
        first_number = self.pop()
        second_number = self.pop()
        minus_number = first_number - second_number
        if self.number_range_check(minus_number):
            self.stack.append(minus_number)

    def operate(self, operation):
        if operation.isdecimal():
            self.add_number(int(operation))
        elif operation == "POP":
            self.pop()
        elif operation == "DUP":
            self.duplicate()
        elif operation == "+":
            self.sum_number()
        elif operation == "-":
            self.sub_number()
        else:
            raise UnknownOperationError()


class StackUnderflowError(Exception):
    def __str__(self):
        return "Stack Underflow Error"


class StackOverflowError(Exception):
    def __str__(self):
        return "Stack Overflow Error"


class UnsignedIntegerError(Exception):
    def __str__(self):
        return "Unsigned Integer Error"


class UnknownOperationError(Exception):
    def __str__(self):
        return "Unknown Operation Error"


def solution(S):
    word_machine = WordMachine()
    for operation in S.split(" "):
        try:
            word_machine.operate(operation)
        except (StackOverflowError, StackUnderflowError,
                UnsignedIntegerError, UnknownOperationError):
            return -1
    return word_machine.peek()


# 1
class NoAgentFoundException(Exception):
    def __str__(self):
        return "No Agent Found Exception Error"

class Agent(object):
    def __init__(self, name, skills, load):
        self.name = name
        self.skills = skills
        self.load = load

    def __str__(self):
        return "<Agent: {}>".format(self._name)


class Ticket(object):
    def __init__(self, id, restrictions):
        self.id = id
        self.restrictions = restrictions


class FinderPolicy(object):
    def _filter_loaded_agents(self, agents: List[Agent]) -> List[Agent]:
        return list(filter(lambda agent: 0 < len(agent.skills) <= 3), agents)

    def find(self, ticket: Ticket, agents: List[Agent]) -> Agent:
        return agents[0]


class LeastLoadedAgent(FinderPolicy):
    def find(self, ticket: Ticket, agents: List[Agent]) -> Agent:
        if not agents:
            raise NoAgentFoundException
        return sorted(agents, key=lambda agent: agent.load)[0]


class LeastFlexibleAgent(FinderPolicy):
    def find(self, ticket: Ticket, agents: List[Agent]) -> Agent:

        available_agents = list(filter(lambda agent: set(ticket.restrictions).issubset(set(agent.skill)), agents))
        if not available_agents:
            raise NoAgentFoundException

        available_agents = sorted(available_agents, key=lambda agent: (agent.load, len(agent.skills)))
        return available_agents[0]
