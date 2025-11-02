# Contributing to JARVIS AI Assistant

First off, thank you for considering contributing to JARVIS! 🎉

## How Can I Contribute?

### 🐛 Reporting Bugs

Before creating bug reports, please check the existing issues to avoid duplicates. When you create a bug report, include as many details as possible:

- **Use a clear and descriptive title**
- **Describe the exact steps to reproduce the problem**
- **Provide specific examples**
- **Describe the behavior you observed and what you expected**
- **Include screenshots if possible**
- **Include your Python version and OS**

### 💡 Suggesting Enhancements

Enhancement suggestions are tracked as GitHub issues. When creating an enhancement suggestion:

- **Use a clear and descriptive title**
- **Provide a detailed description of the suggested enhancement**
- **Explain why this enhancement would be useful**
- **List some examples of how it would be used**

### 🔧 Pull Requests

1. **Fork the repo** and create your branch from `main`
2. **Make your changes** following the code style
3. **Test your changes** thoroughly
4. **Update documentation** if needed
5. **Write clear commit messages**
6. **Submit a pull request**

## Code Style Guidelines

- Follow PEP 8 style guide for Python code
- Use meaningful variable and function names
- Add comments for complex logic
- Keep functions focused and small
- Add docstrings to functions

## Project Structure

```python
class VoiceAssistant:
    def __init__(self):
        # Initialize assistant
        
    def speak(self, text):
        # Text-to-speech
        
    def listen(self):
        # Voice recognition
        
    def your_new_feature(self):
        # Your code here
        
    def process_command(self, query):
        # Add command handling here
```

## Adding New Features

### Example: Adding a New Command

```python
# 1. Create the function
def your_new_feature(self):
    """Description of what this does"""
    try:
        # Your code here
        self.speak("Feature response")
    except Exception as e:
        self.speak("Error message")
        print(f"Error: {e}")

# 2. Add to process_command
def process_command(self, query):
    # ... existing code ...
    
    elif "your trigger" in query:
        self.your_new_feature()
```

### Example: Adding External API Integration

```python
# 1. Add API key to __init__
self.YOUR_API_KEY = "YOUR_API_KEY_HERE"

# 2. Create API function
def fetch_data_from_api(self):
    """Fetch data from external API"""
    try:
        if self.YOUR_API_KEY == "YOUR_API_KEY_HERE":
            self.speak("API key not configured")
            return
            
        url = "https://api.example.com/endpoint"
        response = requests.get(url, timeout=5)
        data = response.json()
        
        # Process data
        self.speak(f"Result: {data}")
        
    except Exception as e:
        self.speak("Unable to fetch data")
        print(f"Error: {e}")
```

## Testing

Before submitting a PR:

1. Test all existing commands still work
2. Test your new feature with various inputs
3. Test error handling
4. Test with and without internet connection (if applicable)
5. Test with and without API keys (if applicable)

## Documentation

When adding features, update:

1. **README.md** - Add to features list and commands
2. **show_help()** function - Add command description
3. **requirements.txt** - Add new dependencies
4. **Code comments** - Document complex logic

## Ideas for Contribution

Here are some features we'd love to see:

### High Priority
- [ ] Spotify integration
- [ ] Smart home device control
- [ ] Reminder/alarm system
- [ ] GUI interface

### Medium Priority
- [ ] Multi-language support
- [ ] Voice customization
- [ ] Conversation logging
- [ ] Custom wake word

### Nice to Have
- [ ] Mobile app
- [ ] Cloud sync
- [ ] Plugin system
- [ ] Voice training

## Questions?

Feel free to open an issue with the `question` label or reach out to the maintainers.

## Code of Conduct

- Be respectful and inclusive
- Welcome newcomers
- Accept constructive criticism
- Focus on what's best for the community

Thank you for contributing! 🚀
