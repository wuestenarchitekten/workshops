"""
Extension classes enhance TouchDesigner component networks with python
functionality. An extension can be accessed via ext.ExtensionClassName from
any operator within the extended component. If the extension is "promoted", all
its attributes with capitalized names can be accessed directly through the
extended component, e.g. op('yourComp').ExtensionMethod()
"""

class Sequencer:
	"""
	Sequencer description
	"""
	def __init__(self, ownerComp):
		# The component to which this extension is attached
		self.ownerComp = ownerComp
		self.SelectActive = False
		self.LastSelect = None

	def Toggle(self, btnId,start=False,end=False):

		if btnId != -1 and self.LastSelect != btnId:
			allActive = [int(x[0].val) for x in op('on').rows()]
			if btnId not in allActive:
				if allActive:
					allActive.append(btnId)
				else:
					allActive = [btnId]
			else:
				allActive.pop(allActive.index(btnId))
			op('on').clear()
			for i in allActive:
				op('on').appendRow(i)
		self.LastSelect = btnId

		if start:
			self.SelectActive = True
			self.LastSelect = btnId
		elif end:
			self.SelectActive = False
			self.LastSelect = None
			btnId = -1