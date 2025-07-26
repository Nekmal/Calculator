#!/usr/bin/env python3
"""
Calculator History Module
Manages calculation history, statistics, and data persistence
"""

import json
import os
from datetime import datetime
from calculator_utils import Calculator_Utils

class CalculatorHistory:
    """Manages calculation history and statistics"""
    
    def __init__(self, history_file="calculator_history.json"):
        self.history_file = history_file
        self.calculations = []
        self.session_start = datetime.now()
        self.utils = Calculator_Utils()
        self.load_history()
    
    def add_calculation(self, calculation, result=None, operation_type="basic"):
        """Add a calculation to history"""
        entry = {
            'id': len(self.calculations) + 1,
            'calculation': calculation,
            'result': result,
            'operation_type': operation_type,
            'timestamp': datetime.now().isoformat(),
            'session_id': self.session_start.isoformat()
        }
        
        self.calculations.append(entry)
        self.save_history()
        
        # Keep only last 1000 calculations to prevent memory issues
        if len(self.calculations) > 1000:
            self.calculations = self.calculations[-1000:]
    
    def show_history(self, limit=10):
        """Display recent calculation history"""
        if not self.calculations:
            print("\n📝 No calculations in history yet!")
            return
        
        print(f"\n📚 CALCULATION HISTORY (Last {min(limit, len(self.calculations))} entries)")
        print("=" * 70)
        
        # Show most recent calculations first
        recent_calculations = self.calculations[-limit:]
        recent_calculations.reverse()  # Most recent first
        
        for entry in recent_calculations:
            timestamp = datetime.fromisoformat(entry['timestamp'])
            formatted_time = timestamp.strftime("%Y-%m-%d %H:%M:%S")
            
            print(f"[{entry['id']:3d}] {formatted_time}")
            print(f"      {entry['calculation']}")
            print(f"      Type: {entry['operation_type'].title()}")
            print("-" * 70)
        
        self.show_history_options()
    
    def show_history_options(self):
        """Show options for history management"""
        print("\n🔧 History Options:")
        print("1. Show all history")
        print("2. Search history")
        print("3. Export history")
        print("4. Show statistics")
        print("5. Return to main menu")
        
        choice = input("\nChoose option (1-5): ").strip()
        
        if choice == '1':
            self.show_all_history()
        elif choice == '2':
            self.search_history()
        elif choice == '3':
            self.export_history()
        elif choice == '4':
            self.show_statistics()
        elif choice == '5':
            return
        else:
            print("❌ Invalid choice!")
    
    def show_all_history(self):
        """Display all calculation history"""
        if not self.calculations:
            print("\n📝 No calculations in history!")
            return
        
        print(f"\n📚 COMPLETE CALCULATION HISTORY ({len(self.calculations)} entries)")
        print("=" * 80)
        
        # Group by date
        grouped_history = {}
        for entry in self.calculations:
            timestamp = datetime.fromisoformat(entry['timestamp'])
            date_key = timestamp.strftime("%Y-%m-%d")
            
            if date_key not in grouped_history:
                grouped_history[date_key] = []
            
            grouped_history[date_key].append(entry)
        
        # Display grouped by date
        for date, entries in sorted(grouped_history.items(), reverse=True):
            print(f"\n📅 {date}")
            print("-" * 40)
            
            for entry in entries:
                timestamp = datetime.fromisoformat(entry['timestamp'])
                time_str = timestamp.strftime("%H:%M:%S")
                
                print(f"[{entry['id']:3d}] {time_str} | {entry['calculation']}")
        
        print("\n" + "=" * 80)
    
    def search_history(self):
        """Search through calculation history"""
        if not self.calculations:
            print("\n📝 No calculations to search!")
            return
        
        search_term = input("\n🔍 Enter search term: ").strip().lower()
        
        if not search_term:
            print("❌ Please enter a search term!")
            return
        
        matches = []
        for entry in self.calculations:
            if (search_term in entry['calculation'].lower() or 
                search_term in entry['operation_type'].lower()):
                matches.append(entry)
        
        if not matches:
            print(f"❌ No calculations found containing '{search_term}'")
            return
        
        print(f"\n🎯 Found {len(matches)} matching calculations:")
        print("=" * 70)
        
        for entry in matches:
            timestamp = datetime.fromisoformat(entry['timestamp'])
            formatted_time = timestamp.strftime("%Y-%m-%d %H:%M:%S")
            
            print(f"[{entry['id']:3d}] {formatted_time}")
            print(f"      {entry['calculation']}")
            print(f"      Type: {entry['operation_type'].title()}")
            print("-" * 70)
    
    def export_history(self):
        """Export history to different formats"""
        if not self.calculations:
            print("\n📝 No calculations to export!")
            return
        
        print("\n📤 Export Options:")
        print("1. JSON format")
        print("2. CSV format")
        print("3. Text format")
        
        choice = input("\nChoose format (1-3): ").strip()
        
        if choice == '1':
            self.export_json()
        elif choice == '2':
            self.export_csv()
        elif choice == '3':
            self.export_text()
        else:
            print("❌ Invalid choice!")
    
    def export_json(self):
        """Export history as JSON"""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"calculator_export_{timestamp}.json"
        
        try:
            export_data = {
                'export_date': datetime.now().isoformat(),
                'total_calculations': len(self.calculations),
                'session_start': self.session_start.isoformat(),
                'calculations': self.calculations
            }
            
            with open(filename, 'w') as f:
                json.dump(export_data, f, indent=2)
            
            print(f"✅ History exported to {filename}")
            
        except Exception as e:
            print(f"❌ Export failed: {e}")
    
    def export_csv(self):
        """Export history as CSV"""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"calculator_export_{timestamp}.csv"
        
        try:
            with open(filename, 'w') as f:
                # Write header
                f.write("ID,Timestamp,Calculation,Operation Type,Result\n")
                
                # Write data
                for entry in self.calculations:
                    timestamp = datetime.fromisoformat(entry['timestamp'])
                    formatted_time = timestamp.strftime("%Y-%m-%d %H:%M:%S")
                    
                    # Escape commas in calculation string
                    calc_escaped = entry['calculation'].replace(',', ';')
                    result = entry.get('result', 'N/A')
                    
                    f.write(f"{entry['id']},{formatted_time},{calc_escaped},"
                           f"{entry['operation_type']},{result}\n")
            
            print(f"✅ History exported to {filename}")
            
        except Exception as e:
            print(f"❌ Export failed: {e}")
    
    def export_text(self):
        """Export history as readable text"""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"calculator_export_{timestamp}.txt"
        
        try:
            with open(filename, 'w') as f:
                f.write("COMPLEX CALCULATOR - CALCULATION HISTORY\n")
                f.write("=" * 50 + "\n\n")
                f.write(f"Export Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
                f.write(f"Total Calculations: {len(self.calculations)}\n")
                f.write(f"Session Started: {self.session_start.strftime('%Y-%m-%d %H:%M:%S')}\n\n")
                
                f.write("CALCULATIONS:\n")
                f.write("-" * 30 + "\n")
                
                for entry in self.calculations:
                    timestamp = datetime.fromisoformat(entry['timestamp'])
                    formatted_time = timestamp.strftime("%Y-%m-%d %H:%M:%S")
                    
                    f.write(f"[{entry['id']:3d}] {formatted_time}\n")
                    f.write(f"     {entry['calculation']}\n")
                    f.write(f"     Type: {entry['operation_type'].title()}\n\n")
            
            print(f"✅ History exported to {filename}")
            
        except Exception as e:
            print(f"❌ Export failed: {e}")
    
    def show_statistics(self):
        """Display calculation statistics"""
        if not self.calculations:
            print("\n📊 No calculations for statistics!")
            return
        
        print("\n📊 CALCULATION STATISTICS")
        print("=" * 50)
        
        # Basic stats
        total_calcs = len(self.calculations)
        session_calcs = len([c for c in self.calculations 
                           if c['session_id'] == self.session_start.isoformat()])
        
        print(f"📈 Total Calculations: {total_calcs}")
        print(f"🎯 This Session: {session_calcs}")
        
        # Operation type breakdown
        operation_counts = {}
        for calc in self.calculations:
            op_type = calc['operation_type']
            operation_counts[op_type] = operation_counts.get(op_type, 0) + 1
        
        print(f"\n🔧 Operations by Type:")
        for op_type, count in sorted(operation_counts.items()):
            percentage = (count / total_calcs) * 100
            print(f"   {op_type.title()}: {count} ({percentage:.1f}%)")
        
        # Time-based stats
        if self.calculations:
            first_calc = datetime.fromisoformat(self.calculations[0]['timestamp'])
            last_calc = datetime.fromisoformat(self.calculations[-1]['timestamp'])
            duration = last_calc - first_calc
            
            print(f"\n⏰ Time Statistics:")
            print(f"   First Calculation: {first_calc.strftime('%Y-%m-%d %H:%M:%S')}")
            print(f"   Latest Calculation: {last_calc.strftime('%Y-%m-%d %H:%M:%S')}")
            print(f"   Total Duration: {self.utils.format_time_duration(duration.total_seconds())}")
            
            if duration.total_seconds() > 0:
                rate = total_calcs / (duration.total_seconds() / 60)  # per minute
                print(f"   Average Rate: {rate:.2f} calculations per minute")
        
        # Daily activity
        daily_counts = {}
        for calc in self.calculations:
            date = datetime.fromisoformat(calc['timestamp']).strftime('%Y-%m-%d')
            daily_counts[date] = daily_counts.get(date, 0) + 1
        
        if daily_counts:
            print(f"\n📅 Daily Activity (Last 7 days):")
            sorted_days = sorted(daily_counts.items(), reverse=True)[:7]
            for date, count in sorted_days:
                print(f"   {date}: {count} calculations")
    
    def clear_history(self):
        """Clear all calculation history with confirmation"""
        if not self.calculations:
            print("\n📝 History is already empty!")
            return
        
        print(f"\n⚠️  You are about to delete {len(self.calculations)} calculations!")
        
        if self.utils.get_confirmation("This action cannot be undone."):
            # Backup before clearing
            backup_file = self.utils.backup_data(
                {'calculations': self.calculations}, 
                "history_backup"
            )
            
            if backup_file:
                print(f"💾 Backup created: {backup_file}")
            
            self.calculations.clear()
            self.save_history()
            print("🗑️  History cleared successfully!")
        else:
            print("❌ Clear operation cancelled.")
    
    def load_history(self):
        """Load history from file"""
        try:
            if os.path.exists(self.history_file):
                with open(self.history_file, 'r') as f:
                    data = json.load(f)
                    self.calculations = data.get('calculations', [])
                    print(f"📚 Loaded {len(self.calculations)} calculations from history.")
        except Exception as e:
            print(f"⚠️  Warning: Could not load history: {e}")
            self.calculations = []
    
    def save_history(self):
        """Save history to file"""
        try:
            data = {
                'last_updated': datetime.now().isoformat(),
                'session_start': self.session_start.isoformat(),
                'calculations': self.calculations
            }
            
            with open(self.history_file, 'w') as f:
                json.dump(data, f, indent=2)
                
        except Exception as e:
            print(f"⚠️  Warning: Could not save history: {e}")
    
    def get_recent_calculations(self, limit=5):
        """Get recent calculations for quick access"""
        return self.calculations[-limit:] if self.calculations else []
    
    def show_summary(self):
        """Show session summary"""
        if not self.calculations:
            print("No calculations performed this session.")
            return
        
        session_calcs = [c for c in self.calculations 
                        if c['session_id'] == self.session_start.isoformat()]
        
        print(f"Session Summary:")
        print(f"  • Calculations performed: {len(session_calcs)}")
        print(f"  • Session duration: {self.utils.format_time_duration((datetime.now() - self.session_start).total_seconds())}")
        
        if session_calcs:
            operation_types = {}
            for calc in session_calcs:
                op_type = calc['operation_type']
                operation_types[op_type] = operation_types.get(op_type, 0) + 1
            
            print(f"  • Most used operation: {max(operation_types, key=operation_types.get)}")
    
    def undo_last_calculation(self):
        """Remove the last calculation from history"""
        if not self.calculations:
            print("❌ No calculations to undo!")
            return None
        
        removed = self.calculations.pop()
        self.save_history()
        print(f"↩️  Undone: {removed['calculation']}")
        return removed
    
    def get_calculation_by_id(self, calc_id):
        """Get a specific calculation by ID"""
        for calc in self.calculations:
            if calc['id'] == calc_id:
                return calc
        return None