def createUI(app, s):
    app.title('My tool')
    width_window = 400
    height_window = 400
    screen_width = app.winfo_screenwidth()
    screen_height = app.winfo_screenheight()
    x_coordinate = (screen_width/2) - (width_window/2)
    y_coordinate = (screen_height/2) - (height_window/2)
    app.geometry('%dx%d+%d+%d' %
                 (width_window, height_window, x_coordinate, y_coordinate))
    app.minsize(400, 400)
    app.tk.eval("""
    set base_theme_dir [pwd]/awthemes-10.3.0/

    package ifneeded awthemes 10.3.0 \
      [list source [file join $base_theme_dir awthemes.tcl]]
    package ifneeded colorutils 4.8 \
      [list source [file join $base_theme_dir colorutils.tcl]]
    package ifneeded awdark 7.11 \
        [list source [file join $base_theme_dir awdark.tcl]]
    package ifneeded awlight 7.9 \
        [list source [file join $base_theme_dir awlight.tcl]]
    """)
    app.tk.call('package', 'require', 'awdark')
    s.theme_use('awdark')
    # Setting font
    s.configure('TButton', font=('Century gothic', 25, 'italic'))
    s.configure('Tools.TButton', font=('Century gothic', 35, 'italic'))

    s.map('TButton', font=[('active', ('consolas', 28, 'bold'))],
          foreground=[('active', '#f1f1c1')],
          background=[('active', '#464656')]
          )

    return app
