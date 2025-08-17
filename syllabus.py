import streamlit as st
import pandas as pd

def show_syllabus():
    st.header("📚 CS101: Computer Science Fundamentals")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.subheader("Course Description")
        st.write("""
        This course introduces students to the fundamental concepts of computer science and programming. 
        Students will learn basic programming constructs, problem-solving techniques, and computational thinking 
        through hands-on coding exercises using Python.
        """)
        
        st.subheader("Learning Objectives")
        st.write("""
        By the end of this course, students will be able to:
        - Understand basic programming concepts including variables, data types, and control structures
        - Write, debug, and test simple Python programs
        - Apply problem-solving strategies to computational problems
        - Work with arrays, lists, and basic data structures
        - Understand the fundamentals of algorithm design and analysis
        """)
        
        st.subheader("Weekly Schedule")
        schedule_data = [
            ["Week 1", "Introduction to Programming & Python Basics"],
            ["Week 2", "Variables, Data Types, and Input/Output"],
            ["Week 3", "Conditional Statements and Boolean Logic"],
            ["Week 4", "Loops and Iteration"],
            ["Week 5", "Functions and Methods"],
            ["Week 6", "Lists and Arrays"],
            ["Week 7", "String Manipulation"],
            ["Week 8", "File I/O and Error Handling"],
            ["Week 9", "Basic Data Structures"],
            ["Week 10", "Algorithm Design Principles"],
            ["Week 11", "Debugging and Testing"],
            ["Week 12", "Final Projects and Review"]
        ]
        
        df = pd.DataFrame(schedule_data, columns=["Week", "Topic"])
        st.dataframe(df, use_container_width=True)
        
    with col2:
        st.subheader("Course Information")
        st.write("**Instructor:** Dr. Sarah Johnson")
        st.write("**Email:** sjohnson@university.edu")
        st.write("**Office Hours:** MW 2-4 PM")
        st.write("**Credits:** 3")
        st.write("**Prerequisites:** None")
        
        st.subheader("Grading Breakdown")
        grading_data = [
            ["Programming Assignments", "40%"],
            ["Midterm Exam", "25%"],
            ["Final Exam", "25%"],
            ["Class Participation", "10%"]
        ]
        
        df_grades = pd.DataFrame(grading_data, columns=["Category", "Weight"])
        st.dataframe(df_grades, use_container_width=True)
        
        st.subheader("Required Materials")
        st.write("- Python 3.x (free download)")
        st.write("- Code editor (VS Code recommended)")
        st.write("- Course textbook: *Python Programming* by Smith & Jones")
        
        st.subheader("Course Policies")
        st.write("**Late Work:** -10% per day late")
        st.write("**Attendance:** Required for all classes")
        st.write("**Academic Integrity:** Strictly enforced")