#include "myShiftOutMSBFirst.hpp"


void myShiftOutMSBFirst(uint8_t data_pin, uint8_t clock_pin, uint16_t val, volatile uint8_t *port) {
    uint8_t bit;
    for (bit = 0; bit < 8; bit++)  {

        uint8_t curr = !!(val & (1 << (7 - bit)));
        digitalWriteFast(data_pin, port, curr);  //digitalWrite(data_pin, curr);

        digitalWriteFast(clock_pin, port, HIGH);  //digitalWrite(clock_pin, HIGH);

        digitalWriteFast(clock_pin, port, LOW);   //digitalWrite(clock_pin, LOW);
    }
}