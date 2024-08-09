label test: 

    $ persistent.sayori_value = None
    $ persistent.natsuki_value = None
    $ persistent.yuri_value = None
    $ persistent.monika_value = None

    menu:
        "monika True":
            $ persistent.monika_value = True
        "yuri True":
            $ persistent.yuri_value = True
        "natsuki True":
            $ persistent.natsuki_value = True
        "sayori True":
            $ persistent.sayori_value = True
        "run else":
            $ persistent.sayori_value = None
            $ persistent.natsuki_value = None
            $ persistent.yuri_value = None
            $ persistent.monika_value = None
        "run fake splash":
            call fake_splash

    