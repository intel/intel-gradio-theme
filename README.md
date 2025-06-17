[![OpenSSF Scorecard](https://api.scorecard.dev/projects/github.com/intel/intel-gradio-theme/badge)](https://scorecard.dev/viewer/?uri=github.com/intel/intel-gradio-theme)
[![CodeQL](https://github.com/intel/intel-gradio-theme/workflows/CodeQL/badge.svg)](https://github.com/intel/intel-gradio-theme/security/code-scanning)


# Intel® theme for Gradio

## Table of Contents
- [How to Use](#how-to-use)
- [What This Theme Provides](#what-this-theme-provides)
    - [Header & Footer Components](#header--footer-components)
        - [Header](#header)
        - [Footer](#footer)
- [Troubleshooting](#troubleshooting)
    - [Python dependency troubles](#python-dependency-troubles)
    - [CSS file not found error](#css-file-not-found-error)
    - [no_proxy environment variable](#no_proxy-environment-variable)
- [How to Provide Feedback or Request New Features](#how-to-provide-feedback-or-request-new-features)

## What is the Intel theme for Gradio
The Intel theme for Gradio uses **Gradio's native theming capabilities** to apply the Intel brand to a gradio application. It does not have any 3rd party dependencies other than gradio.

## How to Use
1. If using a virtual environment (strongly recommended), activate the virtual environment:
    ```sh
    source .venv/bin/activate
    ```

    Or in Windows:
    ```sh
    source .venv/Source/activate
    ```

2. Install the intel_gradio_theme package:
    ```sh
    pip install --prefer-binary git+https://github.com/intel/intel-gradio-theme.git
    ```

    intel_gradio_theme has release tags and specific versions can be targeted:
    ```sh
    pip install --prefer-binary git+https://github.com/intel/intel-gradio-theme.git@v0.1.5
    ```

3. Apply the theme to your Gradio app:
    ```python
    import gradio as gr
    from intel_gradio_theme import SparkTheme

    demo = gr.Interface(...)
    theme = SparkTheme()
    cssstyles = theme.load_css()
    demo.launch(theme=theme, css=cssstyles)
    ```

    If Blocks are used to create the interface, then apply the theme to the Blocks
    
    ```python
    with gr.Blocks(theme=theme, css=cssstyles) as demo:
    ```

## What This Theme Provides
There are two themes included in this repository:
* Spark Classic Blue is provided by importing `SparkTheme`
* Spark Tiber is provided by importing `SparkThemeTb`

The Spark Classic Blue theme uses the Intel Corporate Brand colors (Blue), while the Spark Tiber theme uses the Intel Tiber colors (aqua, cosmos, cobalt). Unless you know that your product line uses the Intel Tiber Brand, you should use the Spark Classic Blue theme (`SparkTheme`).

### Header & Footer Components

#### Header
To add a header to your Gradio app using the Intel theme, you can use the `header` method provided in the `SparkTheme` class. Here is an example:

```python
from intel_gradio_theme import SparkTheme

demo = gr.Interface(...)
theme = SparkTheme()
demo.launch(theme=theme, components=[theme.header("Welcome to My Gradio App")])
```

This will add a header with the specified text to your Gradio app.

#### Footer
To add a footer to your Gradio app using the Intel theme, you can use the `footer` method provided in the `SparkTheme` class. Here is an example:

```python
from intel_gradio_theme import SparkTheme

demo = gr.Interface(...)
theme = SparkTheme()
demo.launch(theme=theme, components=[theme.footer("Thank you for using our app")])
```

This will add a footer with the specified text to your Gradio app.

## Troubleshooting
### Python dependency troubles
If there are dependency problems, such as being unable to find gradio after installing it, then create a virtual environment and run from there. [Read more about using virtual environments in python](https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/).
```sh
python3 -m venv .venv
...
source .venv/bin/activate
...
export NO_PROXY=intel.com,localhost,127.0.0.1
...
pip install --prefer-binary git+https://github.com/intel/intel-gradio-theme.git
```

### CSS file not found error
If you encounter a `FileNotFoundError` indicating `No such file or directory: '.../intel_gradio_theme/spark.css'`, it means the CSS file is not being properly included in the package. To fix this please update to version 0.1.7 or newer.

### no_proxy environment variable
If you get the following error when running gradio:

```sh
ValueError: When localhost is not accessible, a shareable link must be created. Please set share=True or check your proxy settings to allow access to localhost.
```

ensure your environment variable for no_proxy is set:

```sh
export NO_PROXY=intel.com,localhost,127.0.0.1
```

## How to Provide Feedback or Request New Features

1. **Open an Issue**: Go to the [Issues](https://github.com/intel/intel-gradio-theme/issues) tab in the repository, click "New Issue," and describe your feedback or feature request.

Your feedback and feature requests are greatly appreciated and help improve the project!
