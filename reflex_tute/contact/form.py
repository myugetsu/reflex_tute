import reflex as rx
from .state import ContactState

def contact_form() -> rx.Component:
    return rx.form(
                rx.vstack(
                    rx.hstack(
                      rx.input(
                          name="first_name",
                          placeholder="First Name",
                          type="text",
                          required=True,
                          width="100%"
                      ),
                      rx.input(
                          name="last_name",
                          placeholder="Last Name",
                          type="text",
                          required=True,
                          width="100%"
                      ),
                      width="100%"
                    ),
                    rx.input(
                        name="email",
                        placeholder="Email",
                        type="email",
                        required=True,
                        width="100%"
                    ),
                    rx.text_area(
                      name="message",
                      placeholder="your message",
                      required=True,
                      width="100%"
                    ),
                    rx.button("Submit", type="submit"),
                ),
                on_submit=ContactState.handle_submit,
                reset_on_submit=True,
            )
