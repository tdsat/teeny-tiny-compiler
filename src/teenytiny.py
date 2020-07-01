
from lex import Lexer
from parse import Parser
import sys

def main():
	print("Teeny tiny compiler")

	if len(sys.argv) != 2:
		sys.exit("Error: Compiler needs source file as argument")
	with open(sys.argv[1],'r') as inputFile:
		input = inputFile.read()

	# Initialize lexer and parser
	lexer = Lexer(input)
	parser = Parser(lexer)

	parser.program() # Start the parser

	print('Parsing completed')


main()