# 🤖 PersonaBlend AI 🧠📝
Welcome to the world of PersonaBlend AI! 🚀 Where engaging, knowledgeable, and empathetic conversations converge seamlessly! This project represents the culmination of cutting-edge research in the realm of open-domain chatbots, harmoniously blending the brilliance of BlenderBot and ChatGPT within the powerful textbase framework. ✨

💻[Demo Video](https://drive.google.com/file/d/1Ku4BQFPep6l6mictVnZHXgFLM3v1toF9/preview)

### Abstract 📜
Building open-domain chatbots is a fascinating yet challenging pursuit in the realm of machine learning. While the scalability of neural models and training data has shown promise, our project delves deeper to unveil the true potential of chatbots. A meaningful conversation is an art, elegantly weaving engaging topics, attentive listening, insightful questions, enlightening answers, and just the right touch of empathy and personality. We've harnessed these elements to craft an advanced chatbot that excels across diverse communication scenarios.

### The Blend 🌐
PersonaBlend AI is a dynamic chatbot designed for everyday interactions. Empowered by [BlenderBot](https://huggingface.co/facebook/blenderbot-400M-distill), it thrives in friendly, human-like conversations, a feat achieved through rigorous training on the Humane Evaluation of communication. However, we recognize that certain contexts demand more than just casual discourse. For educational insights, intricate calculations, and comprehensive briefings, our chatbot seamlessly transitions to ChatGPT, delivering precision and knowledge tailored to the situation.

### Distress Management (Work in Progress) ⚠️
In a world where safety takes precedence, we're weaving an essential feature into PersonaBlend AI. By integrating distress-record, transcript, AWS, and Twilio (currently under development), our chatbot gains the ability to detect and respond to distress signals. It ensures timely communication with relevant authorities, offering an additional layer of security and unwavering support.



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
> I have implemented these features in [YourCompanion](https://github.com/KartikeyMish/yourcompanion) .

> For the API's Integration refer [models.py](https://github.com/KartikeyMish/textbase/blob/main/textbase/models.py) & realted to distress refer [voice.py](https://github.com/KartikeyMish/textbase/blob/main/textbase/voice.py)

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

