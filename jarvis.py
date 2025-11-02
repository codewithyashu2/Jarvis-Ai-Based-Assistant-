import speech_recognition as sr
import datetime
import webbrowser
import os
import sys
import requests
import wikipedia
import pyjokes
import pyautogui
import psutil
import json
import random
import subprocess
from pathlib import Path

# For Windows TTS
if sys.platform == "win32":
    import win32com.client

class VoiceAssistant:
    def __init__(self, name="Jarvis"):
        self.name = name
        self.recognizer = sr.Recognizer()
        
        # Use Windows SAPI
        if sys.platform == "win32":
            self.speaker = win32com.client.Dispatch("SAPI.SpVoice")
            print("✅ Using Windows SAPI for speech")
        else:
            self.speaker = None
            print("⚠️ Text-only mode")
        
        # API Keys Configuration
        self.WEATHER_API_KEY = "YOUR_OPENWEATHER_API_KEY"
        self.NEWS_API_KEY = "YOUR_NEWS_API_KEY"
        self.OPENAI_API_KEY = "YOUR_OPENAI_API_KEY"  # For AI Brain
        
        # Conversation context for AI
        self.conversation_history = []
        
        # Fun features data
        self.motivational_quotes = [
            "The only way to do great work is to love what you do.",
            "Believe you can and you're halfway there.",
            "Success is not final, failure is not fatal.",
            "The future belongs to those who believe in the beauty of their dreams.",
            "Don't watch the clock; do what it does. Keep going."
        ]
        
        self.fun_facts = [
            "Honey never spoils. Archaeologists have found 3000 year old honey in Egyptian tombs that was still edible.",
            "Octopuses have three hearts and blue blood.",
            "Bananas are berries, but strawberries aren't.",
            "A day on Venus is longer than its year.",
            "The shortest war in history lasted only 38 to 45 minutes."
        ]
    
    def speak(self, text):
        """Convert text to speech"""
        print(f"\n{self.name}: {text}")
        if self.speaker:
            try:
                self.speaker.Speak(text)
            except Exception as e:
                print(f"❌ Speech Error: {e}")
    
    def listen(self):
        """Listen to user's voice command"""
        with sr.Microphone() as source:
            print("\n" + "="*50)
            print("🎤 Listening... (Speak now)")
            print("="*50)
            self.recognizer.pause_threshold = 1
            self.recognizer.adjust_for_ambient_noise(source, duration=0.5)
            try:
                audio = self.recognizer.listen(source, timeout=5, phrase_time_limit=10)
                print("🔄 Processing your command...")
                query = self.recognizer.recognize_google(audio, language='en-in')
                print(f"✅ You said: '{query}'")
                return query.lower()
            except sr.WaitTimeoutError:
                return "none"
            except sr.UnknownValueError:
                return "none"
            except Exception as e:
                print(f"❌ Error: {e}")
                return "none"
    
    def greet(self):
        """Greet the user"""
        hour = datetime.datetime.now().hour
        if 0 <= hour < 12:
            greeting = "Good Morning!"
        elif 12 <= hour < 18:
            greeting = "Good Afternoon!"
        else:
            greeting = "Good Evening!"
        
        self.speak(greeting)
        self.speak(f"I am {self.name}, your advanced AI assistant. How may I help you?")
    
    # ==================== AI BRAIN ====================
    
    def ai_conversation(self, query):
        """Have intelligent conversation using OpenAI"""
        try:
            if self.OPENAI_API_KEY == "YOUR_OPENAI_API_KEY":
                self.speak("AI features require OpenAI API key. Using basic response mode.")
                self.basic_ai_response(query)
                return
            
            # Add to conversation history
            self.conversation_history.append({"role": "user", "content": query})
            
            # Call OpenAI API
            headers = {
                "Authorization": f"Bearer {self.OPENAI_API_KEY}",
                "Content-Type": "application/json"
            }
            
            data = {
                "model": "gpt-3.5-turbo",
                "messages": self.conversation_history,
                "max_tokens": 150,
                "temperature": 0.7
            }
            
            response = requests.post(
                "https://api.openai.com/v1/chat/completions",
                headers=headers,
                json=data,
                timeout=10
            )
            
            if response.status_code == 200:
                ai_response = response.json()["choices"][0]["message"]["content"]
                self.conversation_history.append({"role": "assistant", "content": ai_response})
                self.speak(ai_response)
            else:
                self.speak("I couldn't process that request.")
                
        except Exception as e:
            print(f"AI Error: {e}")
            self.basic_ai_response(query)
    
    def basic_ai_response(self, query):
        """Basic responses when OpenAI is not available"""
        responses = {
            "how are you": "I'm functioning perfectly! Thank you for asking. How can I assist you?",
            "who created you": "I was created to be your personal assistant and help you with various tasks.",
            "what can you do": "I can help with many things! Say 'help' to see all my features.",
        }
        
        for key, response in responses.items():
            if key in query:
                self.speak(response)
                return
        
        self.speak("I'm here to help! You can ask me about time, weather, news, or say 'help' for all features.")
    
    # ==================== COMMUNICATION ====================
    
    def send_whatsapp(self):
        """Send WhatsApp message"""
        try:
            self.speak("Opening WhatsApp Web. Please scan QR code if not logged in.")
            webbrowser.open("https://web.whatsapp.com")
            self.speak("You can now send your message through the web interface.")
        except Exception as e:
            self.speak("Unable to open WhatsApp")
            print(f"Error: {e}")
    
    def send_email_simple(self):
        """Open Gmail to compose email"""
        try:
            self.speak("Opening Gmail compose window")
            webbrowser.open("https://mail.google.com/mail/?view=cm&fs=1")
        except Exception as e:
            self.speak("Unable to open Gmail")
    
    # ==================== ADVANCED COMPUTER CONTROL ====================
    
    def get_system_info(self):
        """Get system information"""
        try:
            cpu_percent = psutil.cpu_percent(interval=1)
            memory = psutil.virtual_memory()
            battery = psutil.sensors_battery()
            
            info = f"CPU usage is {cpu_percent} percent. "
            info += f"RAM usage is {memory.percent} percent. "
            
            if battery:
                info += f"Battery is at {battery.percent} percent"
                if battery.power_plugged:
                    info += " and charging."
                else:
                    info += " and not charging."
            
            self.speak(info)
        except Exception as e:
            self.speak("Unable to fetch system information")
            print(f"Error: {e}")
    
    def set_brightness(self, level):
        """Set screen brightness (Windows)"""
        try:
            if sys.platform == "win32":
                import screen_brightness_control as sbc
                sbc.set_brightness(level)
                self.speak(f"Brightness set to {level} percent")
            else:
                self.speak("Brightness control not available on this system")
        except ImportError:
            self.speak("Brightness control module not installed. Run: pip install screen-brightness-control")
        except Exception as e:
            self.speak("Unable to set brightness")
    
    def open_file_or_folder(self, query):
        """Open any file or folder"""
        try:
            # Common locations
            locations = {
                "downloads": str(Path.home() / "Downloads"),
                "documents": str(Path.home() / "Documents"),
                "desktop": str(Path.home() / "Desktop"),
                "pictures": str(Path.home() / "Pictures"),
                "music": str(Path.home() / "Music"),
                "videos": str(Path.home() / "Videos"),
            }
            
            for location, path in locations.items():
                if location in query:
                    if sys.platform == "win32":
                        os.startfile(path)
                    else:
                        subprocess.call(["open", path])
                    self.speak(f"Opening {location} folder")
                    return
            
            self.speak("Folder not recognized. Try downloads, documents, or desktop.")
        except Exception as e:
            self.speak("Unable to open folder")
            print(f"Error: {e}")
    
    def shutdown_system(self):
        """Shutdown the system"""
        self.speak("Are you sure you want to shutdown? Say yes to confirm.")
        confirmation = self.listen()
        if "yes" in confirmation:
            self.speak("Shutting down the system in 10 seconds. Goodbye!")
            if sys.platform == "win32":
                os.system("shutdown /s /t 10")
        else:
            self.speak("Shutdown cancelled")
    
    def restart_system(self):
        """Restart the system"""
        self.speak("Are you sure you want to restart? Say yes to confirm.")
        confirmation = self.listen()
        if "yes" in confirmation:
            self.speak("Restarting the system in 10 seconds")
            if sys.platform == "win32":
                os.system("shutdown /r /t 10")
        else:
            self.speak("Restart cancelled")
    
    # ==================== INFORMATION & UPDATES ====================
    
    def get_stock_price(self, symbol):
        """Get stock price"""
        try:
            # Using Alpha Vantage free API (requires API key)
            self.speak(f"Let me check the stock price for {symbol}")
            # For demo, opening Google Finance
            url = f"https://www.google.com/finance/quote/{symbol}:NASDAQ"
            webbrowser.open(url)
            self.speak(f"Opening stock information for {symbol}")
        except Exception as e:
            self.speak("Unable to fetch stock price")
    
    def get_crypto_price(self, crypto="bitcoin"):
        """Get cryptocurrency price"""
        try:
            url = f"https://api.coingecko.com/api/v3/simple/price?ids={crypto}&vs_currencies=usd"
            response = requests.get(url, timeout=5)
            data = response.json()
            
            if crypto in data:
                price = data[crypto]["usd"]
                self.speak(f"The current price of {crypto} is {price} US dollars")
            else:
                self.speak("Unable to fetch cryptocurrency price")
        except Exception as e:
            self.speak("Unable to fetch cryptocurrency information")
            print(f"Error: {e}")
    
    def get_news(self, category="general"):
        """Get news headlines"""
        try:
            if self.NEWS_API_KEY == "YOUR_NEWS_API_KEY":
                self.speak("News API key not configured. Opening Google News instead.")
                webbrowser.open("https://news.google.com")
                return
            
            url = f"https://newsapi.org/v2/top-headlines?country=in&category={category}&apiKey={self.NEWS_API_KEY}"
            response = requests.get(url, timeout=5)
            data = response.json()
            
            if data["status"] == "ok":
                articles = data["articles"][:3]
                self.speak(f"Here are the top {category} news headlines")
                for i, article in enumerate(articles, 1):
                    self.speak(f"News {i}: {article['title']}")
            else:
                self.speak("Unable to fetch news")
        except Exception as e:
            self.speak("Unable to fetch news")
            print(f"Error: {e}")
    
    def translate_text(self, query):
        """Translate text"""
        try:
            self.speak("What language do you want to translate to?")
            target_lang = self.listen()
            
            self.speak("What text do you want to translate?")
            text = self.listen()
            
            # Using Google Translate (opening in browser for now)
            url = f"https://translate.google.com/?sl=auto&tl={target_lang}&text={text}"
            webbrowser.open(url)
            self.speak("Opening Google Translate")
        except Exception as e:
            self.speak("Unable to translate")
    
    # ==================== LEARNING & KNOWLEDGE ====================
    
    def solve_math(self, expression):
        """Solve math problems"""
        try:
            # Clean expression
            expression = expression.replace("plus", "+").replace("minus", "-")
            expression = expression.replace("multiply", "*").replace("times", "*")
            expression = expression.replace("divide", "/").replace("divided by", "/")
            expression = expression.replace("power", "**").replace("squared", "**2")
            
            result = eval(expression)
            self.speak(f"The answer is {result}")
        except Exception as e:
            self.speak("I couldn't solve that. Please try a simpler expression.")
            print(f"Error: {e}")
    
    def define_word(self, word):
        """Define a word using Wikipedia"""
        try:
            self.speak(f"Searching for definition of {word}")
            result = wikipedia.summary(word, sentences=2)
            self.speak(result)
        except Exception as e:
            self.speak(f"I couldn't find a definition for {word}")
    
    def study_timer(self, minutes):
        """Start a study/pomodoro timer"""
        try:
            self.speak(f"Starting a {minutes} minute study timer")
            self.speak("I'll notify you when time is up. Focus on your work!")
            
            # This is a simple implementation
            # In a real scenario, you'd want this to run in a separate thread
            import time
            time.sleep(minutes * 60)
            self.speak("Time's up! Take a break.")
        except Exception as e:
            self.speak("Unable to start timer")
    
    # ==================== FUN FEATURES ====================
    
    def tell_joke(self):
        """Tell a joke"""
        try:
            joke = pyjokes.get_joke()
            self.speak(joke)
        except Exception as e:
            jokes = [
                "Why do programmers prefer dark mode? Because light attracts bugs!",
                "Why did the computer go to the doctor? Because it had a virus!",
                "What do you call a bear with no teeth? A gummy bear!"
            ]
            self.speak(random.choice(jokes))
    
    def motivational_quote(self):
        """Share a motivational quote"""
        quote = random.choice(self.motivational_quotes)
        self.speak(quote)
    
    def fun_fact(self):
        """Share a fun fact"""
        fact = random.choice(self.fun_facts)
        self.speak(fact)
    
    def play_game(self):
        """Play a number guessing game"""
        self.speak("Let's play a guessing game! I'm thinking of a number between 1 and 10.")
        number = random.randint(1, 10)
        attempts = 3
        
        while attempts > 0:
            self.speak(f"You have {attempts} attempts left. Guess the number.")
            guess = self.listen()
            
            try:
                guess_num = int(''.join(filter(str.isdigit, guess)))
                if guess_num == number:
                    self.speak("Congratulations! You guessed it right!")
                    return
                elif guess_num < number:
                    self.speak("Too low!")
                else:
                    self.speak("Too high!")
                attempts -= 1
            except:
                self.speak("Please say a number")
        
        self.speak(f"Game over! The number was {number}")
    
    def flip_coin(self):
        """Flip a coin"""
        result = random.choice(["Heads", "Tails"])
        self.speak(f"The coin landed on {result}")
    
    def roll_dice(self):
        """Roll a dice"""
        result = random.randint(1, 6)
        self.speak(f"You rolled a {result}")
    
    # ==================== BASIC FEATURES ====================
    
    def get_time(self):
        """Tell current time"""
        time_str = datetime.datetime.now().strftime("%I:%M %p")
        self.speak(f"The time is {time_str}")
    
    def get_date(self):
        """Tell current date"""
        date_str = datetime.datetime.now().strftime("%B %d, %Y")
        day_str = datetime.datetime.now().strftime("%A")
        self.speak(f"Today is {day_str}, {date_str}")
    
    def get_weather(self, city="Delhi"):
        """Get weather"""
        try:
            if self.WEATHER_API_KEY == "YOUR_OPENWEATHER_API_KEY":
                self.speak("Weather API not configured. Opening weather website.")
                webbrowser.open(f"https://www.google.com/search?q=weather+{city}")
                return
            
            url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={self.WEATHER_API_KEY}&units=metric"
            response = requests.get(url, timeout=5)
            data = response.json()
            
            if data["cod"] == 200:
                temp = data["main"]["temp"]
                description = data["weather"][0]["description"]
                self.speak(f"Temperature in {city} is {temp} degrees celsius. Weather is {description}.")
            else:
                self.speak("Unable to fetch weather")
        except Exception as e:
            self.speak("Unable to fetch weather")
    
    def search_wikipedia(self, query):
        """Search Wikipedia"""
        try:
            search_term = query.replace("wikipedia", "").replace("search", "").strip()
            self.speak(f"Searching Wikipedia for {search_term}")
            result = wikipedia.summary(search_term, sentences=2)
            self.speak(result)
        except Exception as e:
            self.speak("Unable to find that on Wikipedia")
    
    def search_web(self, query):
        """Search Google"""
        search_term = query.replace("search", "").replace("google", "").strip()
        url = f"https://www.google.com/search?q={search_term}"
        webbrowser.open(url)
        self.speak(f"Searching for {search_term}")
    
    def open_youtube(self, query=None):
        """Open YouTube"""
        if query and "search" in query:
            search_term = query.replace("search", "").replace("youtube", "").strip()
            url = f"https://www.youtube.com/results?search_query={search_term}"
            webbrowser.open(url)
            self.speak(f"Searching YouTube for {search_term}")
        else:
            webbrowser.open("https://www.youtube.com")
            self.speak("Opening YouTube")
    
    def take_screenshot(self):
        """Take screenshot"""
        try:
            timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"screenshot_{timestamp}.png"
            screenshot = pyautogui.screenshot()
            screenshot.save(filename)
            self.speak(f"Screenshot saved as {filename}")
        except Exception as e:
            self.speak("Unable to take screenshot")
    
    def open_website(self, website):
        """Open websites"""
        sites = {
            "google": "https://www.google.com",
            "youtube": "https://www.youtube.com",
            "github": "https://www.github.com",
            "gmail": "https://mail.google.com",
            "facebook": "https://www.facebook.com",
            "instagram": "https://www.instagram.com",
            "twitter": "https://www.twitter.com",
            "linkedin": "https://www.linkedin.com",
            "reddit": "https://www.reddit.com",
            "amazon": "https://www.amazon.com",
        }
        
        for site, url in sites.items():
            if site in website:
                webbrowser.open(url)
                self.speak(f"Opening {site}")
                return
        self.speak("Website not recognized")
    
    def open_application(self, app_name):
        """Open applications"""
        try:
            if sys.platform == "win32":
                apps = {
                    "notepad": "notepad.exe",
                    "calculator": "calc.exe",
                    "paint": "mspaint.exe",
                    "chrome": "chrome.exe",
                    "edge": "msedge.exe",
                    "word": "winword.exe",
                    "excel": "excel.exe",
                }
                if app_name in apps:
                    os.system(apps[app_name])
                    self.speak(f"Opening {app_name}")
                else:
                    self.speak("Application not found")
        except Exception as e:
            self.speak("Unable to open application")
    
    def show_help(self):
        """Show commands"""
        commands = """
        ═══════════════════════════════════════════════════════════
        🤖 JARVIS - ADVANCED AI ASSISTANT COMMANDS
        ═══════════════════════════════════════════════════════════
        
        💬 AI BRAIN:
        • "ask [question]" - Ask any question
        • "who created you" - Learn about me
        
        📧 COMMUNICATION:
        • "send whatsapp" - Open WhatsApp
        • "send email" - Open Gmail
        
        💻 COMPUTER CONTROL:
        • "system info" - CPU, RAM, Battery status
        • "shutdown" / "restart" - System control
        • "brightness [level]" - Set brightness
        • "open downloads/documents/desktop" - Open folders
        
        📊 INFORMATION:
        • "stock price [symbol]" - Stock prices
        • "crypto price [coin]" - Cryptocurrency prices
        • "news" / "tech news" - Latest news
        • "translate" - Translate text
        
        📚 LEARNING:
        • "solve [math problem]" - Math solver
        • "define [word]" - Word definitions
        • "study timer [minutes]" - Pomodoro timer
        
        🎮 FUN:
        • "tell me a joke" - Random joke
        • "motivate me" - Motivational quote
        • "fun fact" - Interesting fact
        • "play game" - Number guessing game
        • "flip coin" / "roll dice" - Random choice
        
        ⏰ BASICS:
        • "time" / "date" - Current time/date
        • "weather [city]" - Weather info
        • "search [topic]" - Google search
        • "wikipedia [topic]" - Wikipedia search
        • "screenshot" - Take screenshot
        • "open [website/app]" - Open apps
        
        ═══════════════════════════════════════════════════════════
        """
        print(commands)
        self.speak("I've listed all my advanced features in the console!")
    
    def process_command(self, query):
        """Process commands"""
        if "none" in query:
            return True
        
        # Exit
        if "exit" in query or "quit" in query or "goodbye" in query:
            self.speak("Goodbye! Have a productive day!")
            return False
        
        # AI Brain
        elif "ask" in query or "tell me about" in query:
            question = query.replace("ask", "").replace("tell me about", "").strip()
            self.ai_conversation(question)
        
        # Communication
        elif "whatsapp" in query:
            self.send_whatsapp()
        elif "send email" in query or "compose email" in query:
            self.send_email_simple()
        
        # Computer Control
        elif "system info" in query or "system status" in query:
            self.get_system_info()
        elif "brightness" in query:
            try:
                level = int(''.join(filter(str.isdigit, query)))
                self.set_brightness(level)
            except:
                self.speak("Please specify brightness level")
        elif "shutdown" in query:
            self.shutdown_system()
        elif "restart" in query:
            self.restart_system()
        elif "open downloads" in query or "open documents" in query or "open desktop" in query or "open pictures" in query:
            self.open_file_or_folder(query)
        
        # Information
        elif "stock price" in query or "stock" in query:
            symbol = query.replace("stock", "").replace("price", "").strip().upper()
            self.get_stock_price(symbol if symbol else "AAPL")
        elif "crypto" in query or "bitcoin" in query:
            crypto = "bitcoin"
            if "ethereum" in query:
                crypto = "ethereum"
            elif "dogecoin" in query:
                crypto = "dogecoin"
            self.get_crypto_price(crypto)
        elif "news" in query:
            category = "technology" if "tech" in query else "general"
            self.get_news(category)
        elif "translate" in query:
            self.translate_text(query)
        
        # Learning
        elif "solve" in query or "calculate" in query or "what is" in query:
            expression = query.replace("solve", "").replace("calculate", "").replace("what is", "").strip()
            self.solve_math(expression)
        elif "define" in query or "meaning of" in query:
            word = query.replace("define", "").replace("meaning of", "").strip()
            self.define_word(word)
        elif "study timer" in query or "timer" in query:
            try:
                minutes = int(''.join(filter(str.isdigit, query)))
                self.study_timer(minutes)
            except:
                self.speak("Please specify minutes for the timer")
        
        # Fun
        elif "joke" in query:
            self.tell_joke()
        elif "motivate" in query or "motivation" in query:
            self.motivational_quote()
        elif "fun fact" in query or "fact" in query:
            self.fun_fact()
        elif "play game" in query or "game" in query:
            self.play_game()
        elif "flip coin" in query or "coin" in query:
            self.flip_coin()
        elif "roll dice" in query or "dice" in query:
            self.roll_dice()
        
        # Basics
        elif "time" in query:
            self.get_time()
        elif "date" in query:
            self.get_date()
        elif "weather" in query:
            city = query.replace("weather", "").replace("in", "").strip()
            self.get_weather(city if city else "Delhi")
        elif "wikipedia" in query:
            self.search_wikipedia(query)
        elif "search" in query and "google" in query:
            self.search_web(query)
        elif "youtube" in query:
            self.open_youtube(query)
        elif "screenshot" in query:
            self.take_screenshot()
        elif "open" in query:
            if any(site in query for site in ["google", "youtube", "github", "gmail", "facebook", "instagram"]):
                self.open_website(query)
            else:
                app_name = query.replace("open", "").strip()
                self.open_application(app_name)
        elif "who are you" in query:
            self.speak("I am Jarvis, your advanced AI assistant with multiple capabilities!")
        elif "help" in query or "what can you do" in query:
            self.show_help()
        else:
            self.speak("I'm not sure about that. Try asking me something else or say 'help'")
        
        return True
    
    def run(self):
        """Main loop"""
        print("\n" + "="*70)
        print("🤖 JARVIS - ADVANCED AI VOICE ASSISTANT")
        print("="*70)
        print("\n✨ NEW FEATURES ADDED:")
        print("   • AI Brain for conversations")
        print("   • Communication tools")
        print("   • Advanced computer control")
        print("   • Information & updates")
        print("   • Learning assistance")
        print("   • Fun features & games")
        print("\n💡 Say 'help' to see all commands\n")
        
        self.greet()
        
        while True:
            query = self.listen()
            if not self.process_command(query):
                break
            print("\n" + "-"*70 + "\n")

if __name__ == "__main__":
    try:
        assistant = VoiceAssistant(name="Jarvis")
        assistant.run()
    except KeyboardInterrupt:
        print("\n\n👋 Jarvis shutting down. Goodbye!")
    except Exception as e:
        print(f"\n❌ Critical Error: {e}")