## File 1
- open AudioViz.1.toe
- explain terminology:
	- CV: controlvoltage
	- Gate: on/off value
	- VCO: Voltage Controlled Oscillator - Voltage controls the pitch
	- VCF: Voltage Controlled Filter - Voltage Controls the cutoff or bypass frequency
	- VCA: Voltage Controlled Amplifier - literally a multiplication of one value with another
	- Envelope Generator: also called a ADSR which stands for Attack, Decay, Sustain and Release
- Add 2 Audio Oscillator CHOPs and set their type to Ramp and Square
- Turn down your Speakers, append an Audio Device Out and listen in. 
- Combine the 2 Oscillator CHOPs using a Math CHOP
- See how the Amplitude is now -2 to plus 2 --> something Audio doesn't like
- Add Audio Dynamics CHOP and enable Limiter
- Append an Audio Filter CHOP
	- Low Pass: everything below Frequency is passed
	- High Pass: everything above Frequency is passed
	- Band Pass: everything around Frequency is passed
	- Band Reject: specified Frequency is cut
	- Look at Logarithmic Frequency Control over Linear
- Append and Audio Oscillator CHOP to watch Filter effect
- Append Math CHOP as the VCA

## File 2.
- Explore Gates and Envelopes
- Add a Button COMP and set Type to Momentary
- Activate Viewer of Button so we can click it
- Append a Trail CHOP to see the state value of the Button
- Append an Trigger CHOP on Button and explore default behaviour through trail
	- Especially explore what Sustain means
- Set the values of the trigger to control the filter to: 
	- Attack Length: 0.06 S
	- Peak Length: 0
	- Decay Length: 0.06
	- Release Length: 0.3
	- Decay Shape: Ease Out
- As we are using Logarithmic values in the Filter, append a math and convert the range from 0-1 to 4-2
- Try out what different Filter types do to the Sound
- Add another trigger to contrl the VCA:
	- Attack Length: 0.08
	- Peak Length: 0.1
	- Decay Length 0.17
	- Release Length: 0.3
	
## File 3.
- Controlling Pitch via the Input to the Oscillator
- Add a Panel CHOP and reference Button to get Panel u and v value
- Use Select CHOPs to control osc1 with u and osc2 with v
- Going stereo: copy everything to audio dynamics CHOP and create second chain
- Use Merge CHOP to bring both chains together
- Change all the oscillator frequencies to individual ones: 440, 555, 160, 990

## File 4.
- Look at it through X/Y scope
- Append a Null CHOP to Audio Dynamics
- Append a CHOP To SOP to Null CHOP
- Fix the warnings
- Create Render Setup:
- Append Geo COMP to ChopTo SOP
- Add Camera, Constant Material and Render TOP (render to parent panel size)
- Add a Null TOP and call it bg
- Open Parent Viewer and Parent Parameters
- Set the BG TOP parameter
- Place a new Panel CHOP and select u, v and select
- Replace the Button as a source with the panel and control Synth from Panel

## File 5.
- Add a Feedback effect

## File 6.
- Add Particles
- Control by Leap Motion or Zig Sim
