from faster_whisper import WhisperModel
import tempfile
import os

print("Loading Whisper Model...")

model = WhisperModel(
    "base",
    device="cpu",
    compute_type="int8"
)

print("Whisper Model Loaded")


def transcribe_audio(audio_bytes, language):

    try:

        with tempfile.NamedTemporaryFile(
            delete=False,
            suffix=".wav"
        ) as temp_file:

            temp_file.write(audio_bytes)

            temp_path = temp_file.name

        lang_map = {
            "English": "en",
            "Telugu": "te",
            "Hindi": "hi"
        }

        whisper_lang = lang_map.get(
            language,
            "en"
        )

        print("=" * 80)
        print("TRANSCRIBING AUDIO")
        print("Language:", whisper_lang)
        print("=" * 80)

        segments, info = model.transcribe(
            temp_path,
            language=whisper_lang,
            beam_size=5
        )
        print("Detected Language:", info.language)

        text = ""

        for segment in segments:

            text += segment.text + " "

        text = text.strip()

        print("=" * 80)
        print("TRANSCRIPT")
        print(text)
        print("=" * 80)

        os.remove(temp_path)

        return {
    "text": text,
    "detected_language": info.language
}

    except Exception as e:

        print("=" * 80)
        print("TRANSCRIPTION ERROR")
        print(e)
        print("=" * 80)

        return ""