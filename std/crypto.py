import base64

class CryptoBox:

    def seal(self,text):
        return base64.b64encode(text.encode()).decode()

    def unseal(self,text):
        try:
            return base64.b64decode(text.encode()).decode()
        except:
            return ""