from google import genai
from google.genai import types
from dotenv import load_dotenv

def main():
    try:
        # Get user input
        video_url = input("Enter YouTube video URL to summarize: ")
        dst_filename = input("Enter output filename (without extension): ")

        load_dotenv()
        
        # The client gets the API key from the environment variable `GEMINI_API_KEY`.
        client = genai.Client()

        # Load system prompt from file
        with open("system_prompt.md", "r", encoding="utf-8") as f:
            system_prompt = f.read()

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            config=types.GenerateContentConfig(
                system_instruction=system_prompt
            ),
            contents= types.Content(
                parts=[
                    types.Part(file_data=types.FileData(file_uri=video_url)),
                    types.Part(text='Please summarize the tutorial video.')
                ]
            )
        )

        # Save output to markdown file
        with open(f"./{dst_filename}.md", "w", encoding="utf-8") as f:
            f.write(response.text)

        print(f"Success: Summary saved to {dst_filename}.md")
        return 0

    except Exception as e:
        print(f"Error: {str(e)}")
        return 1

if __name__ == "__main__":
    exit(main())
