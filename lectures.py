import streamlit as st

def show_lectures():
    st.header("🎥 CS101 Lecture Notes")
    
    lecture_topics = [
        "Week 1: Introduction to Programming & Python Basics",
        "Week 2: Variables, Data Types, and Input/Output", 
        "Week 3: Conditional Statements and Boolean Logic",
        "Week 4: Loops and Iteration",
        "Week 5: Functions and Methods"
    ]
    
    selected_lecture = st.selectbox("Select a lecture:", lecture_topics)
    
    if "Week 1" in selected_lecture:
        st.subheader("Week 1: Introduction to Programming & Python Basics")
        
        col1, col2 = st.columns([3, 2])
        
        with col1:
            st.write("**Learning Objectives:**")
            st.write("- Understand what programming is and why it's useful")
            st.write("- Learn basic Python syntax and structure")
            st.write("- Write your first Python program")
            
            st.write("**Key Concepts:**")
            st.write("1. **Programming Languages**: Tools for giving instructions to computers")
            st.write("2. **Python**: A beginner-friendly, versatile programming language")
            st.write("3. **Syntax**: The rules for writing valid Python code")
            st.write("4. **Comments**: Notes in code using # symbol")
            
            st.code('''# This is a comment in Python
print("Hello, World!")  # This prints text to the screen
print("Welcome to CS101!")''', language='python')
            
        with col2:
            st.write("**Practice Exercises:**")
            st.write("1. Install Python on your computer")
            st.write("2. Write a program that prints your name")
            st.write("3. Add comments explaining your code")
            
            st.write("**Homework:**")
            st.write("- Read Chapter 1 in textbook")
            st.write("- Complete Practice Problems 1.1-1.5")
            st.write("- Submit Hello World program")
    
    elif "Week 2" in selected_lecture:
        st.subheader("Week 2: Variables, Data Types, and Input/Output")
        
        col1, col2 = st.columns([3, 2])
        
        with col1:
            st.write("**Learning Objectives:**")
            st.write("- Understand variables and how to use them")
            st.write("- Learn different data types in Python")
            st.write("- Get input from users")
            
            st.write("**Key Concepts:**")
            st.write("1. **Variables**: Containers that store data values")
            st.write("2. **Data Types**: Different kinds of data (int, float, string, bool)")
            st.write("3. **Input/Output**: Getting data from users and displaying results")
            
            st.code('''# Variables and data types
name = "Alice"          # String
age = 20               # Integer
height = 5.6           # Float
is_student = True      # Boolean

# Getting input from user
user_name = input("What's your name? ")
print(f"Hello, {user_name}!")''', language='python')
            
        with col2:
            st.write("**Practice Exercises:**")
            st.write("1. Create variables of each data type")
            st.write("2. Write a program that asks for user's age")
            st.write("3. Calculate and display birth year")
            
            st.write("**Common Mistakes:**")
            st.write("- Forgetting quotes around strings")
            st.write("- Using = instead of == for comparison")
            st.write("- Not converting input() to numbers")
    
    elif "Week 3" in selected_lecture:
        st.subheader("Week 3: Conditional Statements and Boolean Logic")
        
        col1, col2 = st.columns([3, 2])
        
        with col1:
            st.write("**Learning Objectives:**")
            st.write("- Use if, elif, and else statements")
            st.write("- Understand boolean expressions")
            st.write("- Create programs that make decisions")
            
            st.code('''# Conditional statements
age = int(input("Enter your age: "))

if age >= 18:
    print("You can vote!")
elif age >= 16:
    print("You can drive!")
else:
    print("You're still young!")

# Boolean operators
temperature = 75
sunny = True

if temperature > 70 and sunny:
    print("Perfect weather for a picnic!")''', language='python')
            
        with col2:
            st.write("**Boolean Operators:**")
            st.write("- `and`: Both conditions must be true")
            st.write("- `or`: At least one condition must be true") 
            st.write("- `not`: Reverses the boolean value")
            
            st.write("**Comparison Operators:**")
            st.write("- `==` equal to")
            st.write("- `!=` not equal to")
            st.write("- `<` less than")
            st.write("- `>` greater than")
            st.write("- `<=` less than or equal")
            st.write("- `>=` greater than or equal")
    
    elif "Week 4" in selected_lecture:
        st.subheader("Week 4: Loops and Iteration")
        
        col1, col2 = st.columns([3, 2])
        
        with col1:
            st.write("**Learning Objectives:**")
            st.write("- Use for loops to repeat code")
            st.write("- Use while loops for conditional repetition")
            st.write("- Understand when to use each type of loop")
            
            st.code('''# For loop - when you know how many times
for i in range(5):
    print(f"Count: {i}")

# For loop with lists
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(f"I like {fruit}")

# While loop - when condition-based
count = 0
while count < 3:
    print(f"While count: {count}")
    count += 1  # Same as count = count + 1''', language='python')
            
        with col2:
            st.write("**Loop Types:**")
            st.write("- **For loop**: Iterate a specific number of times")
            st.write("- **While loop**: Continue until condition is false")
            
            st.write("**Common Patterns:**")
            st.write("- `range(n)`: Numbers 0 to n-1")
            st.write("- `range(start, stop)`: Numbers from start to stop-1")
            st.write("- `range(start, stop, step)`: With custom step size")
            
            st.write("**Avoiding Infinite Loops:**")
            st.write("- Always modify the condition variable")
            st.write("- Use break statement when needed")
    
    elif "Week 5" in selected_lecture:
        st.subheader("Week 5: Functions and Methods")
        
        col1, col2 = st.columns([3, 2])
        
        with col1:
            st.write("**Learning Objectives:**")
            st.write("- Define and call functions")
            st.write("- Use parameters and return values")
            st.write("- Understand function scope")
            
            st.code('''# Defining a function
def greet(name):
    return f"Hello, {name}!"

# Calling the function
message = greet("Alice")
print(message)

# Function with multiple parameters
def calculate_area(length, width):
    area = length * width
    return area

# Function with default parameter
def introduce(name, age=18):
    print(f"Hi, I'm {name} and I'm {age} years old.")

introduce("Bob")        # Uses default age
introduce("Carol", 25)  # Uses specified age''', language='python')
            
        with col2:
            st.write("**Function Benefits:**")
            st.write("- Code reusability")
            st.write("- Better organization")
            st.write("- Easier debugging")
            st.write("- Modular design")
            
            st.write("**Function Components:**")
            st.write("- `def` keyword to define")
            st.write("- Function name")
            st.write("- Parameters (optional)")
            st.write("- Function body")
            st.write("- Return statement (optional)")