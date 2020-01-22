class Node:
	def __init__(self,dataval):
		self.dataval = dataval
		self.leftchild = None
		self.rightchild = None


class Bi_tree:
	def __init__(self):
		self.rootval = None
		self.queue = [] #将节点的值存放在列表中
	def creat(self,newdata):
		Newnode = Node(newdata)
		if self.rootval == None:
			self.rootval = Newnode
			self.queue.append(self.rootval)
		else:
			laste = self.queue[0]
			# print(laste.dataval)
			if laste.leftchild == None:
				laste.leftchild = Newnode
				self.queue.append(laste.leftchild)
			else:
				laste.rightchild = Newnode
				self.queue.append(laste.rightchild)
				#如果该结点存在右子树，将此结点丢弃。
				self.queue.pop(0)

		#先序遍历
	def pre_order(self,rootval):
		#主要是利用递归算法
		#第一步：临界点---有回
		if rootval == None:
			return None
		#第二步：算法（根节点->左子树->右子树）---可去
		print(rootval.dataval,end=' ')
		self.pre_order(rootval.leftchild)
		self.pre_order(rootval.rightchild)
	def mid_order(self,rootval):
		#主要利用递归算法
		#第一步：临界点---有回
		if rootval == None:
			return None
		#第二步：算法（左子树->根节点->右子树）
		self.pre_order(rootval.leftchild)
		print(rootval.dataval,end=' ')
		self.pre_order(rootval.rightchild)
	def post_order(self,rootval):
		if rootval == None:
			return None
		self.pre_order(rootval.leftchild)
		self.pre_order(rootval.rightchild)
		print(rootval.dataval,end=' ')
	#层次遍历----广度优先遍历
	def level_order(self,rootval):
		if rootval is None:
			return None
		q = []
		# 首先将根节点入队
		q.append(rootval)
		# 列表为空时，循环终止
		while len(q) != 0:
			length = len(q)
			for i in range(length):
				# 将同层节点依次出队
				r = q.pop(0)
				if r.leftchild is not None:
				# 非空左孩子入队
					q.append(r.leftchild)
				if r.rightchild is not None:
					# 非空右孩子入队
					q.append(r.rightchild)
				print(r.dataval)

if __name__ == '__main__':
	li = Bi_tree()
	li.creat('1')
	li.creat('2')
	li.creat('3')
	li.creat('4')
	li.creat('5')
	# li.pre_order(li.rootval)
	# li.mid_order(li.rootval)
	# li.post_order(li.rootval)
	li.level_order(li.rootval)
