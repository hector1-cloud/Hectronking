import flet as ft
import time

def main(page: ft.Page):
    # --- CONFIGURACIÓN DE VENTANA (PC) ---
    page.title = "Hectron - Baphomet.ai"
    page.window_width = 450        # Ancho tipo móvil/panel
    page.window_height = 800       # Alto
    page.window_resizable = True   # Permitir redimensionar
    page.theme_mode = ft.ThemeMode.DARK
    page.bgcolor = ft.colors.BLACK
    page.vertical_alignment = ft.MainAxisAlignment.END
    
    # Tema Rojo/Negro
    page.theme = ft.Theme(
        color_scheme=ft.ColorScheme(
            primary=ft.colors.RED_600,
            primary_container=ft.colors.RED_900,
            background=ft.colors.BLACK,
            surface=ft.colors.GREY_900,
        )
    )

    # --- UI ---
    
    # Cabecera
    header = ft.Container(
        content=ft.Row(
            [
                ft.Icon(ft.icons.SECURITY_ROUNDED, color=ft.colors.RED_500, size=24),
                ft.Text("HECTRON SYSTEM", size=18, weight="bold", color=ft.colors.RED_500),
            ],
            alignment=ft.MainAxisAlignment.CENTER
        ),
        padding=15,
        bgcolor=ft.colors.GREY_900,
        border_radius=ft.border_radius.only(bottom_left=15, bottom_right=15)
    )

    # Área de Chat
    chat_list = ft.ListView(
        expand=True,
        spacing=12,
        padding=20,
        auto_scroll=True,
    )

    def send_message(e):
        text = user_input.value.strip()
        if not text:
            return

        # Mensaje Usuario
        chat_list.controls.append(
            ft.Row(
                [
                    ft.Container(
                        content=ft.Text(f"User: {text}", color=ft.colors.WHITE),
                        padding=12,
                        border_radius=12,
                        bgcolor=ft.colors.BLUE_GREY_900,
                    )
                ],
                alignment=ft.MainAxisAlignment.END
            )
        )
        user_input.value = ""
        page.update()

        # Simulación
        time.sleep(0.3)

        # Respuesta Baphomet
        chat_list.controls.append(
            ft.Row(
                [
                    ft.Container(
                        content=ft.Column([
                            ft.Text("Baphomet", size=11, color=ft.colors.RED_400, weight="bold"),
                            ft.Text(f"Procesando: {text} ... [OK]", color=ft.colors.RED_50),
                        ]),
                        padding=12,
                        border_radius=12,
                        bgcolor=ft.colors.RED_900,
                        width=300
                    )
                ],
                alignment=ft.MainAxisAlignment.START
            )
        )
        page.update()

    # Input
    user_input = ft.TextField(
        hint_text="Escribir comando...",
        border_color=ft.colors.RED_800,
        bgcolor=ft.colors.GREY_900,
        color=ft.colors.WHITE,
        expand=True,
        on_submit=send_message,
        border_radius=10
    )

    send_btn = ft.IconButton(
        icon=ft.icons.ARROW_FORWARD_IOS_ROUNDED,
        icon_color=ft.colors.RED_500,
        on_click=send_message
    )

    # Layout
    page.add(
        header,
        chat_list,
        ft.Container(
            content=ft.Row([user_input, send_btn]),
            padding=10
        )
    )

# EJECUCIÓN ESTÁNDAR PARA PC
ft.app(target=main)
