import gradio as gr
import pandas as pd

from predict_example import predict


def solve(question, A, B, C, D, E):

    top3, scores = predict(
        question,
        [A, B, C, D, E]
    )

    ranking = (
        f"🥇 {top3[0]}\n\n"
        f"🥈 {top3[1]}\n\n"
        f"🥉 {top3[2]}"
    )

    df = pd.DataFrame({
        "Option": ["A", "B", "C", "D", "E"],
        "Score": scores
    })

    return ranking, df


DESCRIPTION = """
# 🧠 Smart MCQ Solver

Deep Learning & Generative AI Project

Predicts the **Top-3 most likely answers**
for a Multiple Choice Question using
Sentence Transformer semantic similarity.

---

### Enter a question and five answer options.
"""


examples = [

[
"What is the capital of France?",
"Paris",
"London",
"Berlin",
"Madrid",
"Rome"
],

[
"Which planet is known as the Red Planet?",
"Earth",
"Venus",
"Mars",
"Mercury",
"Saturn"
],

[
"What is the process by which plants make food?",
"Respiration",
"Photosynthesis",
"Fermentation",
"Digestion",
"Evaporation"
]

]


with gr.Blocks(theme=gr.themes.Soft(), title="Smart MCQ Solver") as demo:

    gr.Markdown(DESCRIPTION)

    with gr.Row():

        with gr.Column(scale=2):

            question = gr.Textbox(
                label="Question",
                lines=4,
                placeholder="Enter the MCQ question..."
            )

            A = gr.Textbox(label="Option A")
            B = gr.Textbox(label="Option B")
            C = gr.Textbox(label="Option C")
            D = gr.Textbox(label="Option D")
            E = gr.Textbox(label="Option E")

            predict_btn = gr.Button(
                "🚀 Predict",
                variant="primary"
            )

        with gr.Column():

            ranking = gr.Textbox(
                label="🏆 Top 3 Predictions",
                lines=6
            )

            chart = gr.BarPlot(
                x="Option",
                y="Score",
                title="Confidence Scores"
            )

    predict_btn.click(
        solve,
        inputs=[question, A, B, C, D, E],
        outputs=[ranking, chart]
    )

    gr.Examples(
        examples,
        inputs=[
            question,
            A,
            B,
            C,
            D,
            E
        ]
    )


demo.launch()