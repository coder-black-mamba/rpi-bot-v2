from db_local import save_documents, query_documents
from llm_groq import call_groq_llm
from qs import qs


def save_to_file(text, filename):
    """
    # Saves text content to a file
    # Args:
        text: Text content to save
        filename: Name/path of file to save to
    """
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(text)
        print(f"✅ Successfully saved text to {filename}")
    except Exception as e:
        print(f"❌ Error saving to file: {e}")



def run_bot():
    # print("📘 ইনস্টিটিউট চ্যাটবট (বাংলা) চালু হয়েছে। 'exit' লিখে বন্ধ করুন।\n")
    print("\n📘 Institute Chatbot (Bangla) by Abu Sayed is running. Type 'exit' to stop.\n")

    while True:
        try:
            user_input = input("🙋 You: ")
            if user_input.lower() == "exit":
                break

            context_list = query_documents(user_input)
            context = "\n".join(context_list) if context_list else "কোনো context পাওয়া যায়নি।"
            response = call_groq_llm(user_input, context)
            save_to_file(response.choices[0].message.content, 'bot_response.txt')
            print(f"🤖 Rpi Bot: {response}")

        except Exception as e:
            # print(f"An error occurred: {e}")
            print(f"🤖 Rpi Bot : An error occurred")
            continue

 

try:
    # load_data()
    run_bot()
except Exception as e:
    print(f"An error occurred: {e}")
