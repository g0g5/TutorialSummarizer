# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a **GameDev Tutorial Summarizer** - a Python tool that takes YouTube video URLs and generates concise, actionable markdown summaries with complete code snippets for game development tutorials. It uses Google's Gemini AI to analyze video content and extract step-by-step instructions.

## Key Commands

### Environment Setup
```bash
uv sync                    # Install dependencies
uv run main.py            # Run the application
```

### Running the Application
The tool will prompt for:
1. YouTube video URL to summarize
2. Output filename (without extension)

The summary will be saved as `[filename].md` in the current directory.

## Architecture

### Core Components

- **main.py**: Single-file application containing the core logic
  - Initializes Google GenAI client with API key from environment
  - Loads system prompt from `system_prompt.md`
  - Processes YouTube video URL using Gemini 2.5 Flash model
  - Saves markdown output to user-specified filename

- **system_prompt.md**: Contains detailed instructions for the AI model
  - Defines the role as "Game Development Tutorial Summarizer"
  - Specifies output formatting requirements
  - Includes constraints and examples for generating high-quality summaries

### Dependencies

- `google-genai`: Google's Gemini AI client library
- `python-dotenv`: Environment variable management for API keys

### Configuration

- **API Key**: Set `GEMINI_API_KEY` in `.env` file
- **System Prompt**: Edit `system_prompt.md` to customize AI behavior
- **Model**: Uses `gemini-2.5-flash` for video processing

## Development Notes

- The application processes video content entirely on Google's servers - only the YouTube URL is transmitted
- Uses efficient Gemini Flash model to stay within free tier limits
- Output format is strictly defined to ensure consistent, actionable summaries
- Error handling wraps the entire process in try-catch with user-friendly messages