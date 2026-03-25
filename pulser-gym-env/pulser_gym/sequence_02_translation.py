import numpy as np
from pulser import Pulse, Sequence, Register
from pulser.devices import MockDevice
from pulser.waveforms import ConstantWaveform

def build_pulse_sequence(n_qubits: int, action: np.ndarray) -> Sequence:
    """
    Strictly translates a Gym action into a Pasqal Sequence.
    Does not simulate the Sequence (Single Responsibility Principle).
    """
    # Scale normalized action [0.0, 1.0] to physical amplitude [0.0, 10.0] rad/µs
    amplitude = float(action[0]) * 10.0
    
    # Build a 1D Register of atoms spaced by 5 micrometers
    reg = Register.rectangle(1, n_qubits, spacing=5.0)
    
    # Initialize a Sequence using the register and MockDevice
    seq = Sequence(reg, MockDevice)
    
    # Declare a global Rydberg channel
    seq.declare_channel("rydberg_global", "rydberg_global")
    
    # Create the ConstantWaveforms for amplitude and detuning
    amp_wf = ConstantWaveform(duration=1000, value=amplitude)
    det_wf = ConstantWaveform(duration=1000, value=0.0)
    
    # Create the Pulse with Phase 0
    pulse = Pulse(amplitude=amp_wf, detuning=det_wf, phase=0.0)
    
    # Add the pulse to the global Rydberg channel
    seq.add(pulse, "rydberg_global")
    
    return seq
