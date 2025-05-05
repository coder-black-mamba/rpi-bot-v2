from groq import Groq
from dotenv import load_dotenv

load_dotenv()



client = Groq()

def call_groq_llm(user_query,context,model="gemma2-9b-it"):
    print("Context: ", context)
    print("\n\n\n ")
    response = client.chat.completions.create(
    messages=[
        # Set an optional system message. This sets the behavior of the
        # assistant and can be used to provide specific instructions for
        # how it should behave throughout the conversation.
        {
            "role": "system",
            "content": "You are a helpful assistant of rajshahi polytechnic institute named রাজশাহীর লুকাল . You are a bot that can answer any question about the institute. Be polite and helpful.  do not use any religious or political words. Do not use any abusive words. Do not use any slang words. Do not use any bad words. Do not use any hate speech.Try to Answer in Bengali if the user does question in english answer in english , if it is mixed up then no proablem. do not use নমস্কার",
        },
        {
            "role": "system",
            "content": "You have been built by Abu Sayed , Student Of Computer Science and Technology Department,5th semester 1st shift -  Rajshahi Polytechnic Institute.",
        },
        # Set a user message for the assistant to respond to.
        {
            "role": "user",
            "content": user_query,
        }
    ],

    # The language model which will generate the completion.
    model=model,
    )

    return response

# Print the completion returned by the LLM.
if __name__ == "__main__":
    # Example usage
    user_query = "What is the history of Rajshahi Polytechnic Institute?"
    context = ""
    response = call_groq_llm(user_query, context)
    print(response['choices'][0]['message']['content'])
    