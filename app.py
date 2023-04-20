import gradio as gr
import openai
import examples as chatbot_examples
from dotenv import load_dotenv
import os

load_dotenv()  # take environment variables from .env.

# In order to authenticate, secrets must have been set, and the user supplied credentials match
def auth(username, password):
    app_username = os.getenv("APP_USERNAME")
    app_password = os.getenv("APP_PASSWORD")

    if app_username and app_password:
        if(username == app_username and password == app_password):
            print("Logged in successfully.")
            return True
        else:
            print("Username or password does not match.")
    else:
        print("Credential secrets not set.")
    return False
    
# Define a function to get the AI's reply using the OpenAI API
def get_ai_reply(message, model="gpt-3.5-turbo", system_message=None, temperature=0, message_history=[]):
    # Initialize the messages list
    messages = []
    
    # Add the system message to the messages list
    if system_message is not None:
        messages += [{"role": "system", "content": system_message}]

    # Add the message history to the messages list
    if message_history is not None:
        messages += message_history
    
    # Add the user's message to the messages list
    messages += [{"role": "user", "content": message}]
    
    # Make an API call to the OpenAI ChatCompletion endpoint with the model and messages
    completion = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=temperature
    )
    
    # Extract and return the AI's response from the API response
    return completion.choices[0].message.content.strip()

# Define a function to handle the chat interaction with the AI model
def chat(model, system_message, message, chatbot_messages, history_state):
    # Initialize chatbot_messages and history_state if they are not provided
    chatbot_messages = chatbot_messages or []
    history_state = history_state or []
    
    # Try to get the AI's reply using the get_ai_reply function
    try:
        ai_reply = get_ai_reply(message, model=model, system_message=system_message, message_history=history_state)
    except Exception as e:
        # If an error occurs, raise a Gradio error
        raise gr.Error(e)
    
    # Append the user's message and the AI's reply to the chatbot_messages list
    chatbot_messages.append((message, ai_reply))
    
    # Append the user's message and the AI's reply to the history_state list
    history_state.append({"role": "user", "content": message})
    history_state.append({"role": "assistant", "content": ai_reply})
    
    # Return None (empty out the user's message textbox), the updated chatbot_messages, and the updated history_state
    return None, chatbot_messages, history_state

# Define a function to launch the chatbot interface using Gradio
def get_chatbot_app(additional_examples=[]):
    # Load chatbot examples and merge with any additional examples provided
    examples = chatbot_examples.load_examples(additional=additional_examples)
    
    # Define a function to get the names of the examples
    def get_examples():
        return [example["name"] for example in examples]

    # Define a function to choose an example based on the index
    def choose_example(index):
        if(index!=None):
            system_message = examples[index]["system_message"].strip()
            user_message = examples[index]["message"].strip()
            return system_message, user_message, [], []
        else:
            return "", "", [], []

    # Create the Gradio interface using the Blocks layout
    with gr.Blocks() as app:
        with gr.Tab("Conversation"):
            with gr.Row():
                with gr.Column():
                    # Create a dropdown to select examples
                    example_dropdown = gr.Dropdown(get_examples(), label="Examples", type="index")
                    # Create a button to load the selected example
                    example_load_btn = gr.Button(value="Load")
                    # Create a textbox for the system message (prompt)
                    system_message = gr.Textbox(label="System Message (Prompt)", value="You are a helpful assistant.")
                with gr.Column():
                    # Create a dropdown to select the AI model
                    model_selector = gr.Dropdown(
                        ["gpt-3.5-turbo"],
                        label="Model",
                        value="gpt-3.5-turbo"
                    )
                    # Create a chatbot interface for the conversation
                    chatbot = gr.Chatbot(label="Conversation")
                    # Create a textbox for the user's message
                    message = gr.Textbox(label="Message")
                    # Create a state object to store the conversation history
                    history_state = gr.State()
                    # Create a button to send the user's message
                    btn = gr.Button(value="Send")

                # Connect the example load button to the choose_example function
                example_load_btn.click(choose_example, inputs=[example_dropdown], outputs=[system_message, message, chatbot, history_state])
                # Connect the send button to the chat function
                btn.click(chat, inputs=[model_selector, system_message, message, chatbot, history_state], outputs=[message, chatbot, history_state])
        # Return the app
        return app
        
# Call the launch_chatbot function to start the chatbot interface using Gradio
# Set the share parameter to False, meaning the interface will not be publicly accessible
app = get_chatbot_app()
app.queue()  # this is to be able to queue multiple requests at once
app.launch(auth=auth)
