import streamlit as st

st.title("📊 Test Score Evaluator")

st.markdown("Enter marks for 5 subjects. Pass mark is **40**.")

# Input fields for 5 test scores
score1 = st.number_input("Subject 1 Score:", min_value=0, max_value=100, step=1)
score2 = st.number_input("Subject 2 Score:", min_value=0, max_value=100, step=1)
score3 = st.number_input("Subject 3 Score:", min_value=0, max_value=100, step=1)
score4 = st.number_input("Subject 4 Score:", min_value=0, max_value=100, step=1)
score5 = st.number_input("Subject 5 Score:", min_value=0, max_value=100, step=1)

# Calculate when user clicks the button
if st.button("Check Result"):
    scores = [score1, score2, score3, score4, score5]
    pass_mark = 40
    average = sum(scores) / len(scores)

    st.subheader("📋 Subject-wise Result:")
    for i, score in enumerate(scores, start=1):
        status = "✅ Pass" if score >= pass_mark else "❌ Fail"
        st.write(f"Subject {i}: {score} - {status}")

    st.subheader("📈 Overall Result:")
    if all(score >= pass_mark for score in scores):
        st.success(f"🎉 Passed All Subjects! Average Score: {average:.2f}")
    else:
        st.error(f"😢 Failed in one or more subjects. Average Score: {average:.2f}")
