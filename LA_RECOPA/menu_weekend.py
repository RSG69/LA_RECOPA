import reflex as rx
from .layout import header, footer
from .layout import aniversario_flotante
from .celda import crear_celda

# =================================================
#   DATOS
# =================================================
PLATOS_1 = [
    ["Tomate Rosa con Bonito del Norte y Cebolla", "/platos_1/Tomate Rosa con Bonito del Norte y cebolla.jpg"],
    ["Tallarines a la Bolonesa", "/platos_1/Tallarines a la Bolonesa.jpg"],
    ["Verduritas a la plancha con Salsa Romescu", "/platos_1/Verduritas a la plancha con Salsa Romescu.jpg"],
    ["Tosta Gratinada con Setas, Brie y Jamon", "/platos_1/Tosta Gratinada con Setas, Brie y Jamon.jpg"],
]

PLATOS_2 = [
    ["Entrecotte a la pimienta con Patatas Fritas", "/platos_2/Entrecotte a la pimienta con Patatas Fritas.jpg"],
    ["Codillo Asado con Patatas Panaderas", "/platos_2/Codillo Asado con Patatas Panaderas.jpg"],
    ["Lomo Relleno de Bacon y Cammembert", "/platos_2/Lomo Relleno de Bacon y Cammembert.jpg"],
    ["Salmon Fresco al Horno con Guarnicion", "/platos_2/Salmon Fresco al Horno con Guarnicion.jpg"],
]

POSTRES = [
    ["Tarta al Whisky", "/postres/Tarta al Whisky.jpg"],
    ["Tarta de Queso Casero", "/postres/Tarta de Queso Casero.jpg"],
    ["Postre Navideño Especial", "/postres/Postre Navideño Especial.jpg"],
]

BEBIDA_Y_PAN  = [
    ["Vino '3404' D. O. Somomtano, Agua y Pan", "/Vino Agua y Pan.png"],

]

TITULO = "Menú Fin De Semana - 20 y 21 de Diciembre"

# =================================================
#   PÁGINA
# =================================================
def menu_weekend():
    return rx.box(
        header(),
        aniversario_flotante(),
        rx.box(
            rx.text("PRECIO"),
        ),
        rx.vstack(
            rx.heading(
                TITULO,
                size=rx.breakpoints(initial="7", sm="7", md="8", lg="9"),
                color="#5A0F14",
                text_align="center",
                width="100%",
                padding_x="1.5rem",
                #margin_top=rx.breakpoints(initial="1rem", sm="4.5rem", lg="2.5rem"),
                margin_bottom=rx.breakpoints(initial="1rem", sm="2rem", lg="3rem"),
            ),
            rx.center(
                rx.box(
                    rx.grid(
                        crear_celda("Primer Plato", PLATOS_1, "right", "linear-gradient(135deg,#8360c3,#2ebf91)"),
                        crear_celda("Segundo Plato", PLATOS_2, "right", "linear-gradient(135deg,#8360c3,#2ebf91)"),
                        crear_celda("Postres", POSTRES, "right", "linear-gradient(135deg,#F7971E,#FFD200)"),
                        crear_celda("Bebida y Pan", BEBIDA_Y_PAN, None, "linear-gradient(135deg,#43C6AC,#191654)"),
                      
                        # 🔑 CONFIGURACIÓN RESPONSIVA
                        columns=rx.breakpoints(
                            initial="1", # Móvil
                            sm="2",      # Z Fold abierto / Tablet
                            xs="2",  # Esto forzará las 2 columnas en pantallas como el Fold abierto
                        ),
                        spacing="6",
                        width="100%",
                        # 🔑 LAS DOS CLAVES PARA ALTURAS IGUALES:
                        grid_auto_rows="1fr", 
                        align_items="stretch",
                        justify_items="center",
                    ),
                    rx.hstack(
                        rx.text(
                            "PRECIO: 21€",
                            font_weight="bold",
                            color="blue",
                            font_size="2em",
                            #text_align="center"
                            margin_top="3rem",
                            bg="white",
                        ),
                        rx.spacer(),
                        rx.text(
                            "TAMBIEN PARA LLEVAR",
                            font_weight="bold",
                            color="blue",
                            font_size="2em",
                            margin_top="3rem",
                            bg="white",
                        ),
                    ),
                    width="100%",
                    max_width="68.75rem", # 1100px
                    padding_x="1rem",
                    margin_x="auto",
                ),
                width="100%",
            ),
            
            spacing="0",
            # Margen superior para no chocar con el header fijo
            margin_top=rx.breakpoints(initial="4rem", lg="8.5rem"),
            padding_bottom="6.25rem",
            width="100%",
            align="center",
        ),
        footer(),
        bg="linear-gradient(135deg, #fddac7, #f7bfa8)",
        min_height="100vh",
    )