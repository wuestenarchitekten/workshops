![Raster-Noton Screen](https://github.com/wuestenarchitekten/workshops/blob/master/AudioVis-WaveformPeriod/sample.JPG)

## Translating Amplitude to Period of a waveform
- add a Line SOP with 150 points
- append a Copy SOP and create 270 copies
- offset each copy in y by a small amount
- render the scene

## The Audio Section
- load an audio file
- average stereo channels into mono
- resample so we can work in our frequency domain
  - (new rate, new interval, 270 samples long)
- create a Pattern CHOP with 270 channels
  - (length is 150 samples, control cycles with amp from audio using me.chanIndex as sample Lookup)
- shuffle --> rename and filter

## Putting it together
- a SOPtoCHOP to convert lines to channels
- multiply ty channel with channels from shuffled pattern
- convert back to SOP by using CHOPtoSOP
- add color with channels from pattern

## Animate with Oscilloscope instead of Audio File
