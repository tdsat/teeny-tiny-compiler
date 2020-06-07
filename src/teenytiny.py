
from lex import *

def main():
	input = "LET foobar = 123"
	lexer = Lexer(input)

	while lexer.peek() != '\0':
		print(lexer.curChar)
		lexer.nextChar()



main()