import numpy as np

def calculate_mis_reward(state_array: np.ndarray, coords: np.ndarray, blockade_radius: float = 7.0) -> float:
    """
    Calculates the Maximum Independent Set (MIS) score for a given measured quantum state.
    Strictly adheres to the Single Responsibility Principle: evaluates graph penalties.
    
    Args:
        state_array (np.ndarray): 1D array of 1s and 0s representing the measured state bitstring.
        coords (np.ndarray): 2D array of (x, y) spatial coordinates mapping the physical nodes.
        blockade_radius (float): The maximum physical distance (µm) where adjacent excitations are penalized.
        
    Returns:
        float: Evaluated MIS score reflecting independent set node selection.
    """
    score = 0.0
    n = len(state_array)
    
    # Loop 1: Reward +1.0 for every node selected (excited atom)
    for i in range(n):
        if state_array[i] == 1:
            score += 1.0
            
    # Loop 2: Penalize -2.0 for every pair of physically conflicting nodes (Blockade violation)
    for i in range(n):
        for j in range(i + 1, n):
            if state_array[i] == 1 and state_array[j] == 1:
                dist = np.linalg.norm(coords[i] - coords[j])
                if dist <= blockade_radius:
                    score -= 2.0
            
    return float(score)
