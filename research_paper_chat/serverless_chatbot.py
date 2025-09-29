import streamlit as st
import requests
import json
from streamlit_lottie import st_lottie
import os
from dotenv import load_dotenv

load_dotenv()

# Function to load Lottie file
def load_lottieurl(url : str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Load the brain animation
lottie_brain = load_lottieurl("https://assets4.lottiefiles.com/packages/lf20_SkhtL8.json")

# Function to call the API
def call_api(query):
    # Replace with your API endpoint
    api_url = os.getenv("API_URL")
    
    try:
        response = requests.post(str(api_url), json = {"user_query" : query})
        response.raise_for_status() # Raise an exception for bad status codes
        data = response.json()
        
        # If API Gateway wrapped it
        if "body" in data:
            return json.loads(data["body"])
        return data
    
    except requests.exceptions.RequestException as e:
        st.error(f"An Error occured while calling the API : - {str(e)}")
        return None
    except json.JSONDecodeError as e:
        st.error(f"Error Decoding JSON Response : {str(e)}")
        return None
    
# Streamlit App 
def main():
    st.set_page_config(page_title = "RAG AI Chatbot :",
                       page_icon = "🧠",
                       layout = "wide")
    st.title("🤖 AI Assistant")
    
    # User Input
    user_question = st.text_input("Ask Your question related to Arthiritis :")
    if st.button("Click To Get Answer"):
        if user_question:
            # Display spinning earth animation
            with st.spinner("Thinking ..."):
                brain_placeholder = st.empty()
                with brain_placeholder:
                    st_lottie(lottie_brain, height = 200, key = "brain")                    
                # Call API
                result = call_api(user_question)
                
                # Remove the spinning earth animation
                brain_placeholder.empty()
                
            if result:
                # Display the Responsible in good format
                st.subheader("Answer : ")
                st.write(result.get("answer", "No Answer Found"))
                
                # Display Additional Information
                with st.expander("See Details : "):
                    st.json({
                        "Query" : result.get("query", "N/A"),
                        #"Status Code" : result.get("statusCode", "N/A"),
                        "Source" :  result.get("reference", "N/A")
                    })
            else:
                st.error("Failed to get a Valid Response from the API")
        else:
            st.warning("Please Enter a Question ... ")
if __name__ == "__main__":
    main()                    
            