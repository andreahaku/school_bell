# MP3 Scheduler (Streamlit Version)

## 📌 Overview

This is a **Streamlit-based MP3 Scheduler** that allows you to schedule alarms that play an MP3 file at specific times.

## 🚀 Features

- **Add alarms** for specific times of the day.
- **Persistent storage** using a text file (`alarms.txt`).
- **Automatic playback** of an MP3 file when an alarm is triggered.
- **Easy removal** of scheduled alarms.
- **Modern web-based UI** using Streamlit.

---

## 📥 Installation

### **1️⃣ Install Dependencies**

Before running the application, install the required Python packages:

```bash
pip install streamlit pydub ffmpeg
```

### **2️⃣ Install FFmpeg (Required for Audio Playback)**

FFmpeg is required for **PyDub** to play MP3 files.

- **Ubuntu/Debian:**
  ```bash
  sudo apt install ffmpeg
  ```
- **MacOS (Homebrew):**
  ```bash
  brew install ffmpeg
  ```
- **Windows:**
  1. Download FFmpeg from [ffmpeg.org](https://ffmpeg.org/download.html).
  2. Add the FFmpeg `bin` directory to your system `PATH`.

---

## ▶️ Running the Application

Run the following command in the project directory:

```bash
streamlit run mp3_scheduler.py
```

This will start the **Streamlit web app**, and you can access it in your browser.

---

## 🛠️ How to Use

1. **Set Time (HH:MM)** - Enter a time in `HH:MM` format.
2. **Click "Add Time"** - Adds the alarm to the scheduled list.
3. **View Scheduled Alarms** - Alarms are displayed in a two-column layout.
4. **Delete Alarms** - Click the 🗑️ icon to remove an alarm.
5. **Alarms Automatically Play** - The app will play `school-bell.mp3` at the exact scheduled time.

---

## 📂 File Structure

```
📁 MP3_Scheduler
│── mp3_scheduler.py   # Main Streamlit application
│── alarms.txt         # Stores scheduled alarms
│── school-bell.mp3    # Alarm sound file
│── requirements.txt   # Dependencies for the app
```

---

## ❓ Troubleshooting

### **MP3 does not play**

- Ensure **FFmpeg** is installed and working.
- Check if `school-bell.mp3` exists in the project directory.

### **UI does not update immediately**

- If an alarm is added but the UI does not update, try refreshing the page.

---

## 🏁 Notes

- **The app must remain running** for alarms to work.
- Alarms persist in `alarms.txt` and will be reloaded when the app starts.

---

## 📜 License

This project is **open-source** and free to use.
