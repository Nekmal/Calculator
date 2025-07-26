#!/usr/bin/env python3
"""
Calculator Operations Module
Contains all mathematical operations for the complex calculator
"""

import math

class BasicOperations:
    """Basic arithmetic operations"""
    
    def add(self, a, b):
        """Addition operation"""
        return a + b
    
    def subtract(self, a, b):
        """Subtraction operation"""
        return a - b
    
    def multiply(self, a, b):
        """Multiplication operation"""
        return a * b
    
    def divide(self, a, b):
        """Division operation with zero check"""
        if b == 0:
            raise ValueError("Cannot divide by zero!")
        return a / b
    
    def modulus(self, a, b):
        """Modulus operation with zero check"""
        if b == 0:
            raise ValueError("Cannot perform modulus by zero!")
        return a % b
    
    def integer_divide(self, a, b):
        """Integer division with zero check"""
        if b == 0:
            raise ValueError("Cannot divide by zero!")
        return a // b


class AdvancedOperations:
    """Advanced mathematical operations"""
    
    def power(self, base, exponent):
        """Power operation"""
        try:
            result = base ** exponent
            if math.isinf(result):
                raise ValueError("Result is too large!")
            return result
        except OverflowError:
            raise ValueError("Result is too large!")
    
    def square_root(self, number):
        """Square root operation"""
        if number < 0:
            raise ValueError("Cannot calculate square root of negative number!")
        return math.sqrt(number)
    
    def factorial(self, n):
        """Factorial operation"""
        if not isinstance(n, int):
            raise ValueError("Factorial requires an integer!")
        if n < 0:
            raise ValueError("Factorial is not defined for negative numbers!")
        if n > 170:  # Prevent overflow
            raise ValueError("Number too large for factorial calculation!")
        return math.factorial(n)
    
    def logarithm(self, number, base=10):
        """Logarithm operation"""
        if number <= 0:
            raise ValueError("Logarithm is not defined for non-positive numbers!")
        if base <= 0 or base == 1:
            raise ValueError("Invalid logarithm base!")
        
        if base == 10:
            return math.log10(number)
        elif base == math.e:
            return math.log(number)
        else:
            return math.log(number) / math.log(base)
    
    # Trigonometric functions
    def sine(self, angle_degrees):
        """Sine function (input in degrees)"""
        angle_radians = math.radians(angle_degrees)
        return round(math.sin(angle_radians), 10)  # Round to avoid floating point errors
    
    def cosine(self, angle_degrees):
        """Cosine function (input in degrees)"""
        angle_radians = math.radians(angle_degrees)
        return round(math.cos(angle_radians), 10)
    
    def tangent(self, angle_degrees):
        """Tangent function (input in degrees)"""
        # Check for undefined values (90°, 270°, etc.)
        if angle_degrees % 180 == 90:
            raise ValueError("Tangent is undefined at this angle!")
        
        angle_radians = math.radians(angle_degrees)
        return round(math.tan(angle_radians), 10)
    
    # Area calculations
    def rectangle_area(self, length, width):
        """Calculate rectangle area"""
        if length < 0 or width < 0:
            raise ValueError("Dimensions cannot be negative!")
        return length * width
    
    def circle_area(self, radius):
        """Calculate circle area"""
        if radius < 0:
            raise ValueError("Radius cannot be negative!")
        return math.pi * (radius ** 2)
    
    def triangle_area(self, base, height):
        """Calculate triangle area"""
        if base < 0 or height < 0:
            raise ValueError("Dimensions cannot be negative!")
        return 0.5 * base * height
    
    # Unit conversions
    def celsius_to_fahrenheit(self, celsius):
        """Convert Celsius to Fahrenheit"""
        return (celsius * 9/5) + 32
    
    def fahrenheit_to_celsius(self, fahrenheit):
        """Convert Fahrenheit to Celsius"""
        return (fahrenheit - 32) * 5/9
    
    def meters_to_feet(self, meters):
        """Convert meters to feet"""
        if meters < 0:
            raise ValueError("Length cannot be negative!")
        return meters * 3.28084
    
    def feet_to_meters(self, feet):
        """Convert feet to meters"""
        if feet < 0:
            raise ValueError("Length cannot be negative!")
        return feet / 3.28084
    
    def kg_to_pounds(self, kg):
        """Convert kilograms to pounds"""
        if kg < 0:
            raise ValueError("Weight cannot be negative!")
        return kg * 2.20462
    
    def pounds_to_kg(self, pounds):
        """Convert pounds to kilograms"""
        if pounds < 0:
            raise ValueError("Weight cannot be negative!")
        return pounds / 2.20462


class StatisticalOperations:
    """Statistical operations for arrays of numbers"""
    
    def mean(self, numbers):
        """Calculate arithmetic mean"""
        if not numbers:
            raise ValueError("Cannot calculate mean of empty list!")
        return sum(numbers) / len(numbers)
    
    def median(self, numbers):
        """Calculate median"""
        if not numbers:
            raise ValueError("Cannot calculate median of empty list!")
        
        sorted_numbers = sorted(numbers)
        n = len(sorted_numbers)
        
        if n % 2 == 0:
            return (sorted_numbers[n//2 - 1] + sorted_numbers[n//2]) / 2
        else:
            return sorted_numbers[n//2]
    
    def mode(self, numbers):
        """Calculate mode (most frequent value)"""
        if not numbers:
            raise ValueError("Cannot calculate mode of empty list!")
        
        frequency = {}
        for num in numbers:
            frequency[num] = frequency.get(num, 0) + 1
        
        max_frequency = max(frequency.values())
        modes = [num for num, freq in frequency.items() if freq == max_frequency]
        
        return modes if len(modes) > 1 else modes[0]
    
    def standard_deviation(self, numbers):
        """Calculate standard deviation"""
        if len(numbers) < 2:
            raise ValueError("Need at least 2 numbers for standard deviation!")
        
        mean_val = self.mean(numbers)
        variance = sum((x - mean_val) ** 2 for x in numbers) / (len(numbers) - 1)
        return math.sqrt(variance)
    
    def range_calc(self, numbers):
        """Calculate range (max - min)"""
        if not numbers:
            raise ValueError("Cannot calculate range of empty list!")
        return max(numbers) - min(numbers)


class FinancialOperations:
    """Financial calculations"""
    
    def simple_interest(self, principal, rate, time):
        """Calculate simple interest"""
        if principal < 0 or rate < 0 or time < 0:
            raise ValueError("Principal, rate, and time must be positive!")
        return (principal * rate * time) / 100
    
    def compound_interest(self, principal, rate, time, compounds_per_year=1):
        """Calculate compound interest"""
        if principal < 0 or rate < 0 or time < 0 or compounds_per_year <= 0:
            raise ValueError("Invalid input values!")
        
        amount = principal * (1 + rate/100/compounds_per_year) ** (compounds_per_year * time)
        return amount - principal
    
    def percentage_change(self, old_value, new_value):
        """Calculate percentage change"""
        if old_value == 0:
            raise ValueError("Cannot calculate percentage change from zero!")
        return ((new_value - old_value) / old_value) * 100
    
    def tip_calculator(self, bill_amount, tip_percentage, people=1):
        """Calculate tip and split bill"""
        if bill_amount < 0 or tip_percentage < 0 or people <= 0:
            raise ValueError("Invalid input values!")
        
        tip_amount = (bill_amount * tip_percentage) / 100
        total_amount = bill_amount + tip_amount
        per_person = total_amount / people
        
        return {
            'tip_amount': tip_amount,
            'total_amount': total_amount,
            'per_person': per_person
        }