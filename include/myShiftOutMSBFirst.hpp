
#ifndef ARDUINO_ROMPLER_FINAL_MYSHIFTOUTMSBFIRST_HPP
#define ARDUINO_ROMPLER_FINAL_MYSHIFTOUTMSBFIRST_HPP

#include <Arduino.h>
#include <fastIO.hpp>

void myShiftOutMSBFirst(uint8_t data_pin, uint8_t clock_pin, uint16_t val, volatile uint8_t *port);

#endif //ARDUINO_ROMPLER_FINAL_MYSHIFTOUTMSBFIRST_HPP
