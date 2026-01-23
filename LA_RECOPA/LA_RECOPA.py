import json
import reflex as rx

from .layout import header, footer
from .menu_weekend import menu_weekend
from .celda import crear_celda

# ================================================
#   TEMA
# ================================================
custom_theme = rx.theme(color_scheme="orange")

# ================================================
#   LISTAS DE DATOS
# ================================================
DESAYUNOS = [
    ["Café con leche y croissant", "/desayunos/Cafe_con_leche_y_cruasan.jpg"],
    ["Café con leche y tostadas", "/desayunos/cafe_con_leche_y_tostada_con_mermelada.jpg"],
    ["Zumo natural y pan con tomate", "/desayunos/zumo_natural_y_tostada_con_tomate.jpg"],
]

ALMUERZOS = [
    ["Huevos fritos con patatas y jamón", "/almuerzos/huevos fritos con patatas y jamon.jpg"],
    ["Callos con tomate", "/almuerzos/callos.jpg"],
    ["Salchichas a la riojana", "/almuerzos/salchichas a la riojana.jpg"],
]

TAPAS = [
    ["Tortilla española", "/tortilla.jpg"],
    ["Calamares a la romana", "/calamares.jpg"],
    ["Patatas bravas", "/patatas_bravas.jpg"],
]

PLATOS = [
    ["Entrecotte a la pimienta", "/platos_2/Entrecotte a la pimienta con Patatas Fritas.jpg"],
    ["Codillo Asado", "/platos_2/Codillo Asado con Patatas Panaderas.jpg"],
    ["Salmon Fresco al Horno", "/platos_2/Salmon Fresco al Horno con Guarnicion.jpg"],
]

# ================================================
#   CUERPO (CON MARGEN Y SOPORTE DE MOVIMIENTO)
# ================================================
def cuerpo():
    return rx.vstack(
        rx.center(
            rx.box(
                
                rx.script(src="/JS/animation.js"),

                rx.grid(
                    crear_celda("DESAYUNOS", DESAYUNOS, "left", "linear-gradient(135deg,#F7971E,#FFD200)"),
                    crear_celda("ALMUERZOS", ALMUERZOS, "right", "linear-gradient(135deg,#43C6AC,#191654)"),
                    crear_celda("TAPAS", TAPAS, "left", "linear-gradient(135deg,#F7971E,#FFD200)"),
                    crear_celda("DESAYUNOS", DESAYUNOS, "left", "linear-gradient(135deg,#F7971E,#FFD200)"),
                    crear_celda("ALMUERZOS", ALMUERZOS, "right", "linear-gradient(135deg,#43C6AC,#191654)"),
                    crear_celda("TAPAS", TAPAS, "left", "linear-gradient(135deg,#F7971E,#FFD200)"),
                    crear_celda("DESAYUNOS", DESAYUNOS, "left", "linear-gradient(135deg,#F7971E,#FFD200)"),
                    crear_celda("ALMUERZOS", ALMUERZOS, "right", "linear-gradient(135deg,#43C6AC,#191654)"),
                    crear_celda("MENU FIN DE SEMANA", PLATOS, "right", "linear-gradient(135deg,#8360c3,#2ebf91)", link="/menu-weekend"),
                    
                    columns=rx.breakpoints(
                        initial="1", 
                        sm="2", 
                        lg="3",
                        xs="2",  # Esto forzará las 2 columnas en pantallas como el Fold abierto
                    ),
                    spacing="6",
                    width="100%",
                    grid_auto_rows="1fr", 
                    justify_items="center",
                    align_items="stretch", 
                ),
                width="100%",
                max_width="75rem",
                padding_x="1rem",
                margin_x="auto",
            ),
            width="100%",
        ),

        # 🔑 SOLUCIÓN MARGEN: Aumentamos el margen superior para que respire
        # initial es para móvil, lg para pantallas grandes
        margin_top=rx.breakpoints(
            initial="6.5rem",  # Más espacio en móvil para que no toque la cabecera
            lg="8.5rem"        # Espacio generoso en PC
        ),
        padding_bottom=rx.breakpoints(
            initial="15rem",  # Mucho más espacio en móvil para el texto largo
            lg="6.25rem"      # Espacio normal en PC
        ),
        width="100%",
        align="center",
    )

# ================================================
#   PÁGINA PRINCIPAL
# ================================================
def galeria():
    return rx.box(
        header(),
        cuerpo(),
        footer(),
        bg="linear-gradient(135deg, #fddac7, #f7bfa8)",
        min_height="100vh",
        width="100%",
    )

# ================================================
#   APP CONFIG
# ================================================
# 🔑 SOLUCIÓN MOVIMIENTO: Asegúrate de que el CSS esté bien vinculado
app = rx.App(
    stylesheets=[
        "/carousel.css",  # Verifica que este archivo esté en la carpeta /assets/
    ],
    theme=custom_theme
)

# RUTAS
app.add_page(galeria, route="/")
app.add_page(menu_weekend, route="/menu-weekend")