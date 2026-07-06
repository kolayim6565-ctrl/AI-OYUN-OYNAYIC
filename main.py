from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.spinner import Spinner
from kivy.utils import platform
from kivy.clock import Clock

class OyunAsistaniArayuz(BoxLayout):
    def __init__(self, **kwargs):
        super(OyunAsistaniArayuz, self).__init__(orientation='vertical', padding=20, spacing=15, **kwargs)
        
        # Başlık
        self.add_widget(Label(text="🤖 YAPAY ZEKA OYUN ASİSTANI", font_size='24sp', bold=True, size_hint_y=0.15))
        
        # Oyun Seçim Alanı (Spinner)
        self.add_widget(Label(text="Desteklenen Oyunlar arasından seçim yapın:", font_size='16sp', size_hint_y=0.05))
        self.oyun_secici = Spinner(
            text='İyi Pizza Güzel Pizza',
            values=('İyi Pizza Güzel Pizza', 'İyi Kahve Harika Kahve', 'Subway Surfers'),
            size_hint=(1, 0.15)
        )
        self.add_widget(self.oyun_secici)
        
        # Durum Bilgisi Skoru/Yazısı
        self.durum_etiketi = Label(text="Durum: Asistan Başlatılmadı", font_size='14sp', size_hint_y=0.15)
        self.add_widget(self.durum_etiketi)
        
        # BAŞLAT BUTONU
        self.baslat_btn = Button(text="ASİSTANI BAŞLAT", background_color=(0.1, 0.7, 0.3, 1), font_size='18sp', size_hint_y=0.2)
        self.baslat_btn.bind(on_press=self.asistani_baslat)
        self.add_widget(self.baslat_btn)
        
        # DURDUR / SON BUTONU (Uygulamayı ve Botu Kapatır)
        self.son_btn = Button(text="SON (KAPAT)", background_color=(0.9, 0.1, 0.2, 1), font_size='18sp', size_hint_y=0.2)
        self.son_btn.bind(on_press=self.uygulamayi_kapat)
        self.add_widget(self.son_btn)

    def asistani_baslat(self, instance):
        secilen_oyun = self.oyun_secici.text
        self.durum_etiketi.text = f"Durum: {secilen_oyun} Analiz Ediliyor..."
        
        # Android üzerinde arka plan servisini (service.py) tetikler
        if platform == 'android':
            from android import AndroidService
            # Buildozer.spec içindeki OyunAsistani ismiyle eşleşmeli
            service = AndroidService('Yapay Zeka Asistanı', 'OyunAsistani aktif')
            service.start('Asistan Başlatıldı')

    def uygulamayi_kapat(self, instance):
        self.durum_etiketi.text = "Durum: Asistan sonlandırılıyor..."
        
        # Önce Android arka plan servisini durduruyoruz
        if platform == 'android':
            from android import AndroidService
            service = AndroidService('Yapay Zeka Asistanı', 'OyunAsistani aktif')
            service.stop()
            
        # 1 saniye sonra uygulamayı tamamen kapatıyoruz (Sıfırlama mantığı)
        Clock.schedule_once(lambda dt: App.get_running_app().stop(), 1)

class OyunAsistaniApp(App):
    def build(self):
        return OyunAsistaniArayuz()

if __name__ == '__main__':
    OyunAsistaniApp().run()
