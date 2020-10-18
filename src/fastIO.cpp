#include "fastIO.hpp"

void digitalWriteFast(uint8_t pin, volatile uint8_t *port, uint8_t value) {
    if (value)
        *port |= (1 << pin);
    else
        *port &= ~(1 << pin);
}