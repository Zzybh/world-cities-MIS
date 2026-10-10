"""
Home.py - main entry for the Streamlit multipage app.

This file shows a title, welcome text, and a button that attempts to navigate
to the multipage "App" (app.py) by setting Streamlit's page query parameter.
"""

import streamlit as st


def main():
    st.set_page_config(page_title="World Cities MIS — Home", page_icon="🌍")

    st.title("World Cities MIS")
    st.subheader("Welcome")
    st.write(
        "Welcome to the World Cities Management Information System. "
        "Use the button below to open the app page, or select 'App' from the "
        "Pages menu on the left."
    )

    if st.button("Go to App"):
        # Try to navigate to the 'App' page in Streamlit's multipage app.
        # Streamlit's multipage navigation listens to the `page` query param,
        # so we set it and then rerun the app. The visible page title is usually
        # the capitalized filename (e.g., 'App' for pages/app.py).
        st.experimental_set_query_params(page="App")
        st.experimental_rerun()

    st.write("---")
    st.info(
        "If the button doesn't navigate, open the 'App' page from the left-hand "
        "Pages menu (or run the pages/app.py directly)."
    )


if __name__ == "__main__":
    main()
