# BMW

## Abstract
For those paralyzed from the neck down (quadriplegic), simple tasks such as short-range transportation can pose a major difficulty. The goal of this research is to provide quadriplegic individuals with independent transportation. By using electroencephalogram (EEG), a noninvasive method to measure electrical activities in the brain, the group can create a brain-computer interface (BCI) that will allow the user to control a wheelchair with his or her own thoughts. Components being integrated into the project include a Raspberry Pi 3 (with Bluetooth) and a Neurosky headset, which allows the user to analyze levels of concentration, meditation, and registers blinks. Success in this research setting will be indicated by the ability of a non-paralyzed user to navigate a GoPiGo (a Raspberry Pi connected to motorized wheels) proof-of-concept wheelchair-like device from rest to an indicated ending point using only their thoughts.

## Team Members
 - Alexander Harold Polus
   - Contruction of wheelchair prototype
   - Bluetooth connection
   - Implementing tank drive
 - Sandeep Sagoo 
   - Establishing stable Bluetooth connection
   - Implementing tank drive
 - Anish Sinha
   - Neurosky and EEG signal processing
   - Mapping signal value to motor movements
   - Establishing stable Bluetooth connection
   - Implementing tank drive
 - Shuyue (Yvette) Weng
   - Mapping signal to individual motors for left/right turning
   - Implementing tank drive

## Technology
 - Software
   - Raspbian stretch with desktop
   - Python
 - Hardware
   - Neurosky headset (Borrowing from Dr. De Sa's lab)
   - Raspberry Pi 3 (With built-in Bluetooth)
   - GoPiGo kit (three-wheel motorized car kit meant to connect to Raspberry Pi)
   - Portable charging battery

## Milestones
1. Connecting Neurosky to Raspberry Pi over Bluetooth
2. Printing to the terminal raw EEG values, concentration values, and meditation values of the user wearing the Neurosky
3. Building the GoPiGo
4. Using Neurosky output values to map forward/backward movements on the GoPiGo
5. Mapping Neurosky outputs to individual wheel motors for left/right movements on the GoPiGo
