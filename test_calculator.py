from calculator import add, subtract, multiply, divide

def test_add():
	assert add(2, 3) == 5

def test_divide():
	assert divide(6, 2) == 3

def test_subtract():
	assert subtract(7, 2) == 5

def test_multiply():
	assert multiply(3, 7) == 21

def test_divide_uneven():
	# Arrange
	a, b = 5, 2
	# Act
	result = divide(a,b)
	# Assert
	assert result == 2.5
