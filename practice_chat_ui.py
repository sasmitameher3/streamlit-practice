import streamlit as st
from llmware.models import ModelCatalog


def simple_chat_ui_app (model_name):

    st.title(f"Simple Chat with {model_name}")

    model = ModelCatalog().load_model(model_name, temperature=0.3, sample=True, max_output=250)

    # initialize chat history
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # display chat messages from history on app rerun
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # accept user input
    prompt = st.chat_input("Say something")
    if prompt:

        with st.chat_message("user"):
            st.markdown(prompt)

        with st.chat_message("assistant"):

            model_response = model.inference(prompt)

            # insert additional error checking / post-processing of output here
            bot_response = model_response["llm_response"]

            st.markdown(bot_response)

        st.session_state.messages.append({"role": "user", "content": prompt})
        st.session_state.messages.append({"role": "assistant", "content": bot_response})

    return 0


if __name__ == "__main__":

    #   a few representative good chat models that can run locally
    #   note: will take a minute for the first time it is downloaded and cached locally

    chat_models = ["phi-3-gguf",
                   "llama-2-7b-chat-gguf",
                   "llama-3-instruct-bartowski-gguf",
                   "openhermes-mistral-7b-gguf",
                   "zephyr-7b-gguf"]

    model_name = chat_models[0]

    simple_chat_ui_app(model_name)