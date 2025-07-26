#!/usr/bin/env python3
"""
Calculator Utilities Module
Contains utility functions for input validation, formatting, and display
"""

import os
import sys
import re
from datetime import datetime

class Calculator_Utils:
    """Utility functions for the calculator"""
    
    def __init__(self):
        self.decimal_places = 6
    
    def clear_screen(self):
        """Clear the terminal screen"""
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def get_number(self, prompt="Enter a number: ", allow_negative=True):
        """Get a valid number from user input with enhanced validation"""
        while True:
            try:
                user_input = input(f"🔢 {prompt}").strip()
                
                # Handle quit commands
                if user_input.lower() in ['q', 'quit', 'exit']:
                    print("\n👋 Goodbye!")
                    sys.exit(0)
                
                # Handle empty input
                if not user_input:
                    print("❌ Please enter a value!")
                    continue
                
                # Handle special mathematical constants
                if user_input.lower() == 'pi':
                    return 3.141592653589793
                elif user_input.lower() == 'e':
                    return 2.718281828459045
                
                # Convert to float
                number = float(user_input)
                
                # Check for negative numbers if not allowed
                if not allow_negative and number < 0:
                    print("❌ Negative numbers are not allowed for this operation!")
                    continue
                
                # Check for reasonable range
                if abs(number) > 1e100:
                    print("❌ Number is too large! Please enter a smaller number.")
                    continue
                
                return number
                
            except ValueError:
                print("❌ Invalid input! Please enter a valid number.")
                print("💡 Tip: You can use 'pi' or 'e' for mathematical constants")
            except KeyboardInterrupt:
                print("\n\n👋 Goodbye!")
                sys.exit(0)
    
    def get_integer(self, prompt="Enter an integer: ", min_val=None, max_val=None):
        """Get a valid integer from user input"""
        while True:
            try:
                user_input = input(f"🔢 {prompt}").strip()
                
                if user_input.lower() in ['q', 'quit', 'exit']:
                    print("\n👋 Goodbye!")
                    sys.exit(0)
                
                if not user_input:
                    print("❌ Please enter a value!")
                    continue
                
                number = int(float(user_input))  # Allow decimal input but convert to int
                
                if min_val is not None and number < min_val:
                    print(f"❌ Number must be at least {min_val}!")
                    continue
                
                if max_val is not None and number > max_val:
                    print(f"❌ Number must be at most {max_val}!")
                    continue
                
                return number
                
            except ValueError:
                print("❌ Invalid input! Please enter a valid integer.")
            except KeyboardInterrupt:
                print("\n\n👋 Goodbye!")
                sys.exit(0)
    
    def format_number(self, number, decimal_places=None):
        """Format number for display with appropriate precision"""
        if decimal_places is None:
            decimal_places = self.decimal_places
        
        # Handle very large or very small numbers
        if abs(number) >= 1e6 or (abs(number) < 1e-3 and number != 0):
            return f"{number:.3e}"
        
        # Handle integers
        if isinstance(number, int) or number.is_integer():
            return str(int(number))
        
        # Format float with specified decimal places
        formatted = f"{number:.{decimal_places}f}"
        
        # Remove trailing zeros
        if '.' in formatted:
            formatted = formatted.rstrip('0').rstrip('.')
        
        return formatted
    
    def validate_operator(self, operator):
        """Validate mathematical operator"""
        valid_operators = ['+', '-', '*', '/', '%', '//', '**', '^']
        return operator in valid_operators
    
    def parse_expression(self, expression):
        """Parse a mathematical expression (basic implementation)"""
        # Remove spaces
        expression = expression.replace(' ', '')
        
        # Find operator (simple implementation for basic operators)
        operators = ['+', '-', '*', '/', '%', '**', '//']
        
        for op in operators:
            if op in expression:
                parts = expression.split(op, 1)
                if len(parts) == 2:
                    try:
                        num1 = float(parts[0])
                        num2 = float(parts[1])
                        return num1, op, num2
                    except ValueError:
                        continue
        
        raise ValueError("Invalid expression format!")
    
    def get_yes_no(self, prompt):
        """Get yes/no input from user"""
        while True:
            response = input(f"❓ {prompt} (y/n): ").strip().lower()
            
            if response in ['y', 'yes', 'ye']:
                return True
            elif response in ['n', 'no']:
                return False
            elif response in ['q', 'quit', 'exit']:
                print("\n👋 Goodbye!")
                sys.exit(0)
            else:
                print("❌ Please enter 'y' for yes or 'n' for no.")
    
    def display_error(self, error_message, suggestion=None):
        """Display formatted error message"""
        print(f"\n❌ ERROR: {error_message}")
        if suggestion:
            print(f"💡 SUGGESTION: {suggestion}")
    
    def display_result(self, calculation, result, unit=None):
        """Display formatted calculation result"""
        formatted_result = self.format_number(result)
        
        if unit:
            print(f"\n✅ {calculation} = {formatted_result} {unit}")
        else:
            print(f"\n✅ {calculation} = {formatted_result}")
    
    def create_separator(self, char='-', length=50):
        """Create a separator line"""
        return char * length
    
    def get_current_time(self):
        """Get current timestamp"""
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    def validate_email(self, email):
        """Basic email validation"""
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return re.match(pattern, email) is not None
    
    def format_percentage(self, decimal_value):
        """Format decimal as percentage"""
        return f"{decimal_value * 100:.2f}%"
    
    def format_currency(self, amount, currency_symbol='$'):
        """Format number as currency"""
        return f"{currency_symbol}{amount:,.2f}"
    
    def get_multiple_numbers(self, prompt="Enter numbers separated by commas: "):
        """Get multiple numbers from user input"""
        while True:
            try:
                user_input = input(f"🔢 {prompt}").strip()
                
                if user_input.lower() in ['q', 'quit', 'exit']:
                    print("\n👋 Goodbye!")
                    sys.exit(0)
                
                if not user_input:
                    print("❌ Please enter at least one number!")
                    continue
                
                # Split by comma and convert to float
                numbers = []
                for num_str in user_input.split(','):
                    num_str = num_str.strip()
                    if num_str:  # Skip empty strings
                        numbers.append(float(num_str))
                
                if not numbers:
                    print("❌ No valid numbers found!")
                    continue
                
                return numbers
                
            except ValueError as e:
                print("❌ Invalid input! Please enter numbers separated by commas.")
                print("💡 Example: 1, 2.5, 3, 4.7")
            except KeyboardInterrupt:
                print("\n\n👋 Goodbye!")
                sys.exit(0)
    
    def display_table(self, headers, rows):
        """Display data in table format"""
        if not headers or not rows:
            print("❌ No data to display!")
            return
        
        # Calculate column widths
        col_widths = []
        for i, header in enumerate(headers):
            max_width = len(str(header))
            for row in rows:
                if i < len(row):
                    max_width = max(max_width, len(str(row[i])))
            col_widths.append(max_width + 2)
        
        # Print header
        header_row = "|".join(str(header).center(col_widths[i]) for i, header in enumerate(headers))
        print(f"|{header_row}|")
        
        # Print separator
        separator = "+".join("-" * width for width in col_widths)
        print(f"+{separator}+")
        
        # Print rows
        for row in rows:
            formatted_row = []
            for i, cell in enumerate(row):
                if i < len(col_widths):
                    formatted_row.append(str(cell).center(col_widths[i]))
            row_str = "|".join(formatted_row)
            print(f"|{row_str}|")
    
    def progress_bar(self, current, total, length=40):
        """Display a progress bar"""
        if total == 0:
            percent = 0
        else:
            percent = current / total
        
        filled_length = int(length * percent)
        bar = '█' * filled_length + '-' * (length - filled_length)
        print(f'\r|{bar}| {percent:.1%} Complete', end='', flush=True)
    
    def get_menu_choice(self, options, prompt="Choose an option: "):
        """Get menu choice from user with validation"""
        while True:
            print("\n📋 Available options:")
            for i, option in enumerate(options, 1):
                print(f"  {i}. {option}")
            
            try:
                choice = input(f"\n🎯 {prompt}").strip()
                
                if choice.lower() in ['q', 'quit', 'exit']:
                    print("\n👋 Goodbye!")
                    sys.exit(0)
                
                choice_num = int(choice)
                if 1 <= choice_num <= len(options):
                    return choice_num - 1  # Return 0-based index
                else:
                    print(f"❌ Please enter a number between 1 and {len(options)}")
            
            except ValueError:
                print("❌ Please enter a valid number!")
            except KeyboardInterrupt:
                print("\n\n👋 Goodbye!")
                sys.exit(0)
    
    def word_wrap(self, text, width=70):
        """Wrap text to specified width"""
        words = text.split()
        lines = []
        current_line = []
        current_length = 0
        
        for word in words:
            if current_length + len(word) + len(current_line) <= width:
                current_line.append(word)
                current_length += len(word)
            else:
                if current_line:
                    lines.append(' '.join(current_line))
                current_line = [word]
                current_length = len(word)
        
        if current_line:
            lines.append(' '.join(current_line))
        
        return '\n'.join(lines)
    
    def safe_division(self, dividend, divisor):
        """Perform safe division with error handling"""
        if divisor == 0:
            raise ValueError("Division by zero is not allowed!")
        
        result = dividend / divisor
        
        # Check for infinity or NaN
        if abs(result) == float('inf'):
            raise ValueError("Result is infinite!")
        
        if result != result:  # NaN check
            raise ValueError("Result is not a number!")
        
        return result
    
    def round_to_significant_figures(self, number, sig_figs=6):
        """Round number to specified significant figures"""
        if number == 0:
            return 0
        
        import math
        return round(number, -int(math.floor(math.log10(abs(number)))) + (sig_figs - 1))
    
    def get_confirmation(self, message):
        """Get user confirmation for important actions"""
        print(f"\n⚠️  {message}")
        return self.get_yes_no("Are you sure you want to continue?")
    
    def display_welcome_art(self):
        """Display ASCII art welcome message"""
        art = """
    ╔═══════════════════════════════════════════════════════════╗
    ║                                                           ║
    ║      🧮  COMPLEX CALCULATOR - DAY 3 PROJECT  🧮          ║
    ║                                                           ║
    ║           Advanced Mathematical Operations                ║
    ║                  with Python 3                          ║
    ║                                                           ║
    ╚═══════════════════════════════════════════════════════════╝
        """
        print(art)
    
    def loading_animation(self, duration=3):
        """Display loading animation"""
        import time
        
        frames = ['⠋', '⠙', '⠹', '⠸', '⠼', '⠴', '⠦', '⠧', '⠇', '⠏']
        end_time = time.time() + duration
        
        while time.time() < end_time:
            for frame in frames:
                print(f'\r{frame} Processing...', end='', flush=True)
                time.sleep(0.1)
                if time.time() >= end_time:
                    break
        
        print('\r✅ Complete!       ')
    
    def format_time_duration(self, seconds):
        """Format duration in seconds to human readable format"""
        if seconds < 60:
            return f"{seconds:.2f} seconds"
        elif seconds < 3600:
            minutes = seconds // 60
            remaining_seconds = seconds % 60
            return f"{int(minutes)} minutes {remaining_seconds:.1f} seconds"
        else:
            hours = seconds // 3600
            remaining_minutes = (seconds % 3600) // 60
            return f"{int(hours)} hours {int(remaining_minutes)} minutes"
    
    def validate_range(self, value, min_val, max_val, name="Value"):
        """Validate that a value is within specified range"""
        if value < min_val or value > max_val:
            raise ValueError(f"{name} must be between {min_val} and {max_val}!")
        return True
    
    def get_file_input(self, prompt="Enter filename: "):
        """Get filename input with validation"""
        while True:
            filename = input(f"📁 {prompt}").strip()
            
            if filename.lower() in ['q', 'quit', 'exit']:
                print("\n👋 Goodbye!")
                sys.exit(0)
            
            if not filename:
                print("❌ Please enter a filename!")
                continue
            
            # Basic filename validation
            invalid_chars = '<>:"/\\|?*'
            if any(char in filename for char in invalid_chars):
                print("❌ Filename contains invalid characters!")
                continue
            
            return filename
    
    def display_calculation_steps(self, steps):
        """Display step-by-step calculation process"""
        print("\n📚 Calculation Steps:")
        print(self.create_separator('='))
        
        for i, step in enumerate(steps, 1):
            print(f"Step {i}: {step}")
        
        print(self.create_separator('='))
    
    def get_precision_preference(self):
        """Get user's preference for decimal precision"""
        while True:
            try:
                precision = self.get_integer(
                    "Enter desired decimal places (1-15): ", 
                    min_val=1, 
                    max_val=15
                )
                self.decimal_places = precision
                print(f"✅ Decimal precision set to {precision} places")
                return precision
            except Exception as e:
                print(f"❌ Error: {e}")
    
    def backup_data(self, data, backup_name="calculator_backup"):
        """Create a backup of important data"""
        import json
        from datetime import datetime
        
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"{backup_name}_{timestamp}.json"
        
        try:
            with open(filename, 'w') as f:
                json.dump(data, f, indent=2)
            print(f"✅ Data backed up to {filename}")
            return filename
        except Exception as e:
            print(f"❌ Backup failed: {e}")
            return None