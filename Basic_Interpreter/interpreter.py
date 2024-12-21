from lexer import Lexer
from parser import Parser
from evaluator import Evaluator, Environment

def interpret(source_code):
    # Step 1: Tokenize the source code
    lexer = Lexer(source_code)
    tokens = lexer.get_tokens()

    # Step 2: Parse the tokens into an AST
    parser = Parser(tokens)
    ast = parser.parse()

    # Step 3: Evaluate the AST
    env = Environment()
    evaluator = Evaluator(env)
    result = evaluator.evaluate(ast)
    
    print("Result:", result)

if __name__ == "__main__":
    # Get input from the user
    code = input("Enter the code to interpret: ")
    interpret(code)
