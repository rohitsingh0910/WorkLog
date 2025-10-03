import threading
import speech_recognition as sr
import tkinter as tk
from tkinter import ttk
import openai
import json
import re

# ---------- CONFIG ----------
openai.api_key = "YOUR_OPENAI_API_KEY"  # Put your OpenAI API key here
listening = True
current_transcript = ""


# ---------- AI PROCESSING ----------
def generate_questions(text):
    try:
        prompt = f"""
        You are an interview question generator.
        Based on the candidate's speech below:

        "{text}"

        Generate EXACTLY 5 relevant interview questions.
        For each question, provide EXACTLY 4 short answer options.
        Respond ONLY with valid JSON in this format:

        [
            {{"question": "string", "options": ["string", "string", "string", "string"]}},
            ...
        ]
        """

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7
        )

        raw_text = response.choices[0].message.content.strip()
        print("\n--- RAW GPT RESPONSE ---\n", raw_text, "\n------------------------\n")

        # Try parsing directly
        try:
            return json.loads(raw_text)
        except:
            # Fallback: extract JSON part if GPT added extra text
            match = re.search(r"\[.*\]", raw_text, re.S)
            if match:
                return json.loads(match.group())
            return []

    except Exception as e:
        print("AI Error:", e)
        return []


# ---------- SPEECH RECOGNITION ----------
def listen_and_transcribe():
    global current_transcript
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)
        while True:
            if not listening:
                continue
            try:
                print("Listening...")
                audio = recognizer.listen(source, phrase_time_limit=5)
                text = recognizer.recognize_google(audio)
                print("You said:", text)
                current_transcript += " " + text
                update_transcript(current_transcript)

                if len(current_transcript.strip()) > 20:  # avoid empty/super short calls
                    questions = generate_questions(current_transcript)
                    update_questions(questions)

            except sr.UnknownValueError:
                pass
            except Exception as e:
                print("Error:", e)


# ---------- GUI FUNCTIONS ----------
def update_transcript(text):
    transcript_box.delete("1.0", tk.END)
    transcript_box.insert(tk.END, text)


def update_questions(questions):
    for widget in right_frame.winfo_children():
        widget.destroy()
    for q in questions:
        label = tk.Label(right_frame, text=q["question"], wraplength=350, justify="left")
        label.pack(anchor="w")
        dropdown = ttk.Combobox(right_frame, values=q["options"])
        dropdown.pack(anchor="w", pady=2)


def toggle_listening():
    global listening
    listening = not listening
    btn_pause.config(text="Resume" if not listening else "Pause")


# ---------- GUI SETUP ----------
root = tk.Tk()
root.geometry("900x600")
root.title("AI Interview Assistant")

left_frame = tk.Frame(root, width=450)
left_frame.pack(side="left", fill="both", expand=True)
transcript_box = tk.Text(left_frame, wrap="word")
transcript_box.pack(fill="both", expand=True)

right_frame = tk.Frame(root, width=450)
right_frame.pack(side="right", fill="both", expand=True)

btn_pause = tk.Button(left_frame, text="Pause", command=toggle_listening)
btn_pause.pack(side="bottom", pady=5)

# ---------- RUN THREAD ----------
threading.Thread(target=listen_and_transcribe, daemon=True).start()

root.mainloop()
