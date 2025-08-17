import streamlit as st
import pandas as pd

def show_assignments():
    st.header("📋 CS101 Programming Assignments")
    
    # Assignment tabs
    tab1, tab2 = st.tabs(["Current Assignment", "Graded Assignments"])
    
    with tab1:
        st.subheader("Assignment 3: Array Manipulation Challenge")
        st.write("**Due Date:** March 15, 2024 by 11:59 PM")
        st.write("**Points:** 100")
        
        col1, col2 = st.columns([3, 2])
        
        with col1:
            st.write("**Assignment Description:**")
            st.write("""
            Create a Python program that manipulates arrays (lists) to solve various problems. 
            Your program should demonstrate your understanding of loops, conditionals, and list operations.
            """)
            
            st.write("**Requirements:**")
            st.write("1. Create a function `find_max(numbers)` that returns the largest number in a list")
            st.write("2. Create a function `count_evens(numbers)` that counts even numbers")
            st.write("3. Create a function `reverse_list(numbers)` that returns a reversed list")
            st.write("4. Test each function with at least 3 different lists")
            st.write("5. Include proper comments and error handling")
            
            st.write("**Sample Input/Output:**")
            st.code("""
# Example usage:
numbers = [5, 2, 8, 1, 9, 3]

print(find_max(numbers))     # Should output: 9
print(count_evens(numbers))  # Should output: 2
print(reverse_list(numbers)) # Should output: [3, 9, 1, 8, 2, 5]
            """, language='python')
            
        with col2:
            st.write("**Grading Rubric:**")
            rubric_data = [
                ["Correctness", "40 points"],
                ["Code Style", "20 points"],
                ["Comments", "15 points"],
                ["Testing", "15 points"],
                ["Error Handling", "10 points"]
            ]
            
            df_rubric = pd.DataFrame(rubric_data, columns=["Category", "Points"])
            st.dataframe(df_rubric, use_container_width=True)
            
            st.write("**Submission Instructions:**")
            st.write("- Submit a single Python file named `assignment3.py`")
            st.write("- Include your name and student ID in comments")
            st.write("- Test your code before submission")
            
            st.warning("⚠️ **Academic Integrity:** This is individual work. Collaboration is not permitted.")
    
    with tab2:
        st.subheader("Assignment 2: List Operations - **GRADED**")
        
        # Grade display
        col1, col2 = st.columns([1, 1])
        with col1:
            st.metric("Your Grade", "70/100", "70%")
        with col2:
            st.metric("Class Average", "78/100", "78%")
            
        # Student's submission
        st.write("**Your Submission:**")
        student_code = '''# Kevin Smith - Student ID: 12345
# Assignment 2: List Operations

def find_max(numbers):
    """Find the maximum number in a list"""
    max_num = numbers[0]
    for num in numbers:
        if num > max_num:
            max_num = num
    return max_num

def count_evens(numbers):
    """Count even numbers in a list"""
    count = 0
    for num in numbers:
        if num % 2 == 0:
            count = count + 1
    return count

def reverse_list(numbers):
    """Reverse a list"""
    reversed_list = []
    for i in range(len(numbers)):
        reversed_list.append(numbers[len(numbers) - 1 - i])
    return reversed_list

# Test the functions
test_list = [1, 2, 3, 4, 5]
print("Max:", find_max(test_list))
print("Evens:", count_evens(test_list))
print("Reversed:", reverse_list(test_list))'''

        st.code(student_code, language='python')
        
        # Detailed feedback
        st.write("**Instructor Feedback:**")
        
        feedback_data = [
            ["Correctness (40 pts)", "35/40", "✅ All functions work correctly. -5 pts: No error handling for empty lists"],
            ["Code Style (20 pts)", "15/20", "⚠️ Good variable names and structure. -5 pts: Some lines could be more concise"],
            ["Comments (15 pts)", "12/15", "✅ Good function docstrings. -3 pts: Could use more inline comments"],
            ["Testing (15 pts)", "8/15", "❌ Only tested with one list. Need at least 3 test cases. -7 pts"],
            ["Error Handling (10 pts)", "0/10", "❌ No error handling for edge cases (empty lists, invalid input). -10 pts"]
        ]
        
        df_feedback = pd.DataFrame(feedback_data, columns=["Category", "Score", "Comments"])
        st.dataframe(df_feedback, use_container_width=True)
        
        st.write("**Overall Comments:**")
        st.info("""
        **Strengths:** Your logic is correct and the code works well for the basic case. Good use of descriptive function names and clear structure.
        
        **Areas for Improvement:** 
        1. Add error handling for edge cases (what happens with empty lists?)
        2. Include more comprehensive testing with different types of input
        3. Consider using built-in functions like `max()` for efficiency
        4. Add more inline comments to explain complex logic
        
        **Next Steps:** Review the error handling techniques from Week 8 lectures and practice writing more comprehensive test cases.
        """)
        
        st.write("**Resubmission Opportunity:**")
        st.write("You can resubmit this assignment for up to 85% credit by addressing the feedback above.")
        st.write("**Resubmission Deadline:** March 10, 2024")