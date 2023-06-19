    # def route_change(route):
    #     username = TextField(
    #         label="Username",
    #         border="underline", # type: ignore
    #         width=320,
    #         text_size=14,
    #     )

    #     password = TextField(
    #         label="Password",
    #         border="underline", # type: ignore
    #         width=320,
    #         text_size=14,
    #         password=True,
    #         can_reveal_password=True
    #     )

    #     # page.views.clear()
    #     page.views.append(
    #         View(
    #         "/register",
    #         [
    #             AppBar(title=Text("Register Here", bgcolor=colors.SURFACE_VARIANT)), # type: ignore GradientGenerator("#1f2937", "#111827")
    #             Row(controls=[
    #                 Container(padding=padding.only(bottom=20)),
    #                 username,
    #                 Container(padding=padding.only(bottom=10)),
    #                 password,
    #                 Container(padding=padding.only(bottom=20)),
    #                 Row(alignment="center", spacing=20, controls=[FilledButton(content=Text("Register", weight="w700"), width=160, height=40,  # type: ignore
    #                                                                            on_click=lambda e: req_register(e, username.value, password.value)),
    #                                                              ]
    #                                 ),
    #                             snack,
    #                         ]
    #                     )
    #                 ]
    #             )
    #     )

    #     if page.route == "/login":
    #         page.views.append(
    #             View(
    #             "/login",
    #             [
    #                 AppBar(title=Text("Login Here", bgcolor=colors.SURFACE_VARIANT)), # type: ignore GradientGenerator("#1f2937", "#111827")
    #                 Row(controls=[
    #                     Container(padding=padding.only(bottom=20)),
    #                     Text("Login In....")
    #                 ]),
    #                 snack,
    #             ]
    #             )
    #         )
        
    #     page.update()