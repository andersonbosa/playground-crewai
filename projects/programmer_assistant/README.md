# projects/programmer_assistant


## About 

- Gu, the Specialist Software Engineer Agent

GU is an agent specializing in software engineering, designed to assist in programming tasks and provide technical guidance.It is able to generate code based on provided requirements and answer technical questions, offering clear explanations and relevant recommendations.

## Installation


## Usage

To use the GU agent, you can execute the script `main.py` providing the following options:

- `--coding "YOUR REQUEST"`: Uses Gu agent programming ability to generate code based on your request.
- `--mentoring "YOUR QUESTION"`: Uses Gu agent mentoring ability to receive technical guidance in response to your question.

### Example of use

```bash
python main.py --coding "Implement a function to order a Python list using bubble-sort"
```

```bash
python main.py --mentoring "What is the difference between inheritance and composition in object -oriented programming?"
```

### Backup results

The results of interactions with agent GU are saved in the `outputs` folder. Each file generated contains the date, type of interaction and a description of the request.

### Dependencies

- Python 3.x
- CrewAI
- dotenv

### Settings

Be sure to configure the following environment variables in the `.env` file:

- `GOOGLE_API_KEY`: Your Google API key to use Gemini service (required)

## Credits

This project was developed by [Anderson Bosa](https://github.com/andersonbosa).
