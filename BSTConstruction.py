'''
    BST Construction:
    Create a BST class with the following methods:
    contains, insert, remove
    implement the methods

    Time (contains): Avg: O(logN), Worst: O(N)
    Time (insert): Avg: O(logN), Worst: O(N)
    Time (remove): Avg: O(logN), Worst: O(N)
    Space All: O(1) 

    Last Practice: 2022-03-12 16:59:16
'''
class BST:
	def __init__(self, value, left=None, right=None):
		self.value = value
		self.left = left
		self.right = right
		
	def insert(self, value):
		if value < self.value:
			if self.left is None: self.left = BST(value)
			else: self.left.insert(value)
		if value >= self.value:
			if self.right is None: self.right = BST(value)
			else: self.right.insert(value)
	
	def contains(self, value):
		if value == self.value: return True
		elif value < self.value:
			if self.left is None: return False
			else: return self.left.contains(value)
		elif value > self.value:
			if self.right is None: return False
			else: return self.right.contains(value)
	
	def remove(self, value, parent=None):
		if value < self.value:
			if self.left is not None: self.left.remove(value, self)
		elif value > self.value:
			if self.right is not None: self.right.remove(value, self)
		else:
			if self.left is not None and self.right is not None:
				self.value = self.right.getMinValue()
				self.right.remove(self.value, self)
			elif parent is None:
				if self.left is not None:
					self.value = self.left.value
					self.right = self.left.right
					self.left = self.left.left
				elif self.right is not None:
					self.value = self.right.value
					self.left = self.right.left
					self.right = self.right.right
			elif self == parent.left:
				parent.left = self.left if self.left is not None else self.right
			elif self == parent.right:
				parent.right = self.left if self.left is not None else self.right
		return self
	
	def getMinValue(self):
		if self.left is None:
			return self.value
		else: return self.left.getMinValue()
			