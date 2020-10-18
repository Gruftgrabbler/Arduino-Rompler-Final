#ifndef ARDUINO_ROMPLER_FINAL_ROMPLER_HPP
#define ARDUINO_ROMPLER_FINAL_ROMPLER_HPP

#include <Arduino.h>

extern volatile bool startDAC;
extern volatile bool stopDAC;

void shiftDACOut();

#endif //ARDUINO_ROMPLER_FINAL_ROMPLER_HPP
