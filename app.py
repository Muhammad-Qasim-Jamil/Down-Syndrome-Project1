# # app.py
# import streamlit as st
# import pandas as pd
# from langchain_community.llms import Clarifai
# import os

# # Set Clarifai PAT as environment variable
# os.environ["CLARIFAI_PAT"] = '9d07ba8ac414496b8c07bb45216abbf5'

# # Load CSV dataset
# dataset = pd.read_csv('dataset/dataset.csv', encoding='latin1')
# dataset['Question'] = dataset['Question'].fillna('')

# model_url_or_id = 'https://clarifai.com/openai/chat-completion/models/openai-gpt-4-vision'
# clarifai_model = Clarifai(model_url=model_url_or_id)

# def get_response(user_input):
#     clarifai_response = clarifai_model.predict(user_input)
#     return clarifai_response

# def get_fallback_response(user_input):
#     # Fallback logic using GPT model
#     return get_response(user_input)

# def main():
#     st.title("Down Syndrome Chatbot")

#     # Your Streamlit app logic goes here

#     user_input = st.text_input("Enter your question:")
    
#     if st.button("Get Response"):
#         matched_row = dataset[dataset['Question'].str.contains(user_input, case=False, na=False)]

#         if not matched_row.empty:
#             bot_response = matched_row.iloc[0]['Answer']
#         else:
#             # Fallback to GPT model if question not found in the dataset
#             bot_response = get_fallback_response(user_input)

#         st.text("Bot Response:")
#         st.write(bot_response)

# if __name__ == '__main__':
#     main()

# app.py
import streamlit as st
import pandas as pd
from langchain_community.llms import Clarifai
import os

# Set Clarifai PAT as environment variable
os.environ["CLARIFAI_PAT"] = '9d07ba8ac414496b8c07bb45216abbf5'

# Load CSV dataset
dataset = pd.read_csv('dataset/dataset.csv', encoding='latin1')
dataset['Question'] = dataset['Question'].fillna('')

model_url_or_id = 'https://clarifai.com/openai/chat-completion/models/openai-gpt-4-vision'
clarifai_model = Clarifai(model_url=model_url_or_id)

def get_response(user_input):
    clarifai_response = clarifai_model.predict(user_input)
    return clarifai_response

def get_fallback_response(user_input):
    # Fallback logic using GPT model
    return get_response(user_input)

def main():
    st.title("Down Syndrome Chatbot")

    # HTML design using st.markdown
    html_code = """
    <div style="padding: 20px;">
        <h2>Custom HTML Design</h2>
        <input type="text" id="user_input" placeholder="Enter your question...">
        <button onclick="getResponse()">Get Response</button>
        <div id="bot_response"></div>
    </div>

    <script>
        function getResponse() {
            var user_input = document.getElementById('user_input').value.trim();
            
            // Trigger a Streamlit button click with the user input
            Streamlit.Button("Get Response", user_input);
        }
        
        // This function will be called when the Streamlit button is clicked
        Streamlit.setComponentValue("bot_response", function(bot_response) {
            // Update the HTML with the bot response
            document.getElementById('bot_response').innerText = "Bot Response: " + bot_response;
        });
    </script>
    """
    st.markdown(html_code, unsafe_allow_html=True)

    # Streamlit app logic
    user_input = st.text_input("Enter your question:")
    
    # Triggered when the Streamlit button is clicked
    if st.button("Get Response", key="Get Response"):
        matched_row = dataset[dataset['Question'].str.contains(user_input, case=False, na=False)]

        if not matched_row.empty:
            bot_response = matched_row.iloc[0]['Answer']
        else:
            # Fallback to GPT model if the question is not found in the dataset
            bot_response = get_fallback_response(user_input)

        # Display the bot response
        st.write("Bot Response:", bot_response)

if __name__ == '__main__':
    main()
