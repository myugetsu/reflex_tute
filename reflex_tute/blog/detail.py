import reflex as rx
from ..ui.base import base_page
from . import state

def blog_post_detail_page() -> rx.Component:
    # Welcome Page (Index)
    my_child = rx.vstack(
            rx.heading(state.BlogPostState.post.title, size="9"),
            rx.text(
                state.BlogPostState.post.content
            ),
            spacing="5",
            align="center",
            text_align="center",
            min_height="85vh"
        )
    return base_page(my_child)
