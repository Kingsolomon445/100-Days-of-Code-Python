import PyPDF3
import pyttsx3
import pdfplumber

import os

pdf_file = input("Enter the path to the pdf file you would like to convert to audio speech: ")


def get_pages():
    pdf = open(pdf_file, 'rb')
    pdf_reader = PyPDF3.PdfFileReader(pdf)
    pages = pdf_reader.numPages
    return pages


def get_text():
    all_text = ""
    with pdfplumber.open(pdf_file) as pdf:
        for idx in range(get_pages()):
            page = pdf.pages[idx]
            page_text = page.extract_text()
            all_text += page_text
    return all_text


def pdf_to_audio():
    text = get_text()
    choice = input("Type 'save' to save the audio, Type 'say' to say the audio: ").lower().strip()
    engine = pyttsx3.init()
    if choice == "say":
        engine.say(text)
    elif choice == "save":
        file_path = os.path.join(os.getcwd(), 'audio.mp3')
        try:
            engine.save_to_file(text, file_path)
            print("File saved to", file_path)
        except Exception as e:
            print("An error occurred while saving the file:", e)
    else:
        print("Invalid choice! Choose again!")
        pdf_to_audio()
    engine.runAndWait()


pdf_to_audio()
