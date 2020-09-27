from recognizer import Recognizer

def main():
    try:
        rec = Recognizer()
        result = rec.recognizeAudioFile('./samples/file.wav')
        print(result)

    except Exception as e:
        print(f"Erro: {e}")

main()
