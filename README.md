# 🤖 PersonaBlend AI 🧠📝

 PersonaBlend AI is a project that combines the capabilities of BlenderBot and ChatGPT, creating an advanced chatbot with diverse conversational personas. ✨

## Framework: Textbase
✨ Textbase is a framework for building chatbots using NLP and ML. ✨

Just implement the `on_message` function in `main.py`, and Textbase will take care of the rest! 😊

Since it is just Python, you can use whatever models, libraries, vector databases, and APIs you want.

## Project Features 🚀

- Integration of HuggingFace's BlenderBot api 🤖
- Integration of OpenAI's GPT-3.5 Turbo 🚄
- distress-record for conversation history 📜
- transcript and AWS integration (work in progress) 🌐
- Twilio integration (work in progress) 📱

## Installation and Setup 🛠️

1. Clone the repository:

    ```
    git clone https://github.com/yourusername/personablend-ai
    cd personablend-ai
    ```

2. Install the dependencies using Poetry:

    ```
    poetry shell
    poetry install
    ```

## Getting Started 🚀

1. Set up the necessary API keys:
   - Configure Hugging Face's BlenderBot credentials 🤖
   - Set up OpenAI's GPT-3.5 Turbo credentials 🚄
   - Configure AWS credentials for transcript and other services 🌐
   - Configure Twilio credentials for SMS integration 📱

2. Implement the `on_message` function in `main.py`.

3. Start the development server:

    ```
    poetry run python personablend-ai/textbase/textbase_cli.py test main.py
    ```

4. Go to http://localhost:4000 to start chatting with your PersonaBlend AI bot! The bot will automatically reload when you make changes to the code.

## Future Enhancements 🌈

- [ ] PyPI package for easy installation 📦
- [ ] SMS integration using Twilio 📱
- [ ] Web deployment via `textbase deploy` 🌐
- [ ] Native integration of additional models (Claude, Llama, etc.) 🤩

## Contributions 🤝

Contributions are welcome! If you have any suggestions, feedback, or code improvements, feel free to open an issue or submit a pull request.

Happy chatting with your PersonaBlend AI bot! 🌐🤖

