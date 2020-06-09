
from lex import *

def main():
	input = "+- */ >>= = != #hello\n != \"This is a string !\" 2433444444"
	lexer = Lexer(input)

	token = lexer.getToken()

	while token.kind != TokenType.EOF:
		print(token.kind)
		token = lexer.getToken()



main()