label monika:
    jump end_easteregg

label gelistirici:
    dev "Evet bu modu oynadın."
    dev "Bu easteregg'i ya kaynak kodundan buldun yada başka bir şekilde buldun."
    dev "Burası benim ile binevi sohbet edebileceğin bir yer."
    dev "Sadece metin yazdım.{w=1} Ne kadar{w=1} sohbet denebilirse."
    dev "Bu modu github'dan indirdin. new-green yazarak githubdan modun kaynak kodlarına bakabilirsin."
    dev "Discorddan 'new_green' olarak bana yazabilirsin veya discord'da DokiTale veya ValleySoftware sunucularından ulaşabilirsin."
    dev "Eğer gelecekte bu mod tutarsa çok çok iyi olur."
    dev "Sende bu modu oynamış olursun. Ne güzel."
    dev "Mükemmel! Herkes kazançlı."
    menu:
        dev "İstersen seni herhangi bir bölüme atabilirim."
        "Oyunun başı":
            dev "Tamamdır."
            jump story_ch1
        "Sayori ile beraberlik":
            dev "Tamamdır."
            jump story_sayori
        "Yuri ile beraberkik":
            dev "Tamamdır."
            jump story_yuri
        "Natsuki ile beraberlik":
            dev "Tamamdır."
            jump story_natsuki
        "Monika ile beraberlik":
            dev "Tamamdır."
            jump story_monika
        "Easteregg 1":
            dev "Tamamdır."
            jump sayori
        "Easteregg 2":
            dev "Tamamdır."
            jump monika
        "Easteregg 3":
            dev "Tamamdır."
            jump natsuki
        "Easteregg 4":
            dev "Tamamdır."
            jump yuri
        "Oyundan çık.":
            dev "Tamamdır."
            $ renpy.quit()


