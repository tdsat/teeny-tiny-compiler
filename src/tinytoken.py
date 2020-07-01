import enum

class Token:
	def __init__(self,tokenText,tokenKind):
		self.text = tokenText # The token's actual text. Used for identifiers, strings and numbers
		self.kind = tokenKind # The TokenType that this token is classified as

	@staticmethod
	def checkIfKeyword(tokenText):
		for kind in TokenType:
			if kind.name == tokenText and kind.value >= 100 and kind.value <= 200:
				return kind
		return None


# TokenType is our enum for all the types of token
class TokenType(enum.Enum):
	EOF = -1
	NEWLINE = 0
	NUMBER = 1
	IDENT = 2
	STRING = 3
	# Keywords
	LABEL = 101
	GOTO  =102
	PRINT = 103
	INPUT = 104
	LET = 105
	IF = 106
	THEN = 107
	ENDIF = 108
	WHILE = 109
	REPEAT = 110
	ENDWHILE = 111
	# Operators
	EQ = 201
	PLUS = 202
	MINUS = 203
	ASTERISK = 204
	SLASH = 205
	EQEQ = 206
	NOTEQ = 207
	LT = 208
	LTEQ = 209
	GT = 210
	GTEQ = 211