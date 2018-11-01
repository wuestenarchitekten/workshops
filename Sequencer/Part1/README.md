Setup a Render
--------------
- Create a Container COMP with size 400x400
- Place a Rectangle SOP and rclick connect to a Geometry COMP
- Create a Camera and a Render 
- Reference parent panel size for Render resolution
- Reference a Constant Material to the Geo
- Add a out TOP, name bg and reference as bg TOP to parent

Make it an Instance Grid
------------------------
- Create a Grid SOP
- Convert to CHOP and use for instancing
- On the parent create a custom page and parameters for
	- Layers
	- Bars
	- Step per Bar
- Total number of btns is Layers * Bars * Step per Bar
- Layers can be used as Grid Row Number
- Bars*Step per Bar can be used as Col Number


Add Textures for different states
---------------------------------
- Create Base COMP with 4 different colors named
	- 0Default
	- 1Roll
	- 2Selected
	- 3RollSelected
- In main network add constant CHOP, name channel texId and 
- Connect constant to position merge to feed it to instancing
- Test coloring of rectangles
- For rollover behaviour, add fan after constant with
	- Channel names = 'roll[1-{0:.0f}]'.format(layers*bars*steps)
	- Shuffle and sequence all channels
	- Rename to make channel texId again
- For select, add a Table DAT, convert to CHOP with Channel Per Row, Values, Names
- To sort the selected values correctly, use a replace CHOP and have an constant CHOP in the first input with same expression as Fan CHOP
- Shuffle output of replace and add together with rollover and use as texture Id in instance Geo

Drive the Sequencer
-------------------
- Add a Beat CHOP and output Count + Ramp
- We need to loop this value around the number of Bars with a Limit CHOP
- Now multiply by the number of steps per bar and convert to integer (floor)
- Append a Fan CHOP and fan it out to 'chan[1-{0:.0f}]'.format(bars*steps)
- Shuffle and shift --> this gives us 1 Layer, we need 8 which we can get by
- Appending and extend CHOP and a Trim CHOP to lengthen the CHOP.
- Merge into the add for texture ID

How to Renderpick
-----------------
- We will be using renderpick DAT as we can watch multiple panel values in one OP
- Input to renderpick needs to be a table with columns: select, u and v
- For the sequencer we need a select and rollover action
- Place a Panel CHOP and select channels: select, u, v, inside, insideu, insidev
- Connect a shuffle and sequence Every 3rd Channel
- Convert to Dat and use as input to renderpick
- We want the instance ID - so turn on Fetch Instance ID from Renderpick
- Add in callback for rollover

Adding an Extension
-------------------
- On parent() customize Component and add Extension called Sequencer
- Load extension and explain
- Call Toggle function from renderpick callbacks
	
Outputting control signals
--------------------------
- Every step should cause a pulse but we don't have enough resolution
- Use a Stretch CHOP to scale the legnth of the channel and use No Interpolation
- Create a Pattern CHOP with Type Pulse and Number of Cycles being half the number of Samples of the input
- Multiply the 2
- Split the channel with a Shuffle CHOP every (bars*steps*s) Samples
- Get a value from the Beat CHOP chain and use as index in a lookup CHOP
- Specify the index range to be (bars*steps*2)-1
- Append an Out CHOP
