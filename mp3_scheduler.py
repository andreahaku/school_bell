import streamlit as st
import time
import threading
from pydub import AudioSegment
from pydub.playback import play

ALARM_FILE = "alarms.txt"

def load_alarms():
    try:
        with open(ALARM_FILE, "r") as f:
            return sorted([line.strip() for line in f.readlines() if line.strip()])
    except FileNotFoundError:
        return []

def save_alarms(alarms):
    with open(ALARM_FILE, "w") as f:
        f.write("\n".join(alarms) + "\n")

class MP3SchedulerApp:
    def __init__(self):
        self.schedule = load_alarms()
        self.running = True
        self.processed_alarms = set()
        self.scheduler_thread = threading.Thread(target=self.scheduler, daemon=True)
        self.scheduler_thread.start()

    def add_time(self, time_value):
        if self.validate_time_format(time_value) and time_value not in self.schedule:
            self.schedule.append(time_value)
            self.schedule.sort()
            save_alarms(self.schedule)
        else:
            st.error("Invalid Time Format or Duplicate Entry. Use HH:MM.")

    def remove_time(self, time_value):
        if time_value in self.schedule:
            self.schedule.remove(time_value)
            save_alarms(self.schedule)

    def validate_time_format(self, time_value):
        try:
            time.strptime(time_value, "%H:%M")
            return True
        except ValueError:
            return False

    def scheduler(self):
        while self.running:
            now = time.strftime("%H:%M:%S")
            now_time = time.strftime("%H:%M")
            if now_time in self.schedule and now_time not in self.processed_alarms:
                seconds = int(time.strftime("%S"))
                if seconds == 0:  # Ensure it plays exactly at 00 seconds
                    self.processed_alarms.add(now_time)
                    sound = AudioSegment.from_mp3("school-bell.mp3")
                    play(sound)
                    time.sleep(len(sound) / 1000)  # Sleep only for the duration of the sound
                    self.processed_alarms.remove(now_time)  # Do not remove from schedule
            time.sleep(0.5)  # Check every half second to ensure precision

app = MP3SchedulerApp()

st.title("New Marigold School Bell")

st.write("### Scheduled Times")
cols = st.columns(2)  # Create two columns

for index, time_value in enumerate(app.schedule):
    with cols[index % 2]:  # Alternate between the two columns
        col1, col2 = st.columns([4, 1])
        with col1:
            st.markdown(
                f"""
                <div style="padding: 2px; border: 1px solid #ddd; border-radius: 8px; background-color: #040; 
                            font-size: 24px; font-weight: bold; color: white; text-align: center;">
                    {time_value}
                </div>
                """,
                unsafe_allow_html=True
            )
        with col2:
            if st.button("🗑️", key=f"del_{time_value}", help="Delete"):
                app.remove_time(time_value)
                st.rerun()

st.divider()

st.write("### Add New Alarm")
new_time = st.text_input("Set Time (HH:MM)")
if st.button("Add Time"):
    app.add_time(new_time)
    st.rerun()

# Requirements file content
requirements_content = """streamlit\npydub\nffmpeg"""

with open("requirements.txt", "w") as f:
    f.write(requirements_content)
