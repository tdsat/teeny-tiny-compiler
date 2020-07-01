import sys
from lex import *
from token import *

# Parser object keeps track of current token and checks if the code matches the grammar


class Parser:
	def __init__(self, lexer):
		self.lexer = lexer

		self.curToken = None
		self.peekToken = None
		self.nextToken()
		self.nextToken() # Call this twice to initialize current and peek

	# Return true if the current token matche
	def checkToken(self, kind):
		return kind == self.curToken.kind

	# Return true if the next token matches
	def checkPeek(self, kind):
		return kind == self.peekToken.kind

	# Try to match current token. If not, error. Advances the current token.
	def match(self, kind):
		if not self.checkToken(kind):
			self.abort("Expected " + kind.name + ", got " + self.curToken.kind.name)
		self.nextToken()
		
	# Advances the current token
	def nextToken(self):
		self.curToken = self.peekToken
		self.peekToken = self.lexer.getToken()
		# No need to worry about passing the EOF, lexer handles that

	def abort(self, message):
		sys.exit("Parser error. " + message)

	# Production rules

	# program ::= {statement}
	def program(self):
		print("PROGRAM")

		# Parse all the statements in the program
		while not self.checkToken(TokenType.EOF):
			self.statement()

	# One of the following statements....
	def statement(self):
		# Check the first token to see what kind of statement this is.

		# 'PRINT' (expression | string)
		if self.checkToken(TokenType.PRINT):
			print("STATEMENT-PRINT")
			self.nextToken()

			if self.checkToken(TokenType.STRING):
				# Simple string
				self.nextToken()
			else:
				# Expect an expression
				self.expression()
		elif self.checkToken(TokenType.IF): # "IF" comparison "THEN" nl {statement} "ENDIF" nl
			print("STATEMENT-IF")
			self.nextToken()
			self.comparison()

			self.match(TokenType.THEN)
			self.nl()

			# Zero or more statements in the body

			while not self.checkToken(TokenType.ENDIF):
				self.statement()
			
			self.match(TokenType.ENDIF)

		# Newline
		self.nl()

	# nl ::= '\n' +
	def nl(self):
		print ("NEWLINE")

		# Require at least on newline
		self.match(TokenType.NEWLINE)
		# But we will allow extra newlines too, of course
		while self.checkToken(TokenType.NEWLINE):
			self.nextToken()
	
