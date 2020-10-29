#include "rompler.hpp"
#include "settings.hpp"
#include "sample.h"
#include "timer.hpp"
#include "fastIO.hpp"
#include "myShiftOutMSBFirst.hpp"

#define BUTTON_PIN 2            // Pin 2 on Arduino Uno
#define PITCH_ENCODER 0         // Pin A0 on Arduino Uno

volatile uint16_t i;
volatile bool startDAC;
volatile bool stopDAC;
int8_t enc;
uint8_t ocr1a;

void readButton(){
    // TODO Refactor so that the sample will not trigger multiple times after pressing the button
    if(stopDAC && !startDAC){
        startDAC = digitalRead(BUTTON_PIN);
        if(startDAC) {
            enc = analogRead(PITCH_ENCODER) >> 3;
            enc -= 64;
            OCR1A = ocr1a + enc;
            stopDAC = false;
        }
    }
}

void setup() {
    digitalWriteFast(DAC_BCK_PIN, &DDRB, HIGH);         // pinMode(11, OUTPUT)
    digitalWriteFast(DAC_DATA_PIN, &DDRB, HIGH);        // pinMode(12, OUTPUT)
    digitalWriteFast(DAC_WORD_SELECT_PIN, &DDRB, HIGH); // pinMode(13, OUTPUT)

    pinMode(BUTTON_PIN, INPUT);
    i = 0;

    startDAC = false;
    stopDAC = true;

    ocr1a = 180;
    init_timer(ocr1a);
}

void loop() {
    readButton();
}

uint8_t getData(){
    // Return the current samples if the the conversion is ongoing and zero if conversion has stopped
    if(startDAC) {
        return pgm_read_byte_near(sample_data + i); // Use PROGMEM for big samples
    }
    return 0;
}

void shiftDACOut() {
    uint8_t curr = getData();
    // Left Channel
    myShiftOutMSBFirst(DAC_DATA_PIN, DAC_BCK_PIN, curr, &PORTB);

    // Right Channel
    digitalWriteFast(DAC_WORD_SELECT_PIN, &PORTB, HIGH);
    digitalWriteFast(DAC_WORD_SELECT_PIN, &PORTB, LOW);

    if(startDAC && !stopDAC) i++;   // Only increase counter when dac is actually emitting samples data

    if(i >= SAMPLE_LEN) {
        startDAC = false;
        stopDAC = true;
        i = 0;
    }
}

ISR(TIMER1_COMPA_vect) {
    //readButton();
    shiftDACOut();
}