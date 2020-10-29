#include <Arduino.h>
#include "settings.hpp"
#include "fastIO.hpp"
#include "timer.hpp"
#include "myShiftOutMSBFirst.hpp"
#include "sineData.h"

volatile uint16_t i;

void setup() {
    digitalWriteFast(DAC_BCK_PIN, &DDRB, HIGH);         // pinMode(11, OUTPUT)
    digitalWriteFast(DAC_DATA_PIN, &DDRB, HIGH);        // pinMode(12, OUTPUT)
    digitalWriteFast(DAC_WORD_SELECT_PIN, &DDRB, HIGH); // pinMode(13, OUTPUT)
    i = 0;

    #if WAVETABLE == 2
    uint8_t ocr1a = 89;
    #else
    uint8_t ocr1a = 51;
    #endif

    init_timer(ocr1a);
}

void loop() {}

void shiftDACOut() {
    unsigned int curr = sample_data[i];
    // Left Channel
    myShiftOutMSBFirst(DAC_DATA_PIN, DAC_BCK_PIN, curr, &PORTB);

    // Right Channel
    digitalWriteFast(DAC_WORD_SELECT_PIN, &PORTB, HIGH);
    digitalWriteFast(DAC_WORD_SELECT_PIN, &PORTB, LOW);

    i++;
    i %= SAMPLE_LEN;
}

ISR(TIMER1_COMPA_vect) {
        shiftDACOut();
}