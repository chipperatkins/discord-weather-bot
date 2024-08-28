import json
import downloadForecastDiscussion
import plotGraph
from openai import OpenAI
import sys
import os

detailedForecast = downloadForecastDiscussion.main()
hourlyForecastJson = plotGraph.requestDataPeriods()

def sendMessage(textDict, API_KEY, assistantID, messagePrompt, instructions):
    client = OpenAI(api_key=API_KEY)
    thread = client.beta.threads.create()
    assistant = client.beta.assistants.retrieve(assistantID)

    message = client.beta.threads.messages.create(
        thread_id=thread.id,
        role="user",
        content= [
            {
                "type": "text",
                "text": messagePrompt,
            },
            {
                "type": "text",
                "text": textDict[0],
            },
                {
                "type": "text",
                "text": json.dumps(textDict[1]),
            },
        ],
        )

    run = client.beta.threads.runs.create_and_poll(
        thread_id=thread.id,
        assistant_id=assistant.id,
        instructions=instructions)

    if run.status == 'completed': 
      messages = client.beta.threads.messages.list(thread_id=thread.id)
      return messages.data[0].content[0].text.value
    else:
      return run.status
    
def askWillie(API_KEY, detailedForecast, hourlyForecastJson, prompt):
    assistantID = "asst_dTHANVwfjKodEuirH2fi6oHM"
    instructions = "Keep the update strictly to the weather and less than 9 sentances. Include any emojis as unicode."
    return sendMessage([detailedForecast, hourlyForecastJson], API_KEY, assistantID, prompt, instructions)

def askFrank(API_KEY):
   assistantID = "asst_R6gdepDHfkRBj8quXFdo6KFq"
   prompt = "What's my daily forecast? Include a description of today. Also include a description of the week ahead."
   detailedForecast = downloadForecastDiscussion.main()
   hourlyForecastJson = plotGraph.requestDataPeriods()
   return sendMessage([detailedForecast, hourlyForecastJson], API_KEY, assistantID, prompt, instructions="Format your reply in HTML for an email.")

def main():
    prompt = sys.argv[1]
    forecast = askWillie(os.environ.get('OPENAI_API_KEY'), detailedForecast, hourlyForecastJson, prompt)
    print(forecast)
    sys.stdout.flush()

if __name__ == "__main__":
   main()