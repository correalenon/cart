**Install Dependencies**
* Install the required packages using the `requirements.txt` file:
   ```bash
   pip install -r requirements.txt
   ```

**Set Up Your OpenAI API Key**
* Create a .env file in the root directory of the project.
* Add your OpenAI API key to the `.env` file:
   ```bash
   OPENAI_API_KEY='Your-OpenAI-API-Key-Here'
   ```

### Usage
Make sure the fictional store's application is running before running the chatbot. To run, 
simply execute the `chatbot.py` script:
   ```bash
   chainlit run chatbot.py -w --port 8000
```