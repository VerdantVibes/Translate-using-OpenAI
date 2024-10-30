from openai import OpenAI
from io import BytesIO
from PIL import Image
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("API_KEY")

client = OpenAI(api_key=api_key)




import os
from langchain.text_splitter import CharacterTextSplitter

def read_file(file_path):  
    """Read the content from a file."""  
    with open(file_path, 'r', encoding='utf-8') as file:  
        return file.read()  

def save_to_file(file_path, data):  
    """Save the data to a file."""  
    with open(file_path, 'w', encoding='utf-8') as file:  
        file.write(data)  

def split_text_to_paragraphs(text):  
    """Split the text into paragraphs using a text splitter."""  
    text_splitter = CharacterTextSplitter(separator="\n\n", chunk_size=1000, chunk_overlap=0)  
    return text_splitter.split_text(text)  

def mock_translate(paragraph):  
    """Mock function to simulate translation (replace this with actual API call)."""  
    # Simulate translation by reversing the text (for demonstration)  
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "assistant",
                "content": "Translate these sentences to German.",
            },
            {
                "role": "user",
                "content": paragraph
            }
        ],
    )
    # print(response.choices[0].message.content)
    print(response.choices[0].message.content)

def main(input_file_path, output_file_path):  
    # Read text file  
    text = read_file(input_file_path)  

    # Split text into paragraphs (chunks)  
    paragraphs = split_text_to_paragraphs(text)  

    # Translate each paragraph and collect the results  
    translated_paragraphs = []
    for i, paragraph in enumerate(paragraphs):  
        translated_text = mock_translate(paragraph)
        translated_paragraphs.append(translated_text)  

    # Join the translated paragraphs with double newlines to retain paragraph separation  
    translated_content = "\n\n".join(translated_paragraphs)  

    # Save translated content to the output file  
    save_to_file(output_file_path, translated_content)  

if __name__ == "__main__":  
    input_file = "text.txt"  
    output_file = "save.txt"  
    main(input_file, output_file)