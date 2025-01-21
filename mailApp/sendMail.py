import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import customtkinter as ctk
from tkinter import messagebox  

def mail_gonder():
    try:
        kullanici = sender_email.get()
        sifre = password_entry.get()  
        alicilar = recipients.get().split(",")
        mesaj_icerik = mail_body.get("1.0", "end-1c")
        konu = mail_konu.get()
      
        mesaj = MIMEMultipart()
        mesaj["From"] = kullanici
        mesaj["To"] = ", ".join(alicilar)
        mesaj["Subject"] = konu
        mesaj.attach(MIMEText(mesaj_icerik, "plain", "utf-8"))

        context = ssl.create_default_context()

        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as eposta_sunucu:
            eposta_sunucu.login(kullanici, sifre)
            eposta_sunucu.sendmail(kullanici, alicilar, mesaj.as_string())
        
        messagebox.showinfo("Başarılı", "E-postalar başarıyla gönderildi!")
    except smtplib.SMTPAuthenticationError:
        messagebox.showerror("Hata", "Kimlik doğrulama hatası! Gmail kullanıcı adı ve şifrenizi kontrol edin.")
    except Exception as e:
        messagebox.showerror("Hata", f"E-posta gönderilirken bir hata oluştu:\n{e}")


ctk.set_appearance_mode("dark")  
ctk.set_default_color_theme("blue") 

root = ctk.CTk()
root.title("E-posta Gönderme Uygulaması")
root.geometry("500x700")


ctk.CTkLabel(root, text="Gönderici E-posta:", font=("Arial", 14)).pack(pady=10)
sender_email = ctk.CTkEntry(root, width=400, font=("Arial", 14))
sender_email.pack(pady=5)

ctk.CTkLabel(root, text="Uygulama Şifresi:", font=("Arial", 14)).pack(pady=10)
password_entry = ctk.CTkEntry(root, width=400, font=("Arial", 14), show="*")  # Şifre gizli giriş
password_entry.pack(pady=5)

ctk.CTkLabel(root, text="Alıcılar (virgülle ayrılmış):", font=("Arial", 14)).pack(pady=10)
recipients = ctk.CTkEntry(root, width=400, font=("Arial", 14))
recipients.pack(pady=5)

ctk.CTkLabel(root, text="Konu:", font=("Arial", 14)).pack(pady=10)
mail_konu = ctk.CTkEntry(root, width=400, font=("Arial", 14))
mail_konu.pack(pady=5)

ctk.CTkLabel(root, text="Mesaj İçeriği:", font=("Arial", 14)).pack(pady=10)
mail_body = ctk.CTkTextbox(root, width=400, height=200, font=("Arial", 14))
mail_body.pack(pady=5)

send_button = ctk.CTkButton(root, text="Gönder", command=mail_gonder, width=200, height=50, font=("Arial", 16))
send_button.pack(pady=20)

root.mainloop()
