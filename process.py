import json

def process_text(text):
    if isinstance(text, list):
        return ' '.join(item['text'] if isinstance(item, dict) else item for item in text)
    return text.replace("@mention(", "").replace(")", "")

def create_conversation_text(messages):
    conversation = []
    for msg in messages:
        if "text" in msg and "from" in msg:
            conversation.append(f"{msg['from']}: {msg['text']}")
    return "\n".join(conversation)

def save_text(text, output_file):
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(text)

if __name__ == "__main__":
    # Load and filter messages
    with open('Data/result.json', 'r') as file:
        data = json.load(file)
        messages = data["messages"]
        filtered_messages = [
            {
                "id": message["id"],
                "date": message["date"],
                "from": message["from"],
                "text": process_text(message["text"])
            }
            for message in messages 
            if message["type"] == "message"
        ]
    
    # Save filtered messages
    with open('Data/filtered_messages.json', 'w') as output_file:
        json.dump(filtered_messages, output_file, indent=2)
    
    # Create and save conversation text
    conversation_text = create_conversation_text(filtered_messages)
    save_text(conversation_text, "Data/conversation_text.txt")
    print("Filtered output saved in Data/filtered_messages.json /n")
    print("Conversation stream output saved in Data/conversation_text.txt /n")
