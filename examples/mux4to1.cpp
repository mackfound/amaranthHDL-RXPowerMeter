#include <iostream>

// array-based 4-to-1 Multiplexer
int mux4(const int i[], int s1, int s0) { return i[(s1 << 1) | s0]; }

int main() {
    int inputs[] = {10, 20, 30, 40}; // D0, D1, D2, D3
    
    // Example: Select index 3 (binary 11)
    std::cout << "Selected: " << mux4(inputs, 1, 1); // Output: 40
    
    return 0;
}
