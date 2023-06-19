import flet as ft
from flet import (
    AppBar,
    ElevatedButton,
    Page,
    Text,
    View,
    colors,
    Column,
    Container,
    LinearGradient,
    alignment,
    border_radius,
    padding,
    Image,
    UserControl,
    Row,
    IconButton,
    margin,
    Card,
    TextField,
    FilledButton,
    SnackBar
)
import requests

def main(page: ft.Page):
    page.title = "Routes Example"
    page.add(Text("Welcome"))
    snack = SnackBar(
        Text("Registration successful")
    )
    
    
    def req_register(e, username, password):
        data = {
            "username": username,
            "password": password,
        }
        response = requests.post("http://127.0.0.1:8000/register", json=data)

        if response.status_code == 201:
            snack.open = True
            page.update()
        elif response.status_code == 400:
            snack.content.value = "User already exists!" # type: ignore
            snack.open = True
            page.update()
        else:
            snack.content.value = "You were not registered" # type: ignore
            snack.open = True
            page.update()
    
    def route_change(route):
        username = TextField(
            label="Username",
            border="underline", # type: ignore
            width=320,
            text_size=14,
        )

        password = TextField(
            label="Password",
            border="underline", # type: ignore
            width=320,
            text_size=14,
            password=True,
            can_reveal_password=True
        )

        page.views.clear()
        page.views.append(
            ft.View(
                "/register",
                [
                    ft.AppBar(title=ft.Text("Register here"), bgcolor=ft.colors.SURFACE_VARIANT),
                    username,
                    password,
                    ft.Row([
                        ft.ElevatedButton("Register", on_click=lambda e: req_register(e, username.value, password.value)),
                        ft.FilledButton("Already registered?", on_click=lambda _: page.go("/login"))
                    ]),
                    
                    snack,
                ],
            )
        )
        if page.route == "/login":
            page.views.append(
                ft.View(
                    "/login",
                    [
                        ft.AppBar(title=ft.Text("Login Here"), bgcolor=ft.colors.SURFACE_VARIANT),
                        username,
                        password,
                        ft.FilledButton("Login", on_click=lambda _: page.go("/home"))
                        # ft.ElevatedButton("Go Home", on_click=lambda _: page.go("/")),
                    ],
                )
            )
        page.update()


    def view_pop(view):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route)

ft.app(target=main, view=ft.WEB_BROWSER)









