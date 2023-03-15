#include "MicroBit.h"
#include "ml4f.h"
#include "model.h"

// The Micro:bit control object
MicroBit uBit;


// Out main function, run at startup
int main() {
    uBit.init();

    DMESGF("hello world");

    ml4f_header_t * modelPointer = (ml4f_header_t *) &model;

    float input = 7;
    float output;

    int r = ml4f_full_invoke(modelPointer, &input, &output);

    float outputValue = output;
    outputValue = roundf(outputValue);
    int outputInt = static_cast<int>(outputValue);

    DMESGF("output: %d", outputInt);

    // this is a simple test model that should return 0 if the input is under 10 and 1 otherwise.

    release_fiber();
}