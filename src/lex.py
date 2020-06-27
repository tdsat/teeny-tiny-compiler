import enum
import sys
from token import *

class Lexer:
	def __init__(self, input):
		self.source = input + '\n' # Source code to lex as a string. Append newline to simplify lexing/parsing the last token/statement
		self.curChar = '' # Current character in the string
		self.curPos = -1 # Current position in the string
		self.nextChar()

	# Process the next character
	def nextChar(self):
		self.curPos += 1
		if self.curPos >= len(self.source):
			self.curChar = '\0' #EOF
		else:
			self.curChar = self.source[self.curPos]

	# Return the lookahead character
	def peek(self):
		if self.curPos + 1 >= len(self.source):
			return '\0'
		return self.source[self.curPos + 1]

	# Invalid token found. Print error and exit
	def abort(self,message):
		sys.exit("Lexing error. " + message)

	# Skip whitespace except newlines, which we will use to indicate the end of a statement
	def skipWhitespace(self):
		while self.curChar == ' ' or self.curChar == '\t' or self.curChar == '\n':
			self.nextChar()

	# Skip comments in the code
	def skipComment(self):
		if self.curChar == '#':
			while self.curChar != '\n':
				self.nextChar()

	# Return the next token
	def getToken(self):
		self.skipWhitespace()
		self.skipComment()
		token = None

		# Check the first character of this token to see if we can decide what it is
		# If it is a multiple character operator (e.g., !=), number, identifier, or keyword then we will process the rest
		if self.curChar == '+':
			token = Token(self.curChar, TokenType.PLUS)		
		elif self.curChar == '-':
			token = Token(self.curChar, TokenType.MINUS)
		elif self.curChar == '*':
			token = Token(self.curChar, TokenType.ASTERISK)
		elif self.curChar == '/':
			token = Token(self.curChar, TokenType.SLASH)
		elif self.curChar == '=':
			if self.peek() == '=':
				self.nextChar()
				token = Token('=' + self.curChar, TokenType.EQEQ)
			else:
				token = Token(self.curChar, TokenType.EQ)
		elif self.curChar == '<':
			if self.peek() == '=':
				self.nextChar()
				token = Token('<' + self.curChar, TokenType.LTEQ)
			else:
				token = Token(self.curChar, TokenType.LT)
		elif self.curChar == '>':
			if self.peek() == '=':
				self.nextChar()
				token = Token('>' + self.curChar, TokenType.GTEQ)
			else:
				token = Token(self.curChar, TokenType.GT)
		elif self.curChar == '!':
			if self.peek() == '=':
				self.nextChar()
				token = Token('!=', TokenType.NOTEQ)
			else:
				self.abort('Expected !=, got !' + self.peek())
		elif self.curChar == '\"':
			self.nextChar()
			startPos = self.curPos

			while self.curChar != '\"':
				# Do not allow special characters in the string.
				# No escape characters, newlines, tabs or %
				# We will be using C's printf on this string
				if self.curChar in ['\\','\n','\t','%']:
					self.abort('Invalid string character :' + self.curChar)
				self.nextChar()
			
			tokText = self.source[startPos : self.curPos]
			token = Token(tokText, TokenType.STRING)
		
		elif self.curChar.isdigit():
			# Leading character is digit so this must be a number
			# Get all consecutive digits and decimal if there is one
			startPos = self.curPos
			while self.peek().isdigit():
				self.nextChar()
			if self.peek() == '.':
				self.nextChar()
				
				if not self.peek().isdigit():
					self.abort("Illegal character "+ self.peek() +" found in number")
				
				while self.peek().isdigit():
					self.nextChar()
			
			token = Token(self.source[startPos: self.curPos],TokenType.NUMBER)
		
		elif self.curChar.isalpha():

			startPos = self.curPos
			while self.peek().isalnum():
				self.nextChar()
			
			tokenText = self.source[startPos : self.curPos + 1]
			keyword = Token.checkIfKeyword(tokenText)
			if keyword == None:
				token = Token(tokenText, TokenType.IDENT)
			else:
				token = Token(tokenText,keyword)

		elif self.curChar in ['\n','\r']:
			token = Token(self.curChar, TokenType.NEWLINE)
		elif self.curChar == '\0':
			token = Token('', TokenType.EOF)
		else: 
			#Unknown token!
			self.abort("Unknown token : " + self.curChar)
		
		self.nextChar()
		return token