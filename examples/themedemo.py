import gradio as gr
import random
import time
import sys
sys.path.append('../intel_gradio_theme/')
from intel_gradio_theme.spark_classic_blue import SparkTheme  # Import using the package name

# Instantiate the custom theme
theme = SparkTheme()

themecss = theme.load_css()

def print_like_dislike(x: gr.LikeData):
    print(x.index, x.value, x.liked)

def add_message(history, message):
    for x in message["files"]:
        history.append({"role": "user", "content": {"path": x}})
    if message["text"] is not None:
        history.append({"role": "user", "content": message["text"]})
    return history, gr.MultimodalTextbox(value=None, interactive=False)

def bot(history: list):
    response = random.choice(["Pere Monclus", "Krishna Ganugapati"]) #nosec
    history.append({"role": "assistant", "content": ""})
    for character in response:
        history[-1]["content"] += character
        time.sleep(0.05)
        yield history

def respond(message, chat_history):
    bot_message = random.choice(["Tell me more about it", 
                                 "Cool, but I'm not interested", 
                                 "Hmmmm, ok then"])  #nosec
    chat_history.append((message, bot_message))
    return "", chat_history

with gr.Blocks(theme=theme, css=themecss) as demo:  # Add custom CSS here
    
    header = SparkTheme.header("Gradio Theme Demo")  # Use the header from SparkTheme
    
    with gr.Tab("User View"):
        with gr.Row(height=700):
            with gr.Column(scale=2, min_width=300):
                gr.Markdown(
                    """
                    # Chat Interface
                    """)
                chatbot = gr.Chatbot(elem_id="chatbot", bubble_full_width=False, type="messages")
                chat_input = gr.MultimodalTextbox(
                    interactive=True,
                    file_count="multiple",
                    placeholder="Enter message or upload file...",
                    show_label=False,
                    sources=["microphone", "upload"],
                )
                with gr.Row():
                    gr.Slider(0, 512, value=256, step=8, label="Max Tokens in Response")
                    gr.Slider(0.0, 1.0, value=0.7, step=0.1, label="Temperature")

                    chat_msg = chat_input.submit(
                        add_message, [chatbot, chat_input], [chatbot, chat_input]
                    )
                    bot_msg = chat_msg.then(bot, chatbot, chatbot, api_name="bot_response")
                    bot_msg.then(lambda: gr.MultimodalTextbox(interactive=True), None, [chat_input])

                    chatbot.like(print_like_dislike, None, None, like_user_message=True)

            with gr.Column(scale=1, min_width=300):
                gr.Markdown(
                    """
                    # Documents

                    1) Example 1: Intel Edge Computing in Poland.pdf
                    2) Example 2: How Poland helped Intel to become the most valuable company in history.pdf
                    3) Example 3: Intel AI Stacks are trillion dollar business.pdf
                    """)
                gr.Button("Add new document")
    
    with gr.Tab("Developer View"):
        with gr.Row(height=700):
            gr.Markdown(
                """
                # What should go here:

                1) Explain technology behind - Vector Databases, etc.
                2) Show the flow of data
                3) Give details about the model used (family and model)

                """)

    footer = SparkTheme.footer()  # Use the footer from SparkTheme

gr.close_all()

demo.launch()