# GameDev Tutorial Summarizer

**What it is:** A tool that takes any YouTube tutorial on game dev (Unity, Unreal, Godot, Blender, Maya, GIMP, etc.) and spits out a clear, step-by-step action guide with complete code snippets.

**Why it exists:** Because building indie games usually means stitching together stuff from tutorials to build the foundation before making your own thing. Sometimes you just need the steps in text – to quickly check, skip the fluff (TLDW!), or reference easily. Existing AI video summarizers suck at giving devs the concise, actionable, *code included*, guides that actually need.

## Features
- Takes YouTube video URL as input
- Generates concise markdown summaries
- Saves output to specified filename

## Requirements
- Python 3.10+
- `uv` (Python package manager)

## Installation
1. Clone this repository
2. Install dependencies:
   ```bash
   uv sync
   ```
3. Create a `.env` file with your Gemini API key:
   ```
   GEMINI_API_KEY=your_api_key_here
   ```

## Usage
Run the script:
```bash
uv run main.py
```
You'll be prompted to:
1. Enter the YouTube video URL to summarize
2. Specify an output filename (without extension)

The summary will be saved as `[filename].md` in the current directory.

## Example
```bash
$ uv run main.py
Enter YouTube video URL to summarize: https://www.youtube.com/watch?v=soMeV1de0id
Enter output filename (without extension): video_summary
Success: Summary saved to video_summary.md
```

## Configuration
The system prompt can be customized by editing `system_prompt.md`.


## Q&A

**Q: It needs a Gemini API key. Is that free?**
    
A: Yes, a free tier key is completely sufficient. This tool uses the efficient `gemini-2.5-flash` model for watching and generating the guide.

**Q: It's not running locally!**

A: Correct, but **only** the YouTube URL leaves your machine. All video processing and AI generation happens on Google's servers. **NONE** of your local files or data are involved.

**Q: How good is the output quality?**

A: Tested on multiple tutorials – results are good, often flawless for creating actionable steps and extracting codes. It's *not* 100% magic, but highly usable. Try it on your tutorials and report issues if you find any!

**But note:** The free tier has usage limits. Heavy users *might* eventually need paid Gemini access, but for typical indie dev use, free should cover it.
