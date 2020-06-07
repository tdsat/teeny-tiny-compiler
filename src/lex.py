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
		pass

	# Skip whitespace except newlines, which we will use to indicate the end of a statement
	def skipWhitespace(self):
		pass

	# Skip comments in the code
	def skipComment(self):
		pass

	# Return the next token
	def getToken(self):
		pass