import sys
sys.path.append('../intel_gradio_theme/')

import gradio as gr
from intel_gradio_theme.spark_tb import SparkThemeTb
from intel_gradio_theme.spark_classic_blue import SparkTheme

theme = SparkThemeTb()

themecss = theme.load_css()

with gr.Blocks(theme=theme, css=themecss) as demo:
    header = SparkTheme.header("Spark Gradio Theme Demo")
    with gr.Column(scale=6, elem_id="app"):
        with gr.Column(variant="panel"):
            gr.Markdown(
                """
                # Theme Builder
                ## How to Use
                1. Clone the repository:
                    ```sh
                    git clone https://github.com/yourusername/gradio-spark-theme.git
                    ```
                2. Navigate to the project directory:
                    ```sh
                    cd gradio-spark-theme
                    ```
                3. Install the required dependencies:
                    ```sh
                    pip install -r requirements.txt
                    ```
                4. Apply the theme to your Gradio app:
                    ```python
                    import gradio as gr
                    from spark_theme import apply_theme

                    demo = gr.Interface(...)
                    apply_theme(demo, theme="spark-classic-blue")
                    demo.launch()
                    ```


                ## What This Theme Provides
                There are two themes included in this repository:
                * `spark-classic-blue`
                * `spark-tiber` - *coming soon*

                The `spark-classic-blue` theme uses the Intel Corporate Brand colors (Blue), while the `spark-tiber` theme uses the Intel Tiber colors (aqua, cosmos, cobalt). Unless you know that your product line uses the Intel Tiber Brand, you should use the `spark-class-blue` theme.

                ### Additional Components

                #### Header
                To add a header to your Gradio app using the Spark Island Theme, you can use the `add_header` function provided in the `spark_theme` module. Here is an example:

                ```python
                from spark_theme import add_header

                demo = gr.Interface(...)
                add_header(demo, text="Welcome to My Gradio App", color="blue", font_size=24)
                demo.launch()
                ```

                This will add a header with the specified text, color, and font size to your Gradio app.

                #### Footer
                To add a footer to your Gradio app using the Spark Island Theme, you can use the `add_footer` function provided in the `spark_theme` module. Here is an example:

                ```python
                from spark_theme import add_footer
                from spark_tb import SparkThemeTb

                demo = gr.Interface(...)
                add_footer(demo, text="Thank you for using our app", color="blue", font_size=18)
                demo.launch()
                ```

                This will add a footer with the specified text, color, and font size to your Gradio app.
                """
            )

        name = gr.Textbox(
            label="Name",
            info="Full name, including middle name. No special characters.",
            placeholder="John Doe",
            value="John Doe",
            interactive=True,
        )

        gr.Interface(lambda x: x, "number", "textbox")

        with gr.Row():
            slider1 = gr.Slider(label="Slider 1")
            slider2 = gr.Slider(label="Slider 2")
        gr.CheckboxGroup(["A", "B", "C"], label="Checkbox Group")

        with gr.Row():
            with gr.Column(variant="panel", scale=1):
                gr.Markdown("## Panel 1")
                radio = gr.Radio(
                    ["A", "B", "C"],
                    label="Radio",
                    info="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.",
                )
                drop = gr.Dropdown(
                    ["Option 1", "Option 2", "Option 3"], show_label=False
                )
                drop_2 = gr.Dropdown(
                    ["Option A", "Option B", "Option C"],
                    multiselect=True,
                    value=["Option A"],
                    label="Dropdown",
                    interactive=True,
                )
                check = gr.Checkbox(label="Go")
            with gr.Column(variant="panel", scale=2):
                img = gr.Image(
                    "images/local_image.svg",  # Use a local image file
                    label="Image",
                    height=320,
                )
                with gr.Row():
                    go_btn = gr.Button("Go", variant="primary")
                    clear_btn = gr.Button("Clear", variant="secondary")
                    cancel_btn = gr.Button("Cancel", variant="cancel")

                with gr.Row():
                    btn1 = gr.Button("Button 1", size="sm")
                    btn2 = gr.UploadButton(size="sm")
                    stop_btn = gr.Button("Stop", variant="stop", size="sm")

        gr.Examples(
            examples=[
                [
                    "A",
                    "Option 1",
                    ["Option B"],
                    True,
                ],
                [
                    "B",
                    "Option 2",
                    ["Option B", "Option C"],
                    False,
                ],
            ],
            inputs=[radio, drop, drop_2, check],
            label="Examples",
        )

        with gr.Row():
            gr.Dataframe(value=[[1, 2, 3], [4, 5, 6], [7, 8, 9]], label="Dataframe")
            gr.JSON(
                value={"a": 1, "b": 2, "c": {"test": "a", "test2": [1, 2, 3]}},
                label="JSON",
            )
            gr.Label(value={"cat": 0.7, "dog": 0.2, "fish": 0.1})
            gr.File()
        with gr.Row():
            gr.ColorPicker()
            gr.Video(
                "videos/local_video.mp4"  # Use a local video file
            )
            gr.Gallery(
                [
                    ("images/local_image1.svg", "lion"),  # Use local image files
                    ("images/local_image2.svg", "logo"),
                    ("images/local_image3.svg", "tower"),
                ],
                height="200px",
                columns=2,
            )

        with gr.Row():
            with gr.Column(scale=2):
                chatbot = gr.Chatbot(
                    value=[
                        {"role": "user", "content": "Hello"},
                        {"role": "assistant", "content": "Hi there! How can I help you?"},
                    ],
                    label="Chatbot",
                    type="messages",
                )
                multimodal = gr.MultimodalTextbox(
                    interactive=True, show_label=False
                )
            with gr.Column(scale=1):
                with gr.Accordion("Advanced Settings"):
                    gr.Markdown("Hello")
                    gr.Number(label="Chatbot control 1")
                    gr.Number(label="Chatbot control 2")
                    gr.Number(label="Chatbot control 3")

        gr.Audio()
        gr.HTML("<div>Custom HTML</div>")
        gr.HighlightedText(value=[("Hello", "Greeting"), ("world", "Object")])
        #gr.BarPlot(value={"data": [1, 2, 3], "labels": ["A", "B", "C"]}, label="Bar Plot")
        #gr.LinePlot(value={"data": [1, 2, 3], "labels": ["A", "B", "C"]}, label="Line Plot")
        #gr.ScatterPlot(value={"data": [1, 2, 3], "labels": ["A", "B", "C"]}, label="Scatter Plot")
        gr.ImageMask(value="images/local_image.svg", label="Image Mask")  # Use a local image file
        gr.Sketchpad(value="images/local_image.svg", label="Sketchpad")  # Use a local image file
        gr.Code(value="print('Hello, world!')", language="python", label="Code")
        gr.Markdown(value="# Markdown", label="Markdown")
        gr.HTML(value="<div>HTML</div>", label="HTML")
        gr.Video(value="videos/local_video.mp4", label="Video")  # Use a local video file
        gr.Audio(value="videos/local_audio.mp3", label="Audio")  # Use a local audio file
        gr.File(value="local_file.txt", label="File")  # Use a local file
        gr.Image(value="images/local_image.svg", label="Image")  # Use a local image file
        gr.Gallery(value=[
            ("images/local_image1.svg", "lion"),  # Use local image files
            ("images/local_image2.svg", "logo"),
            ("images/local_image3.svg", "tower"),
        ], label="Gallery")
        gr.Chatbot(
            value=[
                {"role": "user", "content": "Hello"},
                {"role": "assistant", "content": "Hi there! How can I help you?"},
            ],
            label="Chatbot",
            type="messages",
        )
        gr.MultimodalTextbox(value="Hello", label="Multimodal Textbox")
        gr.Dataframe(value=[[1, 2, 3], [4, 5, 6], [7, 8, 9]], label="Dataframe")
        gr.JSON(value={"a": 1, "b": 2, "c": {"test": "a", "test2": [1, 2, 3]}}, label="JSON")
        gr.Label(value={"cat": 0.7, "dog": 0.2, "fish": 0.1}, label="Label")
        gr.File(value="local_file.txt", label="File")  # Use a local file
        gr.ColorPicker(value="#ff0000", label="Color Picker")
        gr.Video(value="videos/local_video.mp4", label="Video")  # Use a local video file
        gr.Gallery(value=[
            ("images/local_image1.svg", "lion"),  # Use local image files
            ("images/local_image2.svg", "logo"),
            ("images/local_image3.svg", "tower"),
        ], label="Gallery")
        gr.DateTime(),
    footer = SparkThemeTb.footer()

demo.launch()