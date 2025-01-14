from openai import OpenAI
from tiktoken import encoding_for_model
import os
from datetime import datetime

# Initialize OpenAI client
client = OpenAI()

def count_tokens(text, model="gpt-3.5-turbo"):
    encoding = encoding_for_model(model)
    tokens = encoding.encode(text)
    return len(tokens)


def save_text(text, output_file):
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(text)

def save_qa(question, answer):
    # Create Chats directory if it doesn't exist
    if not os.path.exists('Chats'):
        os.makedirs('Chats')
    
    # Generate timestamp for unique filename
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    filename = f"Chats/qa_{timestamp}.md"
    
    # Format content in markdown
    content = f"""# Question & Answer - {timestamp}

## Question
{question}

## Answer
{answer}
"""
    
    # Save to file
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)
    
    return filename

def ask_question(conversation_text, user_question):
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant. Please answer questions about the provided conversation context. and output it in markdown format."},
            {"role": "user", "content": f"Here is the conversation context:\n\n{conversation_text}\n\nQuestion: {user_question}"}
        ]
    )
    answer = completion.choices[0].message.content
    
    # Save Q&A to file
    qa_file = save_qa(user_question, answer)
    print(f"\nQ&A saved to: {qa_file}")
    
    return answer

def interactive_qa_session(conversation_text):
    print("Enter your questions (type 'quit' to exit):")
    while True:
        question = input("\nYour question: ")
        if question.lower() == 'quit':
            break
            
        answer = ask_question(conversation_text, question)
        print("\nAnswer:")
        print(answer)



# Main execution
if __name__ == "__main__":
    # Read the conversation text
    with open("Data/conversation_text.txt", 'r', encoding='utf-8') as f:
        conversation_text = f.read()
    
    # Start interactive Q&A session
    interactive_qa_session(conversation_text)
