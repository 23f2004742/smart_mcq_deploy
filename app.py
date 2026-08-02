import streamlit as st
import pandas as pd

from predict import predict

st.set_page_config(
    page_title="Smart MCQ Solver",
    page_icon="🧠",
    layout="wide"
)

st.title("🧠 Smart MCQ Solver")
st.markdown(
    """
Deep Learning & Generative AI based Multiple Choice Question Answering.

Enter a question and five options to predict the **Top-3 most likely answers**.
"""
)

question = st.text_area(
    "Question",
    placeholder="Enter your MCQ question here..."
)

col1, col2 = st.columns(2)

with col1:
    A = st.text_input("Option A")
    B = st.text_input("Option B")
    C = st.text_input("Option C")

with col2:
    D = st.text_input("Option D")
    E = st.text_input("Option E")

if st.button("🚀 Predict", use_container_width=True):

    if not all([question, A, B, C, D, E]):
        st.warning("Please fill all fields.")
    else:

        top3, scores = predict(
            question,
            [A, B, C, D, E]
        )

        option_map = {
            "A": A,
            "B": B,
            "C": C,
            "D": D,
            "E": E
        }

        st.success("Prediction Complete!")

        st.subheader("🏆 Top 3 Predictions")

        medals = ["🥇", "🥈", "🥉"]

        for medal, label in zip(medals, top3):
            st.markdown(f"### {medal} {label}")
            st.write(option_map[label])

        st.subheader("Confidence Scores")

        df = pd.DataFrame({
            "Option": ["A", "B", "C", "D", "E"],
            "Score": scores
        })

        st.bar_chart(df.set_index("Option"))

st.divider()

st.markdown("### Example")

if st.button("Load Example"):

    st.session_state["loaded"] = True

if st.session_state.get("loaded", False):

    st.info(
        """
Question:

Which planet is known as the Red Planet?

A. Earth

B. Venus

C. Mars

D. Mercury

E. Saturn
"""
    )
