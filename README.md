# <img src="logo.png" width="30"> J.A.R.V.I.S. - Just A Rather Very Intelligent System

<div align="center">
  <img src="logo.png" width="200">
  <p><i>Your AI-powered assistant that brings the future to your desktop</i></p>
</div>

A sophisticated voice-controlled personal assistant inspired by Iron Man's JARVIS, meticulously crafted in Python to streamline your digital workflow and enhance your productivity. Running continuously in the background, JARVIS is always ready to respond to your commands.

## ✨ Features

- 🎙️ **Advanced Voice Recognition** - Natural language processing for smooth human-computer interaction
- 🌐 **Web & App Control** - Seamlessly open websites and launch applications with simple voice commands
- 🎵 **Smart Media Control** - Play and control music on YouTube and Spotify hands-free
- ⏰ **Intelligent Time Management** - Set personalized alarms and schedules with voice reminders
- 🔋 **Real-time System Monitoring** - Keep track of battery status with timely alerts
- 🖥️ **Secure System Control** - Safely shutdown, restart, or put your device to sleep with password protection
- 🪟 **Effortless Window Management** - Navigate between tabs, virtual desktops, and windows using just your voice
- 🔄 **Self-Recovery** - Automatically restarts if interrupted, ensuring continuous operation

## 🚀 Quick Start

```bash
# Clone the repository
git clone https://github.com/yourusername/jarvis.git
cd jarvis

# Create a virtual environment
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

## 🔧 Configuration

1. **Personalize JARVIS**: Adjust file paths in scripts if needed (especially for notification icons)
2. **Custom Schedules**: Modify `schedule.txt` to set up your daily reminders
3. **Enhanced Security**: Edit the password in `Automation_Brain.py` for system actions
4. **System Integration**: Ensure your microphone and speakers are properly configured

## 💻 Usage

### Starting JARVIS

Three simple ways to bring JARVIS to life:

1. **Double-click** `run_jarvis.bat` from File Explorer
2. **Desktop Shortcut**:
   - Right-click on `run_jarvis.bat` → Create shortcut
   - Drag the shortcut to your desktop
   - Rename to "JARVIS" for easy access
   - Optionally customize the icon

3. **Command Line**:
```bash
run_jarvis.bat
```

JARVIS will run continuously in the background until you manually close the window, and will automatically restart if it encounters any issues.

### 🗣️ Voice Commands

| Command | Function |
|---------|----------|
| "Open website [name]" | Opens your preferred website |
| "Open app [name]" | Launches any installed application |
| "Play music [song name]" | Streams your favorite music on YouTube |
| "Play some music on Spotify" | Starts your Spotify playlist |
| "Check battery" | Reports current battery level and status |
| "Tell me to [activity] at [time]" | Sets a customized schedule reminder |
| "Shutdown my device" | Securely powers off your computer after password verification |
| "Next desktop" | Smoothly switches to the next virtual desktop |

## 📁 Project Structure

```
├── Automation/           # System automation and control modules
├── DATA/                 # Dialogue responses and configuration data
├── SpeechToText/         # Voice recognition and processing modules
├── TextToSpeech/         # Voice synthesis and audio output modules
├── Time_Operations/      # Schedule and alarm management system
├── Jarvis.py             # Main application controller
├── Alert.py              # Notification and alert system
├── co_Brain.py           # Core AI logic and processing engine
├── run_jarvis.bat        # Continuous execution batch script
└── requirements.txt      # Project dependencies
```

## 🔄 Core Dependencies

- `Mohit_STT` - Advanced speech recognition technology
- `psutil` - Comprehensive system monitoring
- `requests` - Seamless web integration
- `playsound` - High-quality audio playback
- `pyautogui` - Sophisticated GUI automation
- `pywhatkit` - Intelligent web automation
- `winotify` - Elegant Windows notifications

## 💡 Future Enhancements

- 🧠 Machine learning capabilities for personalized responses
- 🌦️ Weather integration for forecasts and alerts
- 📅 Calendar synchronization with Google and Microsoft accounts
- 📱 Mobile companion app for on-the-go control
- 🔍 Advanced web searching and information retrieval

## 👨‍💻 Contributing

JARVIS thrives on community contributions! Whether you're fixing bugs, adding features, or improving documentation, your help makes JARVIS more intelligent. Please feel free to submit a Pull Request.

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

<div align="center">
  <p><b>Powered by Python and inspired by science fiction</b></p>
  <p>© 2025 JARVIS Project</p>
</div> 