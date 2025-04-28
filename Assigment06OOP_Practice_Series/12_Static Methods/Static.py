class TemperatureConverter:
    """A utility class for temperature conversions."""
    
    @staticmethod
    def celsius_to_fahrenheit(celsius: float) -> float:
        """Convert Celsius to Fahrenheit.
        
        Args:
            celsius: Temperature in Celsius
            
        Returns:
            Temperature in Fahrenheit
        """
        return (celsius * 9/5) + 32

    @staticmethod
    def fahrenheit_to_celsius(fahrenheit: float) -> float:
        """Convert Fahrenheit to Celsius.
        
        Args:
            fahrenheit: Temperature in Fahrenheit
            
        Returns:
            Temperature in Celsius
        """
        return (fahrenheit - 32) * 5/9

    @staticmethod
    def kelvin_to_celsius(kelvin: float) -> float:
        """Convert Kelvin to Celsius.
        
        Args:
            kelvin: Temperature in Kelvin
            
        Returns:
            Temperature in Celsius
        """
        return kelvin - 273.15

# Demonstration
print("25°C to Fahrenheit:", TemperatureConverter.celsius_to_fahrenheit(25))  # 77.0
print("98.6°F to Celsius:", TemperatureConverter.fahrenheit_to_celsius(98.6))  # 37.0
print("300K to Celsius:", TemperatureConverter.kelvin_to_celsius(300))  # 26.85
#NOTES:
#Just math, no need to create an object. Call it directly with a number.