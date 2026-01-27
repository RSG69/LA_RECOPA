import reflex as rx

# ================================================
#   HEADER
# ================================================
def header():
    return rx.box(
        rx.hstack(
            # Altura original 80px -> 5rem
            rx.image(src="/cafeteria.png", height="5rem", class_name="logo-bar"),
            # Altura original 60px -> 3.75rem
            rx.image(src="/escudo.png", height="3.75rem", class_name="logo-escudo"),
            # Altura original 80px -> 5rem
            rx.image(src="/la_recopa.png", height="5rem", class_name="logo-recopa"),
            spacing="9", # El spacing de Reflex es una escala interna (9 ≈ 2.25rem)
            align="center",
            justify="center",
            class_name="header-logos",
        ),
        width="100%",
        # Si decides activar el height fijo, 95px -> 5.9375rem
        # height="5.9375rem",
        position="fixed",
        top="0",
        z_index="1000",
        display="flex",
        align_items="center",
        justify_content="center",
        bg="""
        linear-gradient(
          135deg,
          rgba(255,255,255,0.06),
          rgba(255,255,255,0)
        ),
        linear-gradient(
          135deg,
          #5A0F14,
          #A4161A
        )
        """,
    )

# ================================================
#   FOOTER
# ================================================
def footer():
    return rx.box(
        rx.grid(
            # Columna 1: Vacía para centrar el resto
            rx.box(),
            
            # Columna 2: Texto central (Dirección y Teléfono)
            rx.vstack(
                rx.text(
                    "Dirección: C/ Mosén Andrés Vicente, nº 27 – Zaragoza",
                    color="#333",
                    font_size=rx.breakpoints(initial="0.65rem", lg="0.85rem"),
                ),
                rx.text(
                    "Teléfono: 976 31 57 15",
                    color="#333",
                    font_size=rx.breakpoints(initial="0.65rem", lg="0.85rem"),
                ),
                spacing="2",
                align="center",
            ),
            
            # Columna 3: Logo y Copyright a la derecha
            rx.vstack(
                rx.image(
                    src="/rsg69.png", 
                    width="1.25rem", 
                    height="1.25rem", 
                    border_radius="0.2rem"
                ),
                rx.text("©Robert69", font_size="0.6rem", color="#666"),
                spacing="0",
                align="center",
                padding_right="1rem",
            ),
            columns="3",
            width="100%",
            align_items="center",
        ),
        width="100%",
        height="4rem",
        bg="white",
        border_top="1px solid #eaeaea",
        position="fixed",
        bottom="0",
        z_index="1000",
        display="flex",
        align_items="center",
    )