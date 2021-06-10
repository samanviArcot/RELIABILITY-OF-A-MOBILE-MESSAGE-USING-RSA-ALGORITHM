import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from Crypto.PublicKey import RSA
from Crypto import Random
from Crypto.Cipher import PKCS1_OAEP

class AppGrid(GridLayout):
    encrypted_text=bytes()
    decrypted_text=bytes()
    public_key=bytes()
    private_key=bytes()
    pre=""
    message=""
    mes=""
    def __init__(self,**kwargs):
        super(AppGrid, self).__init__()
        # self.inside=GridLayout()
        # self.inside.cols=1
        self.cols=1
        self.add_widget(Label(text="ENCRYPTION APP",color =(1, 1, 1, 1),font_size=32))
        self.press=Button(text="Share Public Key",color =(1, 0, 0, 1))
        self.press.bind(on_press=self.share_key)
        self.add_widget(self.press)
        self.press1 = Button(text="ENCRYPTION",color =(1, 1, 0, 1))
        self.press1.bind(on_press=self.Encryption_de)
        self.add_widget(self.press1)
        self.press2 = Button(text="DECRYPTION",color =(0, 1, 1, 1))
        self.press2.bind(on_press=self.Decryption_de)
        self.add_widget(self.press2)
    def Encryption_de(self,instance):
        self.remove_widget(self.press1)
        self.add_widget(Label(text="Enter Message",color =(1, 1, 0, 1)))
        self.message = TextInput()
        self.add_widget(self.message)
        self.press3 = Button(text="ENCRYPT", color=(1, 0, 0, 1))
        self.press3.bind(on_press=self.share_key)
        self.add_widget(self.press3)

    def Decryption_de(self, instance):
        self.remove_widget(self.press)
        self.remove_widget(self.press1)
        self.remove_widget(self.press2)
        self.add_widget(Label(text="Enter Encrypted Message",color =(0, 1, 1, 1)))
        self.public_key1 = TextInput(text="")
        self.add_widget(self.public_key1)
        self.press4 = Button(text="DECRYPT", color=(1, 1, 0, 1))
        self.press4.bind(on_press=self.share_key)
        self.add_widget(self.press4)

    def share_key(self,intsance):
        print(intsance.text)
        if(intsance.text=="Share Public Key"):
            key = RSA.generate(2048)
            self.private_key = key.exportKey('PEM')
            self.public_key = key.publickey().exportKey('PEM')
            self.remove_widget(self.press)
            self.txt = TextInput(text=str(self.public_key))
            self.add_widget(self.txt)
            print(self.public_key, self.private_key)
        elif(intsance.text=="ENCRYPT"):
            # key = RSA.generate(2048)
            # self.private_key = key.exportKey('PEM')
            # self.public_key = key.publickey().exportKey('PEM')
            self.remove_widget(self.press3)
            print(self.message.text)
            self.message=self.message.text
            self.message = str.encode(self.message)
            print(self.message)
            print(self.public_key)
            rsa_public_key = RSA.importKey(self.public_key)
            rsa_public_key = PKCS1_OAEP.new(rsa_public_key)
            self.encrypted_text = rsa_public_key.encrypt(self.message)
            self.add_widget(Label(text="Encrypted Text",color =(1, 0, 0, 1)))
            print(type(self.encrypted_text))
            encrypt=self.encrypted_text
            self.mes = TextInput(text=str(encrypt))
            self.add_widget(self.mes)
        else:
            self.remove_widget(self.press4)
            print(self.private_key)
            rsa_private_key = RSA.importKey(self.private_key)
            rsa_private_key = PKCS1_OAEP.new(rsa_private_key)
            self.decrypted_text = rsa_private_key.decrypt(self.encrypted_text)
            print('your decrypted_text is : {}'.format(self.decrypted_text))
            self.add_widget(Label(text="Decrypted Text"))
            print(self.decrypted_text)
            decrypt = self.decrypted_text
            decrypt=str(decrypt)
            decrypt=decrypt[2:len(decrypt)-1]
            self.mes = TextInput(text=decrypt)
            self.add_widget(self.mes)



class AppEncryption(App):
    def build(self):
        return AppGrid()

AppEncryption().run()
