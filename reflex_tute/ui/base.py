import reflex as rx
from .nav import navbar

def base_page(child: rx.Component, *args) -> rx.Component:
    return rx.fragment(
        navbar(),
        rx.box(
          child,
          padding="1em",
          width="100%",
          id="my-content-area-el"
        ),
        rx.logo(),
        rx.color_mode.button(position="bottom-left"),
        id="my-base-container"
    )
