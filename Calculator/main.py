#!/usr/bin/env python3
"""
Complex Calculator - Main Program
Day 3 Project - Enhanced Calculator with Multiple Files
"""

from calculator_operations import BasicOperations, AdvancedOperations
from calculator_utils import Calculator_Utils
from calculator_history import CalculatorHistory
import sys

class ComplexCalculator:
    def __init__(self):
        self.basic_ops = BasicOperations()
        self.advanced_ops = AdvancedOperations()
        self.utils = Calculator_Utils()
        self.history = CalculatorHistory()
        self.running = True
    
    def display_welcome(self):
        """Display welcome message and menu"""
        self.utils.clear_screen()
        print("=" * 60)
        print("🧮 COMPLEX CALCULATOR")
        print("=" * 60)
        print("\n📋 AVAILABLE OPERATIONS:")
        print("\n🔢 Basic Operations:")
        print("  1. Addition (+)")
        print("  2. Subtraction (-)")
        print("  3. Multiplication (*)")
        print("  4. Division (/)")
        print("  5. Modulus (%)")
        print("  6. Integer Division (//)")
        
        print("\n🧠 Advanced Operations:")
        print("  7. Power (**)")
        print("  8. Square Root (sqrt)")
        print("  9. Factorial (!)")
        print("  10. Logarithm (log)")
        print("  11. Sin, Cos, Tan")
        print("  12. Area Calculator")
        print("  13. Unit Converter")
        
        print("\n📊 Utility Options:")
        print("  h. Show History")
        print("  c. Clear History")
        print("  help. Show Help")
        print("  q. Quit")
        print("-" * 60)
    
    def get_menu_choice(self):
        """Get user's menu choice"""
        while True:
            choice = input("\n🎯 Enter your choice: ").strip().lower()
            
            if choice in ['q', 'quit', 'exit']:
                return 'quit'
            elif choice in ['h', 'history']:
                return 'history'
            elif choice in ['c', 'clear']:
                return 'clear'
            elif choice == 'help':
                return 'help'
            elif choice.isdigit() and 1 <= int(choice) <= 13:
                return int(choice)
            else:
                print("❌ Invalid choice! Please try again.")
    
    def execute_basic_operation(self, choice):
        """Execute basic arithmetic operations"""
        operations = {
            1: ('+', self.basic_ops.add),
            2: ('-', self.basic_ops.subtract),
            3: ('*', self.basic_ops.multiply),
            4: ('/', self.basic_ops.divide),
            5: ('%', self.basic_ops.modulus),
            6: ('//', self.basic_ops.integer_divide)
        }
        
        if choice in operations:
            symbol, operation = operations[choice]
            num1 = self.utils.get_number("Enter first number: ")
            num2 = self.utils.get_number("Enter second number: ")
            
            try:
                result = operation(num1, num2)
                calculation = f"{num1} {symbol} {num2} = {result}"
                print(f"\n✅ Result: {calculation}")
                self.history.add_calculation(calculation)
                return True
            except Exception as e:
                print(f"❌ Error: {e}")
                return False
    
    def execute_advanced_operation(self, choice):
        """Execute advanced mathematical operations"""
        try:
            if choice == 7:  # Power
                base = self.utils.get_number("Enter base: ")
                exponent = self.utils.get_number("Enter exponent: ")
                result = self.advanced_ops.power(base, exponent)
                calculation = f"{base} ** {exponent} = {result}"
                
            elif choice == 8:  # Square Root
                num = self.utils.get_number("Enter number: ")
                result = self.advanced_ops.square_root(num)
                calculation = f"√{num} = {result}"
                
            elif choice == 9:  # Factorial
                num = int(self.utils.get_number("Enter positive integer: "))
                result = self.advanced_ops.factorial(num)
                calculation = f"{num}! = {result}"
                
            elif choice == 10:  # Logarithm
                num = self.utils.get_number("Enter number: ")
                base = self.utils.get_number("Enter base (default 10): ") or 10
                result = self.advanced_ops.logarithm(num, base)
                calculation = f"log_{base}({num}) = {result}"
                
            elif choice == 11:  # Trigonometric
                self.trigonometric_menu()
                return True
                
            elif choice == 12:  # Area Calculator
                self.area_calculator_menu()
                return True
                
            elif choice == 13:  # Unit Converter
                self.unit_converter_menu()
                return True
            
            print(f"\n✅ Result: {calculation}")
            self.history.add_calculation(calculation)
            return True
            
        except Exception as e:
            print(f"❌ Error: {e}")
            return False
    
    def trigonometric_menu(self):
        """Handle trigonometric operations"""
        print("\n📐 Trigonometric Functions:")
        print("1. Sin    2. Cos    3. Tan")
        
        choice = input("Choose function (1-3): ").strip()
        if choice not in ['1', '2', '3']:
            print("❌ Invalid choice!")
            return
        
        angle = self.utils.get_number("Enter angle in degrees: ")
        
        functions = {
            '1': ('sin', self.advanced_ops.sine),
            '2': ('cos', self.advanced_ops.cosine),
            '3': ('tan', self.advanced_ops.tangent)
        }
        
        func_name, func = functions[choice]
        result = func(angle)
        calculation = f"{func_name}({angle}°) = {result}"
        
        print(f"\n✅ Result: {calculation}")
        self.history.add_calculation(calculation)
    
    def area_calculator_menu(self):
        """Handle area calculations"""
        print("\n📏 Area Calculator:")
        print("1. Rectangle   2. Circle   3. Triangle")
        
        choice = input("Choose shape (1-3): ").strip()
        
        if choice == '1':  # Rectangle
            length = self.utils.get_number("Enter length: ")
            width = self.utils.get_number("Enter width: ")
            result = self.advanced_ops.rectangle_area(length, width)
            calculation = f"Rectangle Area: {length} × {width} = {result}"
            
        elif choice == '2':  # Circle
            radius = self.utils.get_number("Enter radius: ")
            result = self.advanced_ops.circle_area(radius)
            calculation = f"Circle Area: π × {radius}² = {result}"
            
        elif choice == '3':  # Triangle
            base = self.utils.get_number("Enter base: ")
            height = self.utils.get_number("Enter height: ")
            result = self.advanced_ops.triangle_area(base, height)
            calculation = f"Triangle Area: ½ × {base} × {height} = {result}"
            
        else:
            print("❌ Invalid choice!")
            return
        
        print(f"\n✅ Result: {calculation}")
        self.history.add_calculation(calculation)
    
    def unit_converter_menu(self):
        """Handle unit conversions"""
        print("\n🔄 Unit Converter:")
        print("1. Temperature   2. Length   3. Weight")
        
        choice = input("Choose conversion type (1-3): ").strip()
        
        if choice == '1':  # Temperature
            print("a. Celsius to Fahrenheit   b. Fahrenheit to Celsius")
            temp_choice = input("Choose (a/b): ").strip().lower()
            
            if temp_choice == 'a':
                celsius = self.utils.get_number("Enter temperature in Celsius: ")
                result = self.advanced_ops.celsius_to_fahrenheit(celsius)
                calculation = f"{celsius}°C = {result}°F"
            elif temp_choice == 'b':
                fahrenheit = self.utils.get_number("Enter temperature in Fahrenheit: ")
                result = self.advanced_ops.fahrenheit_to_celsius(fahrenheit)
                calculation = f"{fahrenheit}°F = {result}°C"
            else:
                print("❌ Invalid choice!")
                return
                
        elif choice == '2':  # Length
            print("a. Meters to Feet   b. Feet to Meters")
            length_choice = input("Choose (a/b): ").strip().lower()
            
            if length_choice == 'a':
                meters = self.utils.get_number("Enter length in meters: ")
                result = self.advanced_ops.meters_to_feet(meters)
                calculation = f"{meters}m = {result}ft"
            elif length_choice == 'b':
                feet = self.utils.get_number("Enter length in feet: ")
                result = self.advanced_ops.feet_to_meters(feet)
                calculation = f"{feet}ft = {result}m"
            else:
                print("❌ Invalid choice!")
                return
                
        elif choice == '3':  # Weight
            print("a. Kg to Pounds   b. Pounds to Kg")
            weight_choice = input("Choose (a/b): ").strip().lower()
            
            if weight_choice == 'a':
                kg = self.utils.get_number("Enter weight in kg: ")
                result = self.advanced_ops.kg_to_pounds(kg)
                calculation = f"{kg}kg = {result}lbs"
            elif weight_choice == 'b':
                pounds = self.utils.get_number("Enter weight in pounds: ")
                result = self.advanced_ops.pounds_to_kg(pounds)
                calculation = f"{pounds}lbs = {result}kg"
            else:
                print("❌ Invalid choice!")
                return
        else:
            print("❌ Invalid choice!")
            return
        
        print(f"\n✅ Result: {calculation}")
        self.history.add_calculation(calculation)
    
    def run(self):
        """Main calculator loop"""
        self.display_welcome()
        
        while self.running:
            try:
                choice = self.get_menu_choice()
                
                if choice == 'quit':
                    self.quit_calculator()
                elif choice == 'history':
                    self.history.show_history()
                elif choice == 'clear':
                    self.history.clear_history()
                    print("🗑️ History cleared!")
                elif choice == 'help':
                    self.display_welcome()
                elif 1 <= choice <= 6:
                    self.execute_basic_operation(choice)
                elif 7 <= choice <= 13:
                    self.execute_advanced_operation(choice)
                
                # Ask if user wants to continue
                if choice not in ['quit', 'help']:
                    continue_calc = input("\n🔄 Continue? (y/n): ").strip().lower()
                    if continue_calc in ['n', 'no', 'quit', 'exit']:
                        self.quit_calculator()
                    elif continue_calc in ['', 'y', 'yes']:
                        continue
                        
            except KeyboardInterrupt:
                self.quit_calculator()
            except Exception as e:
                print(f"❌ Unexpected error: {e}")
    
    def quit_calculator(self):
        """Exit the calculator"""
        print("\n" + "=" * 60)
        print("📊 CALCULATION SUMMARY:")
        self.history.show_summary()
        print("\n🙏 Thank you for using Complex Calculator!")
        print("=" * 60)
        sys.exit(0)

def main():
    """Main function to run the calculator"""
    calculator = ComplexCalculator()
    calculator.run()

if __name__ == "__main__":
    main()