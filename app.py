import streamlit as st

st.set_page_config(
    page_title="Student CGPA Calculator",
    page_icon="📚"
)

# Grade points
grade_points = {
    "A+": 4.0,
    "A": 3.7,
    "A-": 3.3,
    "B+": 3.0,
    "B": 2.7,
    "B-": 2.3,
    "C+": 2.0,
    "C": 1.7,
    "C-": 1.3,
    "D": 1.0,
    "F": 0.0
}

# Store subjects
if "subjects" not in st.session_state:
    st.session_state.subjects = []

# Title
st.title("📚 Student CGPA Calculator")
st.write(
    "Calculate your semester CGPA by entering "
    "your subjects, credit hours and grades."
)

st.divider()

# Input section
st.subheader("➕ Add Subject")

col1, col2, col3 = st.columns(3)

with col1:
    subject_name = st.text_input("Subject Name")

with col2:
    credit_hours = st.number_input(
        "Credit Hours",
        min_value=0.5,
        max_value=10.0,
        step=0.5
    )

with col3:
    selected_grade = st.selectbox(
        "Select Grade",
        ["Select Grade"] + list(grade_points.keys())
    )

# Add subject
if st.button("➕ Add Subject"):

    if not subject_name.strip():
        st.error("Please enter a subject name.")

    elif selected_grade == "Select Grade":
        st.error("Please select a grade.")

    else:
        subject = {
            "name": subject_name.strip(),
            "credits": credit_hours,
            "grade": selected_grade,
            "points": grade_points[selected_grade]
        }

        st.session_state.subjects.append(subject)

        st.success(
            f"Subject '{subject_name}' added successfully!"
        )

# Display subjects
st.subheader("📋 Added Subjects")

if len(st.session_state.subjects) > 0:

    for i, subject in enumerate(st.session_state.subjects):

        col1, col2, col3, col4, col5 = st.columns(
            [3, 1, 1, 1, 1]
        )

        with col1:
            st.write(subject["name"])

        with col2:
            st.write(subject["credits"])

        with col3:
            st.write(subject["grade"])

        with col4:
            st.write(f"{subject['points']:.1f}")

        with col5:
            if st.button("🗑️", key=f"delete_{i}"):
                st.session_state.subjects.pop(i)
                st.rerun()

    st.divider()

    # Calculate CGPA
    if st.button("📊 Calculate CGPA"):

        total_weighted_points = 0
        total_credits = 0

        for subject in st.session_state.subjects:

            weighted_points = (
                subject["points"] * subject["credits"]
            )

            total_weighted_points += weighted_points
            total_credits += subject["credits"]

        cgpa = total_weighted_points / total_credits

        st.success(
            f"🎓 Your Semester CGPA: {cgpa:.2f}"
        )

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric(
                "Total Subjects",
                len(st.session_state.subjects)
            )

        with col2:
            st.metric(
                "Total Credits",
                f"{total_credits:.1f}"
            )

        with col3:
            st.metric(
                "Quality Points",
                f"{total_weighted_points:.2f}"
            )

else:
    st.info("No subjects added yet.")

# Reset
st.divider()

if st.button("🔄 Reset Calculator"):

    st.session_state.subjects = []

    st.success("Calculator has been reset.")

    st.rerun()

st.caption(
    "Student CGPA Calculator | Built with Python + Streamlit"
  )
