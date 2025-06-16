import gradio as gr
import requests
import json
import os
import time
import io
from PIL import Image

# Function to generate image using Hugging Face Inference API
def generate_image_via_api(prompt, negative_prompt, guidance_scale, num_inference_steps, seed):
    # API key from environment variable
    api_key = os.getenv("HUGGINGFACE_API_KEY", "")
    
    if not api_key:
        return None, -1, "Please set the HUGGINGFACE_API_KEY environment variable"
    
    # Set up the API request with a model that's definitely supported by the Inference API
    API_URL = "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-xl-base-1.0"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    
    # Prepare the payload
    payload = {
        "inputs": prompt,
        "parameters": {
            "negative_prompt": negative_prompt,
            "guidance_scale": float(guidance_scale),
            "num_inference_steps": int(num_inference_steps)
        }
    }
    
    # Add seed if it's not random (-1)
    if seed != -1:
        payload["parameters"]["seed"] = int(seed)
    else:
        # Generate random seed for reproducibility
        import random
        seed = random.randint(0, 1000000) #nosec
        payload["parameters"]["seed"] = seed
    
    # Make the API request
    try:
        response = requests.post(API_URL, headers=headers, json=payload)
        
        if response.status_code == 200:
            # Convert the image data to a PIL Image
            image = Image.open(io.BytesIO(response.content))
            return image, seed, "Image generated successfully using Stable Diffusion XL!"
        elif response.status_code == 503:
            # Model is loading
            return None, seed, "The model is currently loading on Hugging Face's servers. Please try again in a few moments."
        else:
            # Handle error
            error_text = f"Error: API returned status code {response.status_code}"
            try:
                error_text += f" - {response.json().get('error', '')}"
            except:
                pass
            return None, seed, error_text
    except Exception as e:
        return None, seed, f"Error: {str(e)}"

# Create Gradio interface
with gr.Blocks() as demo:
    gr.Markdown("# Stable Diffusion XL Image Generator (Cloud-Hosted)")
    
    with gr.Row():
        with gr.Column():
            api_status = gr.Textbox(label="API Status", value="Ready to generate using hosted model")
            
            prompt = gr.Textbox(label="Prompt", placeholder="Enter a description of the image you want to generate...")
            negative_prompt = gr.Textbox(label="Negative Prompt", placeholder="What you don't want in the image...")
            
            with gr.Accordion("Advanced Settings", open=False):
                guidance_scale = gr.Slider(minimum=1, maximum=20, value=7.5, step=0.5, label="Guidance Scale")
                steps = gr.Slider(minimum=10, maximum=50, value=30, step=1, label="Inference Steps")
                seed = gr.Number(value=-1, label="Seed (-1 for random)")
                
            generate_button = gr.Button("Generate Image")
            
        with gr.Column():
            output_image = gr.Image(label="Generated Image")
            used_seed = gr.Number(label="Seed Used")
    
    def run_generation(prompt, negative_prompt, guidance_scale, steps, seed):
        image, used_seed_val, status = generate_image_via_api(prompt, negative_prompt, guidance_scale, steps, seed)
        return image, used_seed_val, status
    
    generate_button.click(
        run_generation,
        inputs=[prompt, negative_prompt, guidance_scale, steps, seed],
        outputs=[output_image, used_seed, api_status]
    )
    
    gr.Markdown("""
    ## Instructions
    1. Make sure you have set your Hugging Face API key as the environment variable `HUGGINGFACE_API_KEY`
    2. Enter a descriptive prompt for what you want to generate
    3. Optionally add a negative prompt for elements you want to avoid
    4. Adjust advanced settings if needed
    5. Click "Generate Image" to create your image using the cloud-hosted model
    
    Note: This demo uses Hugging Face's hosted Inference API, so no models are loaded locally.
    You'll need an internet connection and a Hugging Face API key to use this application.
    """)

# Launch the app locally
if __name__ == "__main__":
    # Check if API key is available
    if not os.getenv("HUGGINGFACE_API_KEY"):
        print("⚠️ Warning: No HUGGINGFACE_API_KEY environment variable found.")
        print("You will need to set this to use the hosted model.")
        print("Get a free API key at https://huggingface.co/settings/tokens")
        print("\nYou can set it with:")
        print("export HUGGINGFACE_API_KEY=\"your_api_key_here\"")
    else:
        print("✓ Hugging Face API key found in environment variables")
    
    print("\nStarting Gradio application with cloud-hosted model...")
    demo.launch(share=False, inbrowser=True)