from cryptography.fernet import Fernet

s = "gAAAAABhXztbKmk_2ALnJSawKjelg2wmn-hdq5dtpIJK0KbveL1pioAJRdNOzuh91acsA0ZFil5VOrSF8oAT4VoV_opezc8BTQMjsV3wkvq78OSEG850pGA="

code = bytes(s, "utf-8")
def call_key(): return open("pass.key", "rb").read()
key = call_key()
b = Fernet(key)
decoded_code = b.decrypt(code)
print(decoded_code)