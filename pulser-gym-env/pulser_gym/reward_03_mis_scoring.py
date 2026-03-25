import numpy as np

def calculate_mis_reward(state_array: np.ndarray) -> float:
    """
    Calculates the Maximum Independent Set (MIS) score for a given measured quantum state.
    Strictly adheres to the Single Responsibility Principle: evaluates graph penalties.
    
    Args:
        state_array (np.ndarray): 1D array of 1s and 0s representing the measured state bitstring.
        
    Returns:
        float: Evaluated MIS score reflecting independent set node selection.
    """
    score = 0.0
    n = len(state_array)
    
    # Loop 1: Reward +1.0 for every node selected (excited atom)
    for i in range(n):
        if state_array[i] == 1:
            score += 1.0
            
    # Loop 2: Penalize -2.0 for every pair of adjacent excited nodes
    for i in range(n - 1):
        if state_array[i] == 1 and state_array[i+1] == 1:
            score -= 2.0
            
    return float(score)
