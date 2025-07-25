
from tkinter import *
from tkinter import messagebox, ttk
import tkinter.font as tkFont
from DataBase import Database

class LoginSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("VGM Systems - Painel de Acesso")
        self.root.geometry("500x400")
        self.root.configure(background="#002333")
        self.root.resizable(False, False)
        
        # Centralizar janela
        self.center_window()
        
        # Configuração de fontes
        self.title_font = tkFont.Font(family="Helvetica", size=24, weight="bold")
        self.label_font = tkFont.Font(family="Helvetica", size=12)
        self.button_font = tkFont.Font(family="Helvetica", size=12, weight="bold")
        
        # Frame principal
        self.main_frame = Frame(self.root, bg="#002333")
        self.main_frame.pack(fill=BOTH, expand=True, padx=40, pady=40)
        
        # Logo/Cabeçalho
        self.header = Frame(self.main_frame, bg="#002333")
        self.header.pack(fill=X, pady=(0, 30))
        
        self.title_label = Label(self.header, text="VGM Systems", 
                               font=self.title_font, bg="#002333", fg="white")
        self.title_label.pack()
        
        self.subtitle_label = Label(self.header, text="Painel de Acesso", 
                                  font=self.label_font, bg="#002333", fg="#a0a0a0")
        self.subtitle_label.pack()
        
        # Formulário de login
        self.form_frame = Frame(self.main_frame, bg="#002333")
        self.form_frame.pack(fill=X)
        
        # Campo Usuário
        self.user_frame = Frame(self.form_frame, bg="#002333")
        self.user_frame.pack(fill=X, pady=10)
        
        self.user_label = Label(self.user_frame, text="Usuário", 
                              font=self.label_font, bg="#002333", fg="white")
        self.user_label.pack(anchor=W)
        
        self.LoginEntry = ttk.Entry(self.user_frame, font=self.label_font, width=25)
        self.LoginEntry.pack(fill=X, ipady=5)
        
        # Campo Senha
        self.pass_frame = Frame(self.form_frame, bg="#002333")
        self.pass_frame.pack(fill=X, pady=10)
        
        self.pass_label = Label(self.pass_frame, text="Senha", 
                              font=self.label_font, bg="#002333", fg="white")
        self.pass_label.pack(anchor=W)
        
        self.pass_entry = ttk.Entry(self.pass_frame, font=self.label_font, 
                                   width=25, show="•")
        self.pass_entry.pack(fill=X, ipady=5)
        
        # Botão de Login
        self.button_frame = Frame(self.main_frame, bg="#002333")
        self.button_frame.pack(fill=X, pady=(20, 0))
        
        self.login_button = Button(self.button_frame, text="ENTRAR", 
                                 font=self.button_font, bg="#0078D7", fg="white",
                                 activebackground="#0063B1", activeforeground="white",
                                 borderwidth=0, padx=20, pady=10,
                                 command=self.FazerLogin)
        self.login_button.pack(fill=X)
        
        # Rodapé
        self.footer = Frame(self.main_frame, bg="#002333")
        self.footer.pack(fill=X, pady=(20, 0))
        
        self.version_label = Label(self.footer, text="v1.0.0", 
                                 font=("Helvetica", 8), bg="#002333", fg="#a0a0a0")
        self.version_label.pack(side=RIGHT)
    
    def center_window(self):
        self.root.update_idletasks()
        width = self.root.winfo_width()
        height = self.root.winfo_height()
        x = (self.root.winfo_screenwidth() // 2) - (width // 2)
        y = (self.root.winfo_screenheight() // 2) - (height // 2)
        self.root.geometry(f'{width}x{height}+{x}+{y}')
    
    def FazerLogin(self):
        usuario = self.LoginEntry.get()
        senha = self.pass_entry.get()

        try:
            db = Database()

            # Verifica na tabela 'adm'
            db.cursor.execute("SELECT * FROM adm WHERE usuario = %s AND senha = %s", (usuario, senha))
            verify_adm = db.cursor.fetchone()

            if verify_adm:
                messagebox.showinfo(title="INFO LOGIN", message="Acesso Confirmado, Bem-vindo administrador!")
                from tela_ADM import TeldACASTRO
                self.root.destroy()  # Fecha a tela atual, se estiver dentro de uma classe
                root_menu = Tk()
                TeldACASTRO(root_menu)
                root_menu.mainloop()
                return

            # Se não for admin, verifica na tabela 'usuario'
            db.cursor.execute("SELECT * FROM usuario WHERE usuario = %s AND senha = %s", (usuario, senha))
            verify_user = db.cursor.fetchone()

            if verify_user:
                messagebox.showinfo(title="INFO LOGIN", message="Acesso Confirmado, Bem-vindo usuário!")
                from tela_de_usuario import TeldACASTRO  # Corrigido o nome
                self.root.destroy()
                root_menu = Tk()
                TeldACASTRO(root_menu)
                root_menu.mainloop()
            else:
                messagebox.showinfo(title="INFO LOGIN", message="Acesso Negado. Verifique se está cadastrado no sistema!")

        except Exception as e:
            messagebox.showerror(title="Erro", message=f"Ocorreu um erro: {str(e)}")



if __name__ == "__main__":
    root = Tk()
    app = LoginSystem(root)
    root.mainloop()
