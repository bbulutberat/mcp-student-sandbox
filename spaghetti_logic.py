"""
Data processing module with clean code and modular functions.
Handles data transformation, formatting, and logging using SRP principles.
"""

from typing import List
import logging

# Configure logging
logging.basicConfig(
    filename="processing_log.txt",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


PRICE_MULTIPLIER = 1.15
DECIMAL_PLACES = 2


def apply_price_multiplier(value: float, multiplier: float = PRICE_MULTIPLIER) -> float:
    """
    Apply a multiplier to a numeric value.
    
    Args:
        value: The base numeric value
        multiplier: The multiplier to apply (default: 1.15 for 15% increase)
    
    Returns:
        The value after applying the multiplier
    
    Raises:
        TypeError: If value is not numeric
        ValueError: If multiplier is negative
    """
    if not isinstance(value, (int, float)):
        raise TypeError(f"Value must be numeric, got {type(value).__name__}")
    if multiplier < 0:
        raise ValueError(f"Multiplier must be non-negative, got {multiplier}")
    
    return value * multiplier


def format_total(value: float, decimal_places: int = DECIMAL_PLACES) -> str:
    """
    Format a numeric value as a total string.
    
    Args:
        value: The numeric value to format
        decimal_places: Number of decimal places (default: 2)
    
    Returns:
        Formatted string like "Total: 1234.56"
    """
    return f"Total: {value:.{decimal_places}f}"


def display_result(formatted_result: str) -> None:
    """
    Display a formatted result to console.
    
    Args:
        formatted_result: The formatted string to display
    """
    print(formatted_result)


def log_processing_result(processed_values: List[float]) -> None:
    """
    Log the processing results to file and logger.
    
    Args:
        processed_values: List of processed values to log
    """
    logging.info(f"Processed values: {processed_values}")


def process_data(data: List[float]) -> List[float]:
    """
    Process a list of values by applying multiplier transformation.
    
    This function implements separation of concerns by delegating:
    - Calculation to apply_price_multiplier()
    - Formatting to format_total()
    - Display to display_result()
    - Logging to log_processing_result()
    
    Args:
        data: List of numeric values to process
    
    Returns:
        List of processed values
    
    Raises:
        TypeError: If data contains non-numeric values
    """
    if not isinstance(data, (list, tuple)):
        raise TypeError(f"Data must be a list or tuple, got {type(data).__name__}")
    
    processed_results = []
    
    for raw_value in data:
        # Calculate
        processed_value = apply_price_multiplier(raw_value)
        
        # Format
        formatted_message = format_total(processed_value)
        
        # Display
        display_result(formatted_message)
        
        # Store
        processed_results.append(processed_value)
    
    # Log
    log_processing_result(processed_results)
    
    return processed_results
