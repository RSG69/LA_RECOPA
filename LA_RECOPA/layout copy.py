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
        rx.hstack(
            # Espacio lateral 120px -> 7.5rem
            rx.box(width="7.5rem"),
            rx.text(
                "Direccion: C/ Mosen Andres Vicente , nº 27 - Zaragoza - Telefono: 976 31 57 15",
                class_name="footer-text",
                width="100%",
                text_align="center",
                # Tamaño de fuente estándar 16px -> 1rem
                font_size="1rem",
            ),
            rx.vstack(
                # Icono 28px -> 1.75rem
                rx.image(
                    src="/rsg69.png", 
                    width="1.75rem", 
                    height="1.75rem", 
                    border_radius="0.375rem" # 6px -> 0.375rem
                ),
                # Texto pequeño 12px -> 0.75rem
                rx.text("©Robert69", font_size="0.75rem", color="#555"),
                spacing="0",
                align="center",
                # Margen derecho 20px -> 1.25rem
                padding_right="1.25rem",
            ),
            width="100%",
            align="center",
            justify="between",
        ),
        width="100%",
        # Altura del footer 90px -> 5.625rem
        #height="5.625rem",
        #hago mas mas pequeño (alto) el footer
        height="3rem",
        bg="white",
        border_top="0.0625rem solid #eaeaea", # 1px -> 0.0625rem
        display="flex",
        align_items="center",
        position="fixed",
        bottom="0",
        z_index="1000",
    )