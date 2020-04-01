from skpy import Skype

sk = Skype("avante-test202004@outlook.jp","avantetest202004")

c = sk.contacts["live:.cid.43066b9eed9b5a16"].chat
c.sendMsg("ハロー")