Impulse
======
## Music in your hands
![Impulse](/assets/graphics/impulse_logo.jpg)

[![Build Status](https://travis-ci.org/resolutedreamer/Impulse.svg?branch=master)](https://travis-ci.org/resolutedreamer/Impulse)

Impulse is a project created for UCLA's hardware hackathon, IDEA Hacks, which ran January 15th-17th 2016. Impulse is designed to use the Myo armband to control the Kodi music player and synchronize the song being played with RGB LED Lights.

Check it out on YouTube:

[![IMAGE ALT TEXT](http://img.youtube.com/vi/63a6ebVmFpA/0.jpg)](http://www.youtube.com/watch?v=63a6ebVmFpA "Impulse - Demo")

#### Screenshot
![Screenshot](/assets/screenshots/ss1.png)
## Getting Started

### Installation

#### Arduino Client
Use the Arduino IDE to program the Arduino with "Arduino_RGB_Receive.ino"

#### Intel Edison Client
Download the file "edison_rgb_receive.py" onto the Intel Edison device and execute the program.

#### Server
Download the file "Impulse.py" onto the server connected via serial to the Arduino Client, or connected to MongoLab via the internet. Run the program with the path to the wav files that you want to play as command line arguments.

## Contributors

### Contributors on GitHub
* [Anthony Nguyen](https://github.com/resolutedreamer)
* [Eric Du](https://github.com/edu5)
* [Ryan Ho](https://github.com/horyan)
* [Kevin Kim]()
* [Dhiren Lad]()

### Third party libraries
*  [pyserial](https://github.com/pyserial/pyserial)
*  [pyaudio](https://people.csail.mit.edu/hubert/pyaudio/)
*  [scipy](https://www.scipy.org/)
*  [WHEN IT RAINS](http://opsound.org/artist/peterrudenko/)

## License 
* This project is licensed under the Apache License - see the [LICENSE](https://github.com/resolutedreamer/Impulse/blob/master/LICENSE) file for details
* The song WHEN IT RAINS is licenced under [Creative Commons Attribution-ShareAlike license](https://creativecommons.org/licenses/by-sa/3.0/)

## Version 
* Version 1.0

## Contact
#### Anthony Nguyen
* Homepage: [http://www.resolutedreamer.com](http://www.resolutedreamer.com)

Last Updated 2016/08/10
