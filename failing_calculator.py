"""
Calculator module for computing average ratios with safe division handling.
"""

from typing import List, Union


def average_ratios(numbers: List[Union[int, float]]) -> Union[float, None]:
    """
    Calculate the average of 100 divided by each number, skipping zeros.
    
    Args:
        numbers: List of numeric values
    
    Returns:
        Average of ratios (100/number), or None if no valid values to process
    
    Raises:
        ValueError: If input list is empty
        TypeError: If any element is not numeric
    """
    if not numbers:
        raise ValueError("Input list cannot be empty")
    
    # Filter out zeros and validate types
    valid_numbers = []
    skipped_count = 0
    
    for num in numbers:
        if not isinstance(num, (int, float)):
            raise TypeError(f"All elements must be numeric, got {type(num).__name__}")
        
        if num == 0:
            skipped_count += 1
        else:
            valid_numbers.append(num)
    
    # Handle case where all values are zero
    if not valid_numbers:
        print(f"Warning: All {len(numbers)} values are zero, cannot compute ratios")
        return None
    
    # Calculate ratios
    total = sum(100 / num for num in valid_numbers)
    average = total / len(valid_numbers)
    
    # Log skipped values
    if skipped_count > 0:
        print(f"Info: Skipped {skipped_count} zero value(s) during calculation")
    
    return average


# Test with the problematic input
result = average_ratios([10, 5, 0])
if result is not None:
    print(f"Result: {result:.2f}")
