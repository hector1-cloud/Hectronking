import flet as ft
import random
import json
import os
from datetime import datetime

# --- EL CEREBRO (SISTEMA HÍBRIDO) ---
class HectronBaphomet:
    def __init__(self):
        self.state_file = 'hectron_state.json'
        self.vault_file = 'boveda_imperio.json' # <--- AQUÍ ESTÁ LA CLAVE QUE FALTABA
        # Estado Psicológico
        self.self_state = {
            "maquiavelismo": 4.5,
            "estoicismo": 4.8,
            "peso_emocional": 20,
            "nivel_soberania": 1
        }
        self._cargar_memoria()

    def _cargar_memoria(self):
        if os.path.exists(self.state_file):
            try:
                with open(self.state_file, 'r') as f:
                    data = json.load(f)
                    if 'self_state' in data:
                        self.self_state.update(data['self_state'])
            except:
                pass

    def guardar_boveda(self, tipo, contenido):
        """Guarda en el Grimorio"""
        entry = {
            "fecha": datetime.now().strftime("%Y-%m-%d %H:%M"),
            "tipo": tipo,
            "contenido": contenido
        }
        datos = []
        if os.path.exists(self.vault_file):
            try:
                with open(self.vault_file, 'r') as f:
                    datos = json.load(f)
            except:
                pass
        datos.insert(0, entry)
        with open(self.vault_file, 'w') as f:
            json.dump(datos, f, indent=4)
        self.self_state['nivel_soberania'] += 1
        self._guardar_estado()
        return f"🔒 [BÓVEDA]: '{tipo}' guardado correctamente."

    def leer_boveda(self):
        if os.path.exists(self.vault_file):
            try:
                with open(self.vault_file, 'r') as f:
                    return json.load(f)
            except:
                return []
        return []

    def _guardar_estado(self):
        try:
            with open(self.state_file, 'w') as f:
                json.dump({'self_state': self.self_state}, f)
        except:
            pass

    def procesar(self, texto):
        return f"[HÉCTRON]: Recibido. Estructura estable.\n>> SOBERANÍA: Nvl {self.self_state['nivel_soberania']}"

# --- EL CUERPO (INTERFAZ) ---
def main(page: ft.Page):
    page.title = "BAPHOMET.ai // LOCAL SYSTEM"
    page.theme_mode = ft.ThemeMode.DARK
    page.bgcolor = "#050505"
    page.window_width = 450
    page.window_height = 850
    page.padding = 0

    sistema = HectronBaphomet()

    # --- PESTAÑA 1: COMANDO ---
    chat_list = ft.ListView(expand=True, spacing=10, auto_scroll=True, padding=20)
    inp = ft.TextField(
        hint_text="Comando...",
        expand=True,
        bgcolor="#1a1a1a",
        border_color="#333",
        text_style=ft.TextStyle(font_family="Courier New")
    )
    def enviar(e):
        if not inp.value:
            return
        txt = inp.value
        inp.value = ""
        chat_list.controls.append(ft.Text(f"> {txt}", color="#888", font_family="Courier New"))
        resp = sistema.procesar(txt)
        chat_list.controls.append(ft.Container(
            content=ft.Text(resp, color="#0f0", font_family="Courier New"),
            bgcolor="#051105",
            padding=10,
            border_radius=5
        ))
        page.update()

    btn_send = ft.IconButton(icon=ft.Icons.TERMINAL, icon_color="green", on_click=enviar)

    # --- PESTAÑA 2: BÓVEDA ---
    lista_boveda = ft.ListView(expand=True, spacing=10, padding=20)

    def refrescar_boveda():
        lista_boveda.controls.clear()
        items = sistema.leer_boveda()
        for item in items:
            color = "cyan" if item['tipo'] == "NEGOCIO" else "purple"
            card = ft.Container(
                content=ft.Column([
                    ft.Text(f"{item['tipo']} // {item['fecha']}", color=color, weight="bold", size=12),
                    ft.Text(item['contenido'], color="#ddd", font_family="Courier New")
                ]),
                bgcolor="#111",
                padding=15,
                border=ft.border.all(1, "#333"),
                border_radius=5
            )
            lista_boveda.controls.append(card)
        page.update()

    def guardar_rap(e):
        if inp.value:
            res = sistema.guardar_boveda("RAP/MAGIA", inp.value)
            chat_list.controls.append(ft.Text(res, color="purple", italic=True))
            inp.value = ""
            refrescar_boveda() # Refresh vault list after saving
            page.update()
    
    # --- The inferred function to complete the code ---
    def guardar_biz(e):
        if inp.value:
            res = sistema.guardar_boveda("NEGOCIO/PLAN", inp.value) # Typo in user code was "NEGOCIO", using that
            chat_list.controls.append(ft.Text(res, color="cyan", italic=True))
            inp.value = ""
            refrescar_boveda() # Refresh vault list after saving
            page.update()
    # --------------------------------------------------

    # --- PESTAÑAS (TABS) ---
    tabs = ft.Tabs(
        selected_index=0,
        animation_duration=300,
        label_color="green",
        unselected_label_color="gray",
        indicator_color="green",
        on_change=lambda e: refrescar_boveda() if e.control.selected_index == 1 else None,
        tabs=[
            ft.Tab(text="Consola", icon=ft.Icons.TERMINAL),
            ft.Tab(text="Bóveda", icon=ft.Icons.LOCK),
        ],
        expand=1
    )

    page.add(
        tabs,
        ft.Column(
            controls=[chat_list, lista_boveda],
            expand=True,
            # Initially only show chat_list by controlling visibility
            visible=tabs.selected_index == 0 
        ),
        ft.Row(
            controls=[
                inp,
                btn_send,
                ft.IconButton(icon=ft.Icons.MIC_EXTERNAL_ON, icon_color="purple", on_click=guardar_rap),
                ft.IconButton(icon=ft.Icons.BUSINESS_CENTER, icon_color="cyan", on_click=guardar_biz),
            ],
            padding=10
        )
    )

    # Functionality to switch views when tabs change
    def tab_change_handler(e):
        chat_list.visible = e.control.selected_index == 0
        lista_boveda.visible = e.control.selected_index == 1
        if e.control.selected_index == 1:
            refrescar_boveda()
        page.update()
    
    tabs.on_change = tab_change_handler

    # Initial update to set correct visibility and load initial vault data
    refrescar_boveda()
    chat_list.visible = True
    lista_boveda.visible = False
    page.update()

# Run the application
if __name__ == "__main__":
    ft.app()
