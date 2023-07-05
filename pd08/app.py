from shiny import ui, App

# Interface do usuário ----
app_ui = ui.page_navbar()

# Servidor ----
def server(input, output, session):
    ...


# Dashboard Shiny App
app= App(app_ui, server)