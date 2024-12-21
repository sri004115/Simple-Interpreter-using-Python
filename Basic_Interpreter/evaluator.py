class Environment:
    #elevator
    def __init__(self):
        self.variables = {}

    def get(self, var_name):
        return self.variables.get(var_name)

    def set(self, var_name, value):
        self.variables[var_name] = value

class Evaluator:
    def __init__(self, environment):
        self.environment = environment

    def evaluate(self, node):
        if isinstance(node, int):
            return node
        elif isinstance(node, str):  # Variable reference
            return self.environment.get(node)
        elif isinstance(node, tuple):  # Binary operation
            left, op, right = node
            left_value = self.evaluate(left)
            right_value = self.evaluate(right)
            if op[0] == 'PLUS':
                return left_value + right_value
            elif op[0] == 'MINUS':
                return left_value - right_value
            else:
                raise ValueError(f"Unsupported operator: {op[0]}")