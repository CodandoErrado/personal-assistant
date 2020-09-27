import speech_recognition as sr

class Recognizer():
    """ Classe para transcricão de voz para texto
    """
    
    def __init__(self):
        self.rec = sr.Recognizer()

    def formatResponse(self, filename, transcription):
        response = {
            'filename': filename,
            'transcription': transcription
        }
        return response


    def recognizeAudioFile(self, filename):
        """ Gera uma transcricão para arquivos de áudio em formato wav, utilizando
        o speech-to-text do pocketspinx

        Arguments:
            filename {str} -- Nome do arquivo

        Returns:
            response {dict} Dicionário com nome do arquivo e transcricão
        """
        
        with sr.AudioFile(filename) as source:
            audio = self.rec.record(source)

            try:
                text = self.rec.recognize_sphinx(audio)
                return self.formatResponse(filename,text)

            except Exception as e:
                raise Exception(e)

