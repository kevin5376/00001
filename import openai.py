import openai

from dotenv import dotenv_values

config = dotenv_values(".env")

openai.api_key = config['xxx'] 


def generate_content(prompt, max_tokens=400, temperature=0.3):
    response = openai.Completion.create(
        model='text-davinci-002',
        prompt=prompt,
        max_tokens=max_tokens,
        temperature=temperature
    )

    generated_text = response.choices[0].text
    return generated_text


def main():
    while True:
        print("Choose the type of content to generate:")
        print("1. Paragraph")
        print("2. Character Description")
        print("3. Dialogue")
        print("4. Exit")
        
        choice = input("Enter your choice (1/2/3/4): ")
        
        if choice == '1':
            prompt = input("What should the paragraph be about? ")
            content_type = "paragraph"
        elif choice == '2':
            prompt = input("Describe a character: ")
            content_type = "character description"
        elif choice == '3':
            prompt = input("Write a dialogue: ")
            content_type = "dialogue"
        elif choice == '4':
            print("Exiting the Storytelling Assistant.")
            break
        else:
            print("Invalid choice. Please select a valid option.")
            continue
        
        generated_content = generate_content(prompt)
        
        print(f"Generated {content_type}:\n")
        print(generated_content)
        print("\n")

if __name__ == "__main__":
    main()
