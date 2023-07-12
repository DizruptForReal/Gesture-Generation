# Gesture-Generation
Gesture Generation and recognition for HCI:
Main module: 
  Takes and audio sample, either user recorded using the recorder module or a pre recorded audio.
  Set the mood from the list of possible moods/body languages from the data set
  Generates the output skeleton fram in a .bvh file format supported by softwares like Autodesk MotionBuilder.

RecorderPy:
  Record user audio from default audio input device
  Noise reduction applied to remove background and white noise
  Generate a command with the given audio sample and the motion capture file


