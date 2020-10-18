
#ifndef ARDUINO_ROMPLER_FINAL_FASTIO_HPP
#define ARDUINO_ROMPLER_FINAL_FASTIO_HPP

#include <Arduino.h>

void digitalWriteFast(uint8_t pin, volatile uint8_t *port, uint8_t value);

#endif //ARDUINO_ROMPLER_FINAL_FASTIO_HPP
