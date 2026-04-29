from amaranth import *
from amaranth.back import verilog
from amaranth.sim import Simulator

class Blinky(Elaboratable):
    def __init__(self, max_cnt):
        # parameterize the counter maximum so we can use a huge number
        # for real hardware, and a tiny number for simulation.
        self.max_cnt = max_cnt 
        
        # Top-level output port
        self.led = Signal()

    def elaborate(self, platform):
        m = Module()

        # Create a counter wide enough to hold max_cnt
        counter = Signal(range(self.max_cnt + 1))

        # Synchronous logic (driven by the implicit 'sync' clock domain)
        with m.If(counter == self.max_cnt - 1):
            m.d.sync += [
                counter.eq(0),
                self.led.eq(~self.led) # Toggle the LED
            ]
        with m.Else():
            m.d.sync += counter.eq(counter + 1)

        return m

if __name__ == "__main__":
    
    # VERILOG GENERATION
    # Assuming a 50 MHz clock from the Zynq PS (FCLK_CLK0).
    # Toggling every 25,000,000 cycles gives a 1 Hz blink rate.
    hw_blinky = Blinky(max_cnt=25_000_000)
    
    print("Generating Verilog...")
    v_code = verilog.convert(hw_blinky, ports=[hw_blinky.led])
    with open("blinky.v", "w") as f:
        f.write(v_code)
    print("Successfully generated blinky.v")

    # SIMULATION & VCD GENERATION
    # We use a much smaller max_cnt (e.g., 5) so the simulation runs 
    # instantly and the VCD file is easy to read.
    sim_blinky = Blinky(max_cnt=5)
    
    # Initialize the simulator with our simulation module
    sim = Simulator(sim_blinky)
    
    # Add a clock to the 'sync' domain (1 MHz / 1us period for example)
    sim.add_clock(1e-6)
    
    # Define a simple testbench process that just waits
    def bench():
        # Run for 30 clock cycles to observe a few toggles
        for _ in range(30):
            yield # Tick the clock forward one cycle
            
    sim.add_sync_process(bench)
    
    print("Running simulation...")
    # Run the simulation and write the waveform to a VCD file
    with sim.write_vcd("blinky.vcd"):
        sim.run()
        
    print("Successfully generated blinky.vcd")