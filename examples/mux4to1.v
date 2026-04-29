module tb_mux4to1;
    reg a, b, c, d;
    reg [1:0] sel;
    wire y;
    // instantiate Unit Under Test (UUT)
    mux4to1 uut (a, b, c, d, sel, y);

    initial begin
        // initialize Inputs
        a = 0; b = 1; c = 0; d = 1;
        // apply test cases
        sel = 2'b00; #10; // output should be a (0)
        sel = 2'b01; #10; // output should be b (1)
        sel = 2'b10; #10; // output should be c (0)
        sel = 2'b11; #10; // output should be d (1)
        $finish;
    end
endmodule
