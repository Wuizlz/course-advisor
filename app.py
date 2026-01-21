import streamlit as st

courses = [
    {"name": "Intro to Programming", "dept": "CS", "credits": 3},
    {"name": "Data Structures", "dept": "CS", "credits": 4},
    {"name": "Calculus I", "dept": "Math", "credits": 4},
    {"name": "English Composition", "dept": "English", "credits": 3},
    {"name": "Statistics", "dept": "Math", "credits": 3}
]
drop_down_menu = ["All", "CS", "Math", "English"]

st.title("🎓Simple Course Advisor") 
st.write("Select")
selected_var = st.selectbox("Select department", drop_down_menu)

user_input = st.text_input("Type keyword")
keyword = user_input.strip().lower()
if keyword == "":
    st.write("Keyword filter: none")
else:
    st.write(f"Keyword filter: {keyword}")

clicked = st.button("Show Courses")
if clicked:
    matches = []
    for course in courses:
        dept_match = selected_var == "All" or course["dept"] == selected_var
        keyword_match = keyword == "" or keyword in course["name"].lower()
        if dept_match and keyword_match:
            matches.append(course)

    if not matches:
        st.write("No courses found.")

    for course in matches:
        st.write(f"{course['name']} ({course['credits']} credits)")
        if course["credits"] == 4:
            st.write("High workload course")
        else:
            st.write("Regular workload")
            
