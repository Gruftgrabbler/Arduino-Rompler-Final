#include "timer.hpp"

void init_timer(uint8_t ocr1a) {
    // According to my measurements the highest interrupt frequency the arduino can handle the shiftDACOut function
    // is 38528Hz

    // Tutorial: https://www.instructables.com/Arduino-Timer-Interrupts/
    cli();              // Disable interrupts during initialisation
    TCCR1A = 0;         // Reset Timer 1 Counter Control Register A
    TCCR1B = 0;         // Reset Timer 1 Counter Control Register B
    TCNT1 = 0;          // Initialized counter value = 0
    // OCR1A = (frequency_clock / (pre_scalar * frequency_interrupt)) - 1
    // OCR1A = (frequency_clock / (pre_scalar * (tone_frequency * interrupts_per_cycle)))) - 1
    // OCR1A = (16Mhz / (8 * (301 * 128)) -1)

    // EDIT:
    // OCR1A = (16Mhz / (8 * 440 * 32) - 1) For SAMPLE_LEN = 32
    // OCR1A = 141

    OCR1A = ocr1a;          // Set Timer 1 Output Compare Register -  bounds

    TCCR1B |= (1 << WGM12); // Turn on CTC (clear timer on compare match) mode
    TCCR1B |= (0 << CS12) | (1 << CS11) | (0 << CS10);  // pre_scalar = 8

    TIMSK1 |= (1 << OCIE1A);        // Enable timer compare interrupt
    sei();                          // enable interrupts after initialisation
}