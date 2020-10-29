#ifndef ARDUINO_ROMPLER_FINAL_SAMPLE_HPP
#define ARDUINO_ROMPLER_FINAL_SAMPLE_HPP

#ifndef WAVETABLE
#define WAVETABLE 2
#endif

#if WAVETABLE == 1
const int SAMPLE_LEN = 128;
const uint8_t sample_data[] = {
        255, 6, 12, 18, 24, 31, 37, 43, 48, 54, 60, 65, 71, 76, 81, 85, 90, 94, 98, 102, 106, 109, 112, 115, 118, 120,
        122, 124, 125, 126, 127, 127, 127, 127, 127, 126, 125, 124, 122, 120, 118, 115, 112, 109, 106, 102, 98, 94, 90,
        85, 81, 76, 71, 65, 60, 54, 48, 43, 37, 31, 24, 18, 12, 6, 255, 249, 243, 237, 231, 224, 218, 212, 207, 201,
        195, 190, 184, 179, 174, 170, 165, 161, 157, 153, 149, 146, 143, 140, 137, 135, 133, 131, 130, 129, 128, 128,
        128, 128, 128, 129, 130, 131, 133, 135, 137, 140, 143, 146, 149, 153, 157, 161, 165, 170, 174, 179, 184, 190,
        195, 201, 207, 212, 218, 224, 231, 237, 243, 249
};


#elif WAVETABLE == 2
// Sine samples generated with Audacity and post processed with
//
// which reduces the sample_len by factor 2 and returns the data in twos complement encoding

const int SAMPLE_LEN = 50;
const uint8_t sample_data[] = {
        0, 16, 31, 47, 61, 75, 87, 98, 107, 115, 121, 125, 127, 127, 125, 121, 116, 108, 99, 88, 75, 62, 47, 32, 16, 0,
        240, 225, 209, 195, 181, 169, 158, 148, 140, 134, 130, 128, 128, 130, 133, 139, 147, 156, 167, 179, 192, 207,
        222, 238
};
#endif //WAVETABLE
#endif //ARDUINO_ROMPLER_FINAL_SAMPLE_HPP
