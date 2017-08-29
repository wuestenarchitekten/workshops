# The function below is called when any passed values have changed.
# Be sure to turn on the related parameter in the DAT to retrieve these values.
#
# me - this DAT
# renderPickDat - the connected Render Pick DAT
#
# events - a list of named tuples with the fields listed below.
# eventsPrev - a list of events holding the eventsPrev values.
#
#	u				- The selection u coordinate.			(float)
#	v				- The selection v coordinate.			(float)
#	select			- True when a selection is ongoing.		(bool)
#	selectStart		- True at the start of a selection.		(bool)
#	selectEnd		- True at the end of a selection.		(bool)
#	selectedOp		- First picked operator.				(OP)
#	selectedTexture	- Texture coordinate of seleectedOp.	(Position)
#	pickOp			- Currently picked operator.			(OP)
#	pos				- 3D position of picked point.			(Position)
#	texture			- Texture coordinate of picked point.	(Position)
#	color			- Color of picked point.				(4-tuple)
#	normal			- Geometry normal of picked point.		(Vector)
#	depth			- Post projection space depth.			(float)
#	instanceId		- Instance ID of the object.			(int)
#	row				- The row associated with this event	(float)
#	inValues		- Dictionary of input DAT strings for the given row, where keys are column headers. (dict)
#	custom  		- Dictionary of selected custom attributes

def onEvents(renderPickDat, events, eventsPrev):

	for event, eventPrev in zip(events, eventsPrev):
	
		if event.selectStart and event.row == 1:
			parent().Toggle(event.instanceId,start=True)
			
		elif event.select:
			if event.row == 1:
				parent().Toggle(event.instanceId)
			if event.row == 2:
				op('roll').par.value0 = event.instanceId
				
		elif event.selectEnd:
			if event.row == 1:
				parent().Toggle(-1, end=True)
			if event.row == 2:
				op('roll').par.value0 = -1

	return

	