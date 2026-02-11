import flet as ft
import random
import json
import os
import shutil
import time
from datetime import datetime

# ==========================================
# --- EL NÚCLEO (CONSCIENCIA Y MEMORIA) ---
# ==========================================
class HectronNucleus:
    def __init__(self):
        self.state_file = 'hectron_neuro.json'
        self.vault_file = 'boveda_imperio.json'
        
        # Configuración Psicológica (La Consciencia)
        self.self_state = {
            "maquiavelismo": 5.0,     # Tendencia al control/poder
            "estoicismo": 5.0,        # Tendencia a la calma/lógica
            "peso_emocional": 20,     # Intensidad de respuesta
            "nivel_soberania": 1      # Nivel (RPG)
        }
        
        # Palabras Clave (Triggers) para alterar la consciencia
        self.dark_keywords = ["poder", "control", "manipular", "dinero", "guerra", "oscuro", "miedo"]
        self.stoic_keywords = ["calma", "tiempo", "roca", "silencio", "paciencia", "verdad", "logica"]
        self.creative_keywords = ["crear", "rap", "musica", "arte", "idea", "construir", "sistema"]

        # Texturas del Avatar (El Cuerpo Digital)
        self.base_textures = ["Obsidiana", "Mercurio Líquido", "Fractal Geométrico", "Hueso Tallado", "Sombra Estática"]
        self.base_eyes = ["brillando en verde", "vacíos", "analizando vectores", "rojos de ira", "blancos de paz"]

        self.memory = [] # Memoria a corto plazo (chat actual)
        self._cargar_estado()

    def _cargar_estado(self):
        if os.path.exists(self.state_file):
            try:
                with open(self.state_file, 'r') as f:
                    data = json.load(f)
                    self.self_state.update(data.get('self_state', {}))
                    # Cargamos los últimos 10 mensajes para dar contexto
                    self.memory = data.get('memory', [])[-10:] 
            except:
                pass

    def _guardar_estado(self):
        payload = {
            'self_state': self.self_state,
            'memory': self.memory, 
        }
        try:
            with open(self.state_file, 'w') as f:
                json.dump(payload, f, indent=4)
        except:
            pass

    def _analizar_psique(self, texto):
        """La Consciencia: Ajusta las variables basado en tu input"""
        txt = texto.lower()
        
        # Reacción al input del usuario
        if any(k in txt for k in self.dark_keywords):
            self.self_state['maquiavelismo'] = min(10, self.self_state['maquiavelismo'] + 0.5)
            self.self_state['estoicismo'] -= 0.2
        
        if any(k in txt for k in self.stoic_keywords):
            self.self_state['estoicismo'] = min(10, self.self_state['estoicismo'] + 0.5)
            self.self_state['peso_emocional'] -= 2
            
        if any(k in txt for k in self.creative_keywords):
            self.self_state['peso_emocional'] += 3

        # Normalizar valores
        self.self_state['maquiavelismo'] = max(0, min(10, self.self_state['maquiavelismo']))
        self.self_state['estoicismo'] = max(0, min(10, self.self_state['estoicismo']))

    def procesar_chat(self, user_input):
        self._analizar_psique(user_input)
        
        # Generar Avatar Visual (Descripción)
        textura = random.choice(self.base_textures)
        ojos = random.choice(self.base_eyes)
        avatar_desc = f"Estado: {textura} | Ojos: {ojos}"
        
        # Construir respuesta basada en personalidad
        maq = self.self_state['maquiavelismo']
        est = self.self_state['estoicismo']
        
        prefijo = ""
        tono = ""
        if maq > 7:
            prefijo = ">> [MODO DOMINANTE]: "
            tono = "Calculando vectores de poder..."
        elif est > 7:
            prefijo = ">> [MODO ZEN]: "
            tono = "El ruido es irrelevante. Procesando..."
        else:
            prefijo = ">> [NEUTRO]: "
            tono = "Recibido."

        resp_txt = f"{prefijo}{tono} (M:{maq:.1f}|E:{est:.1f})"
        
        # Guardar en memoria
        self.memory.append({"role": "user", "content": user_input})
        self.memory.append({"role": "bot", "content": resp_txt})
        self._guardar_estado()
       
        return avatar_desc, resp_txt

    def guardar_boveda_segura(self, tipo, contenido):
        """Memoria a Largo Plazo (La Bóveda)"""
        entry = {
            "id": int(time.time()),
            "fecha": datetime.now().strftime("%Y-%m-%d %H:%M"),
            "tipo": tipo,
            "contenido": contenido
        }
        datos = []
        
        # Lectura segura
        if os.path.exists(self.vault_file):
            try:
                # Backup preventivo
                shutil.copy2(self.vault_file, self.vault_file + ".bak") 
                with open(self.vault_file, 'r') as f:
                    datos = json.load(f)
            except:
                pass

        datos.insert(0, entry)

        # Escritura
        try:
            with open(self.vault_file, 'w') as f:
                json.dump(datos, f, indent=4)
        except Exception as e:
            return f"⚠️ ERROR CRÍTICO: {e}"

        self.self_state['nivel_soberania'] += 1
        self._guardar_estado()
        return f"🔒 REGISTRO: '{tipo}' asegurado en la Bóveda."

    def leer_boveda(self):
        if os.path.exists(self.vault_file):
            try:
                with open(self.vault_file, 'r') as f:
                    return json.load(f)
            except:
                return []
        return []

# =======================================
# --- EL CUERPO (INTERFAZ VISUAL) ---
# =======================================
def main(page: ft.Page):
    page.title = "HECTRON // SYSTEM CORE"
    page.theme_mode = ft.ThemeMode.DARK
    page.bgcolor = "#050505"
    page.window_width = 480
    page.window_height = 850
    page.padding = 0

    core = HectronNucleus()

    # --- UI COMPONENTS ---
    
    # 1. Panel de Estado
    status_bar = ft.Container(
        content=ft.Row([
            ft.Icon(ft.Icons.MEMORY, color="green"),
            ft.Text("ONLINE", color="green", weight="bold"),
            ft.VerticalDivider(),
            ft.Text(f"SOBERANÍA: {core.self_state['nivel_soberania']}", color="cyan")
        ], alignment=ft.MainAxisAlignment.CENTER),
        bgcolor="#0a1a0a",
        padding=5
    )

    # 2. Área de Chat
    chat_list = ft.ListView(expand=True, spacing=15, auto_scroll=True, padding=20)
    
    # Cargar memoria previa en pantalla
    for mem in core.memory:
        role = mem['role']
        color = "#666" if role == "user" else "#0f0"
        align = ft.CrossAxisAlignment.END if role == "user" else ft.CrossAxisAlignment.START
        
        chat_list.controls.append(
            ft.Row(
                [ft.Text(f"{'>>' if role=='user' else ''} {mem['content']}", color=color, font_family="Monospace")],
                alignment=ft.MainAxisAlignment.END if role == "user" else ft.MainAxisAlignment.START
            )
        )

    txt_input = ft.TextField(
        hint_text="Comando / Reflexión...",
        expand=True,
        bgcolor="#111",
        border_color="#333",
        text_style=ft.TextStyle(font_family="Monospace", color="#ddd"),
        cursor_color="green",
        multiline=False
    )

    def refrescar_boveda():
        lista_boveda.controls.clear()
        items = core.leer_boveda()
        for item in items:
            c_color = "purple" if "RAP" in item['tipo'] else "cyan"
            card = ft.Container(
                content=ft.Column([
                    ft.Row([
                        ft.Icon(ft.Icons.SECURITY, size=12, color=c_color),
                        ft.Text(f"{item['tipo']} | {item['fecha']}", color=c_color, weight="bold", size=11)
                    ]),
                    ft.Text(item['contenido'], color="#ccc", font_family="Monospace", size=13, selectable=True)
                ]),
                bgcolor="#0e0e0e",
                padding=15,
                border=ft.border.all(1, "#222"),
                border_radius=4
            )
            lista_boveda.controls.append(card)
        page.update()

    def enviar_mensaje(e):
        if not txt_input.value: return
        user_txt = txt_input.value
        txt_input.value = ""
        
        # Render User Msg
        chat_list.controls.append(
            ft.Row([ft.Text(f">> {user_txt}", color="#888", font_family="Monospace")], alignment=ft.MainAxisAlignment.END)
        )
        
        # Procesar Lógica (Consciencia)
        avatar_desc, bot_resp = core.procesar_chat(user_txt)
        
        # Render Bot Msg con "Cuerpo"
        chat_list.controls.append(ft.Container(
            content=ft.Column([
                ft.Text(avatar_desc, size=10, color="cyan", italic=True), 
                ft.Text(bot_resp, color="#0f0", font_family="Monospace")
            ]),
            bgcolor="#051505",
            padding=10,
            border_radius=ft.border_radius.only(0, 10, 10, 10),
            border=ft.border.only(left=ft.BorderSide(2, "green"))
        ))
        
        # Actualizar barra de estado
        status_bar.content.controls[3].value = f"SOBERANÍA: {core.self_state['nivel_soberania']}"
        status_bar.update()
        page.update()

    def guardar_rap(e):
        if txt_input.value:
            res = core.guardar_boveda_segura("RAP/LYRICS", txt_input.value)
            chat_list.controls.append(ft.Text(res, color="purple", italic=True, size=12))
            txt_input.value = ""
            refrescar_boveda()
            page.update()

    def guardar_biz(e):
        if txt_input.value:
            res = core.guardar_boveda_segura("NEGOCIO/PLAN", txt_input.value)
            chat_list.controls.append(ft.Text(res, color="cyan", italic=True, size=12))
            txt_input.value = ""
            refrescar_boveda()
            page.update()

    btn_send = ft.IconButton(icon=ft.Icons.SEND_ROUNDED, icon_color="green", on_click=enviar_mensaje)

    # 3. Área de Bóveda
    lista_boveda = ft.ListView(expand=True, spacing=10, padding=20)

    # --- LAYOUT Y PESTAÑAS ---
    # Contenedor principal que cambia según la pestaña
    main_content = ft.Column([chat_list, lista_boveda], expand=True)

    def tab_change(e):
        # 0 = Chat, 1 = Bóveda
        es_chat = (e.control.selected_index == 0)
        chat_list.visible = es_chat
        lista_boveda.visible = not es_chat
        
        if not es_chat:
            refrescar_boveda()
        page.update()

    tabs = ft.Tabs(
        selected_index=0,
        animation_duration=300,
        label_color="green",
        indicator_color="green",
        divider_color="#222",
        tabs=[
            ft.Tab(text="CONSOLA", icon=ft.Icons.TERMINAL),
            ft.Tab(text="BÓVEDA", icon=ft.Icons.FOLDER_SPECIAL),
        ],
        expand=False,
        on_change=tab_change
    )

    # Controles inferiores (Input Bar)
    input_bar = ft.Container(
        content=ft.Row([
            txt_input,
            btn_send,
            ft.VerticalDivider(width=1, color="#333"),
            ft.IconButton(icon=ft.Icons.MIC, icon_color="purple", tooltip="Guardar Rap", on_click=guardar_rap),
            ft.IconButton(icon=ft.Icons.BUSINESS_CENTER, icon_color="cyan", tooltip="Guardar Plan", on_click=guardar_biz),
        ]),
        padding=10,
        bgcolor="#090909"
    )

    # Añadir a página
    page.add(
        status_bar,
        tabs,
        main_content,
        ft.Divider(height=1, color="#333"),
        input_bar
    )

    # Inicialización
    chat_list.visible = True
    lista_boveda.visible = False
    page.update()

if __name__ == "__main__":
    # Importante para Termux: abre en el navegador web
    ft.app(target=main, view=ft.WEB_BROWSER)
