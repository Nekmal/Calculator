<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Python Calculator</title>
    <style>
        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, sans-serif;
            max-width: 800px;
            margin: 0 auto;
            padding: 40px 20px;
            line-height: 1.6;
            color: #333;
            background-color: #f8f9fa;
        }
        .container {
            background: white;
            padding: 40px;
            border-radius: 10px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        }
        h1 {
            color: #2c3e50;
            border-bottom: 3px solid #3498db;
            padding-bottom: 10px;
            margin-bottom: 20px;
        }
        h2 {
            color: #34495e;
            margin-top: 30px;
            margin-bottom: 15px;
        }
        .description {
            font-size: 18px;
            color: #555;
            margin-bottom: 30px;
        }
        ul {
            padding-left: 0;
        }
        li {
            list-style: none;
            padding: 8px 0;
            font-size: 16px;
        }
        .features li::before {
            content: "✓ ";
            color: #27ae60;
            font-weight: bold;
            margin-right: 8px;
        }
        .requirements li::before {
            content: "• ";
            color: #3498db;
            font-weight: bold;
            margin-right: 8px;
        }
        .support li::before {
            content: "";
        }
        pre {
            background: #2c3e50;
            color: #ecf0f1;
            padding: 20px;
            border-radius: 8px;
            overflow-x: auto;
            font-family: 'Courier New', Consolas, monospace;
            font-size: 14px;
            margin: 15px 0;
        }
        code {
            background: #ecf0f1;
            color: #2c3e50;
            padding: 3px 6px;
            border-radius: 4px;
            font-family: 'Courier New', Consolas, monospace;
            font-size: 14px;
        }
        .bash {
            background: #1e1e1e;
            color: #ddd;
        }
        .python {
            background: #0f4c75;
            color: #ffffff;
        }
        a {
            color: #3498db;
            text-decoration: none;
        }
        a:hover {
            text-decoration: underline;
        }
        .section {
            margin-bottom: 30px;
        }
        .emoji {
            font-size: 18px;
            margin-right: 8px;
        }
        .support-links {
            display: flex;
            gap: 20px;
            flex-wrap: wrap;
        }
        .support-links a {
            display: inline-flex;
            align-items: center;
            padding: 10px 15px;
            background: #3498db;
            color: white;
            border-radius: 5px;
            text-decoration: none;
            transition: background 0.3s;
        }
        .support-links a:hover {
            background: #2980b9;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Python Calculator</h1>
        
        <p class="description">
            A simple Python calculator with GUI and CLI interfaces supporting basic arithmetic and scientific functions.
        </p>

        <div class="section">
            <h2>Features</h2>
            <ul class="features">
                <li><span class="emoji">🧮</span> Basic arithmetic operations (+, -, ×, ÷)</li>
                <li><span class="emoji">🔬</span> Scientific functions (sin, cos, log, sqrt)</li>
                <li><span class="emoji">🖥️</span> GUI interface using Tkinter</li>
                <li><span class="emoji">⌨️</span> Command line interface</li>
            </ul>
        </div>

        <div class="section">
            <h2>Installation</h2>
            <pre class="bash">git clone https://github.com/yourusername/python-calculator.git
cd python-calculator
pip install -r requirements.txt</pre>
        </div>

        <div class="section">
            <h2>Usage</h2>
            
            <h3>GUI Calculator</h3>
            <pre class="bash">python calculator_gui.py</pre>

            <h3>Command Line</h3>
            <pre class="bash"># Direct calculation
python calculator.py "2 + 3 * 4"

# Interactive mode
python calculator.py --interactive</pre>

            <h3>Python Module</h3>
            <pre class="python">from calculator import Calculator

calc = Calculator()
result = calc.add(5, 3)        # Returns 8
result = calc.sin(45)          # Returns sine of 45 degrees
result = calc.sqrt(25)         # Returns 5.0</pre>
        </div>

        <div class="section">
            <h2>Basic Operations</h2>
            <pre class="python">calc.add(10, 5)           # 15
calc.subtract(10, 5)      # 5
calc.multiply(10, 5)      # 50
calc.divide(10, 5)        # 2.0
calc.power(2, 3)          # 8
calc.sqrt(16)             # 4.0
calc.sin(90)              # 1.0
calc.log10(100)           # 2.0</pre>
        </div>

        <div class="section">
            <h2>Requirements</h2>
            <ul class="requirements">
                <li>Python 3.8+</li>
                <li>tkinter</li>
                <li>numpy</li>
                <li>math (built-in)</li>
            </ul>
        </div>

        <div class="section">
            <h2>Support</h2>
            <div class="support-links">
                <a href="https://github.com/yourusername/python-calculator/issues">
                    <span class="emoji">🐛</span> GitHub Issues
                </a>
                <a href="mailto:your-email@example.com">
                    <span class="emoji">📧</span> Email Support
                </a>
            </div>
        </div>
    </div>
</body>
</html>
