#include "rompler.hpp"
#include "settings.hpp"
#include "sample.hpp"
#include "timer.hpp"
#include "fastIO.hpp"
#include "myShiftOutMSBFirst.hpp"

#define BUTTON_PIN 2            // Pin 2 on Arduino Uno

volatile uint16_t i;
volatile bool startDAC;
volatile bool stopDAC;

void readButton(){
    if(stopDAC && !startDAC){
        startDAC = digitalRead(BUTTON_PIN);
        if(startDAC)
            stopDAC = false;
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

    uint8_t ocr1a = 51;
    init_timer(ocr1a);
}

void loop() {
    readButton();
}

uint8_t getData(){
    // Return the current sample if the the conversion is ongoing and zero if conversion has stopped
    if(startDAC) {
        //return pgm_read_byte_near(sample_data + i); // Use PROGMEM for big samples
        return sample_data[i];
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

    if(startDAC && !stopDAC) i++;   // Only increase counter when dac is actually emitting sample data

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