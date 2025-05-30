class Audio:
    def __init__(self, audioId, callbackUrl, path, model):
        self.audioId = audioId
        self.callbackUrl = callbackUrl
        self.savePath = path
        self.model = model


class Transcription:
    def __init__(self, audioId, transcription):
        self.audioId = audioId
        self.transcription = transcription
