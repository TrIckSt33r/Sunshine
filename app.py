
from flask import Flask, render_template

app = Flask(__name__)

app.config["ENV"] = "production"
app.config["DEBUG"] = False



 
menu_antipasti_speciali = [
    {
        "name": "Tris di Mini Buns",
        "desc": [
            "gambero rosso di cetara, stracciata di bufala",
            "baccala e friarielli",
            "spigola, friarielli, maionese e insalata"
        ],
        "price": 13.00
    },
    {
        "name": "Julienne di calamari",
        "desc": "con pane croccante e insalatina del campo",
        "price": 16.00
    },
    {
        "name": "Calamaro croccante",
        "desc": "con ripieno di ricotta, salame e mozzarella",
        "price": 16.00
    },
    {
        "name": "Saute’ di lupini",
        "desc": "con provolone del monaco e tarallo sbriciolato",
        "price": 15.00
    },
    {
        "name": "Poker di gamberoni",
        "desc": "con maionese agli agrumi",
        "price": 16.00
    },
    {
        "name": "Antipasto dello chef",
        "desc": None,
        "price": 18.00
    },
    {
        "name": "Chips di spigola",
        "desc": "con ricotta a limone e spinacino croccante",
        "price": 15.00
    }
]

menu_crudi_ostriche = [
    {
        "name": "Gillardeau",
        "desc": None,
        "price": 5.00,
        "unit": "cad."
    },
    {
        "name": "David Herve'",
        "desc": None,
        "price": 4.00,
        "unit": "cad."
    },
    {
        "name": "Ostriche Locali",
        "desc": None,
        "price": 3.00,
        "unit": "cad."
    },
    {
        "name": "Tartufi di Mare",
        "desc": None,
        "price": 60.00,
        "unit": "al kg."
    },
    {
        "name": "Tartare di gambero rosso di cetara",
        "desc": None,
        "price": 18.00
    },
    {
        "name": "Tartare di tonno",
        "desc": None,
        "price": 15.00
    },
    {
        "name": "Tartare di salmone",
        "desc": None,
        "price": 15.00
    }
]

menu_crostacei = [
    {
        "name": "Astice blu",
        "desc": None,
        "price": 100.00
    },
    {
        "name": "Astice canada",
        "desc": None,
        "price": 60.00
    },
    {
        "name": "Aragosta",
        "desc": None,
        "price": 140.00
    },
    {
        "name": "Cicala",
        "desc": None,
        "price": 140.00
    },
    {
        "name": "Scampi reali norvegia",
        "desc": None,
        "price": 110.00
    },
    {
        "name": "Scampi sicilia",
        "desc": None,
        "price": 90.00
    },
    {
        "name": "Gamberoni di cetara",
        "desc": None,
        "price": 90.00
    }
]

antipasti_freddi = [
    {
        "name": "Insalata di mare",
        "desc": None,
        "price": 14.00
    },
    {
        "name": "Polpo all'insalata",
        "desc": None,
        "price": 12.00
    },
    {
        "name": "Marinato misto",
        "desc": None,
        "price": 13.00
    },
    {
        "name": "Cocktail di gambero",
        "desc": None,
        "price": 10.00
    },
]


antipasti_caldi = [
    {
        "name": "Sautè di vongole",
        "desc": None,
        "price": 15.00
    },
    {
        "name": "Sautè di frutti di mare",
        "desc": None,
        "price": 13.00
    },
    {
        "name": "Sautè di cozze",
        "desc": None,
        "price": 10.00
    },
    {
        "name": "Impepata di cozze",
        "desc": None,
        "price": 10.00
    },
    {
        "name": "Polipetti alla luciana",
        "desc": None,
        "price": 15.00
    },
    {
        "name": "Baccala alla luciana",
        "desc": None,
        "price": 15.00
    },
    {
        "name": "Baccala e friarelli",
        "desc": None,
        "price": 13.00
    },
    {
        "name": "Polpo croccante",
        "desc": "con rucola, pomodorini e glass di aceto balsamico",
        "price": 15.00
    }
]


pescato_del_giorno = [
    {
        "name": "Spigola",
        "desc": None,
        "price": 50.00
    },
    {
        "name": "Orata",
        "desc": None,
        "price": 50.00
    },
    {
        "name": "Dentice",
        "desc": None,
        "price": 60.00
    },
    {
        "name": "Pescatrice",
        "desc": None,
        "price": 50.00
    },
    {
        "name": "Scorfano",
        "desc": None,
        "price": 60.00
    },
    {
        "name": "Cocchio",
        "desc": None,
        "price": 60.00
    },
    {
        "name": "San Pietro",
        "desc": None,
        "price": 60.00
    },
    {
        "name": "Triglia",
        "desc": None,
        "price": 50.00
    },
    {
        "name": "Pezzogna",
        "desc": None,
        "price": 70.00
    },
    {
        "name": "Ricciola",
        "desc": None,
        "price": 60.00
    },
    {
        "name": "Calamari",
        "desc": None,
        "price": 30.00
    },
    {
        "name": "Rombo",
        "desc": None,
        "price": 60.00
    }
]


primi = [
    {
        "name": "Spaghetti con vongole",
        "desc": None,
        "price": 18.00
    },
    {
        "name": "Linguine con frutti di mare",
        "desc": None,
        "price": 15.00
    },
    {
        "name": "Linguine al cartoccio",
        "desc": None,
        "price": 18.00
    },
    {
        "name": "Linguine con scampi",
        "desc": None,
        "price": 22.00
    },
    {
        "name": "Linguine con gamberoni",
        "desc": None,
        "price": 22.00
    },
    {
        "name": "Pacchero all'astice",
        "desc": None,
        "price": 24.00
    },
    {
        "name": "Risotto alla pescatora",
        "desc": None,
        "price": 18.00
    },
    {
        "name": "Risotto con gamberi di cetara e limone",
        "desc": None,
        "price": 22.00
    },
    {
        "name": "Spaghetto con riccio e lime a flambe'",
        "desc": None,
        "price": 20.00
    },
    {
        "name": "Primo dello chef",
        "desc": None,
        "price": 24.00
    }
]


secondi = [
    {
        "name": "Calamari alla brace",
        "desc": None,
        "price": 18.00
    },
    {
        "name": "Gamberoni alla brace",
        "desc": None,
        "price": 20.00
    },
    {
        "name": "Scampi",
        "desc": None,
        "price": 24.00
    },
    {
        "name": "Pesce Spada",
        "desc": None,
        "price": 18.00
    },
    {
        "name": "Tonno",
        "desc": None,
        "price": 18.00
    },
    {
        "name": "Baccala",
        "desc": None,
        "price": 15.00
    },
    {
        "name": "Salmone",
        "desc": None,
        "price": 15.00
    },
    {
        "name": "Polpo",
        "desc": None,
        "price": 18.00
    }
]


secondi = [
    {
        "name": "Calamari alla brace",
        "desc": None,
        "price": 18.00
    },
    {
        "name": "Gamberoni alla brace",
        "desc": None,
        "price": 20.00
    },
    {
        "name": "Scampi",
        "desc": None,
        "price": 24.00
    },
    {
        "name": "Pesce Spada",
        "desc": None,
        "price": 18.00
    },
    {
        "name": "Tonno",
        "desc": None,
        "price": 18.00
    },
    {
        "name": "Baccala",
        "desc": None,
        "price": 15.00
    },
    {
        "name": "Salmone",
        "desc": None,
        "price": 15.00
    },
    {
        "name": "Polpo",
        "desc": None,
        "price": 18.00
    }
]

secondi = [
    {
        "name": "Calamari alla brace",
        "desc": None,
        "price": 18.00
    },
    {
        "name": "Gamberoni alla brace",
        "desc": None,
        "price": 20.00
    },
    {
        "name": "Scampi",
        "desc": None,
        "price": 24.00
    },
    {
        "name": "Pesce Spada",
        "desc": None,
        "price": 18.00
    },
    {
        "name": "Tonno",
        "desc": None,
        "price": 18.00
    },
    {
        "name": "Baccala",
        "desc": None,
        "price": 15.00
    },
    {
        "name": "Salmone",
        "desc": None,
        "price": 15.00
    },
    {
        "name": "Polpo",
        "desc": None,
        "price": 18.00
    }
]

nostri_fritti = [
    {
        "name": "Cuoppo fritto",
        "desc": "baccalà, calamari, gamberi e polpo",
        "price": 16.00
    },
    {
        "name": "Fritto di calamari",
        "desc": None,
        "price": 13.00
    },
    {
        "name": "Fritto di gamberi e calamari",
        "desc": None,
        "price": 16.00
    },
    {
        "name": "Fritto di baccala",
        "desc": None,
        "price": 14.00
    },
    {
        "name": "Fritto di paranza",
        "desc": None,
        "price": 16.00
    },
    {
        "name": "Fritto di alici",
        "desc": None,
        "price": 10.00
    }
]


contorni = [
    {
        "name": "Insalata verde",
        "desc": None,
        "price": 5.00
    },
    {
        "name": "Insalata mista",
        "desc": None,
        "price": 5.00
    },
    {
        "name": "Friarielli",
        "desc": None,
        "price": 5.00
    },
    {
        "name": "Verdure alla griglia",
        "desc": None,
        "price": 5.00
    },
    {
        "name": "Patate fritte",
        "desc": None,
        "price": 5.00
    }
]

frutta = [
    {
        "name": "Ananas",
        "desc": None,
        "price": 5.00
    },
    {
        "name": "Frutta mista di stagione",
        "desc": None,
        "price": 7.00
    }
]

dolci = [
    {
        "name": "Sorbetto al limone",
        "desc": None,
        "price": 6.00
    },
    {
        "name": "Tiramisu'",
        "desc": None,
        "price": 6.00
    },
    {
        "name": "Millefoglie scomposta",
        "desc": None,
        "price": 6.00
    }
]

bibite = [
    {
        "name": "Acqua grande",
        "desc": "0.75cl",
        "price": 2.50
    },
    {
        "name": "Coca cola",
        "desc": "0.33cl",
        "price": 3.00
    },
    {
        "name": "Fanta",
        "desc": "0.33cl",
        "price": 3.00
    },
    {
        "name": "Sprite",
        "desc": "0.33cl",
        "price": 3.00
    },
    {
        "name": "Birre",
        "desc": "0.33cl",
        "price": 4.00
    }
]


vini_al_calice = [
    {
        "name": "Bianco - Rosso campani",
        "desc": None,
        "price": 6.00
    },
    {
        "name": "Calice prosecco",
        "desc": None,
        "price": 5.00
    }
]

bar = [
    {
        "name": "Caffè",
        "desc": None,
        "price": 1.50
    },
    {
        "name": "Amari nazionali",
        "desc": None,
        "price": 5.00
    },
    {
        "name": "Limoncello / Meloncello",
        "desc": None,
        "price": 3.00
    },
    {
        "name": "Grappe",
        "desc": None,
        "price": 5.00
    }
]

vini_bianchi_campania = [

    {
        "name": "Falanghina",
        "desc": "CANTAVITAE",
        "price": 15.00
    },
    {
        "name": "Greco di tufo",
        "desc": "CANTAVITAE",
        "price": 15.00
    },
    {
        "name": "Fiano avellino",
        "desc": "CANTAVITAE",
        "price": 15.00
    },
    {
        "name": "Fiano colli di lapio",
        "desc": "ROMANO CLELIA",
        "price": 25.00
    },
    {
        "name": "Greco di tufo",
        "desc": "BENITO FERRARA VIGNA CICOGNA",
        "price": 28.00
    },
    {
        "name": "Biancolella d'ischia",
        "desc": "CASA D'AMBRA",
        "price": 28.00
    },
    {
        "name": "Lacrima Christi",
        "desc": "FEUDI DI SAN GREGORIO",
        "price": 22.00
    },
    {
        "name": "Costa d'amalfi",
        "desc": "MARISA CUOMO",
        "price": 28.00
    }
]

vini_bianchi_adige = [
    {
        "name": "Gewurztraminer",
        "desc": "SAN MICHELE APPIANO",
        "price": 25.00
    },
    {
        "name": "Chardonnay",
        "desc": "SAN MICHELE APPIANO",
        "price": 25.00
    },
    {
        "name": "Blange' ceretto",
        "desc": "ARNEIS",
        "price": 33.00
    },
    {
        "name": "Sharis",
        "desc": "LIVIO FELLUGA",
        "price": 24.00
    }
]
    
vini_bianchi_prosecco = [
    {
        "name": "Prosecco brut",
        "desc": "VALDOBBIADENE",
        "price": 18.00
    },
    {
        "name": "Fergherttina brut",
        "desc": "FRANCIACORTA",
        "price": 30.00
    },
    {
        "name": "Ca' del bosco",
        "desc": "FRANCIACORTA",
        "price": 55.00
    }
]
    
vini_rossi = [
    {
        "name": "Gragnano",
        "desc": "Ottouve",
        "price": 23.00
    },
    {
        "name": "Rue Dell'Inchiostro",
        "desc": "Aglianico beneventano",
        "price": 18.00
    },
    {
        "name": "Simone Giacomo",
        "desc": "Benevento rosato",
        "price": 15.00
    },
    {
        "name": "Marisa Cuomo",
        "desc": "Costa d'amalfi",
        "price": 28.00
    }
]



@app.route("/")
def index():
    return render_template("dashboard.html", title = "Sunshine")


@app.route("/menu")
def menu_page():
    return render_template("menu_page.html", antipasti = menu_antipasti_speciali, 
    crudi = menu_crudi_ostriche, crostacei = menu_crostacei, antipasti_freddi = antipasti_freddi, 
    antipasti_caldi = antipasti_caldi, pescato_del_giorno = pescato_del_giorno, primi = primi, secondi = secondi,
    nostri_fritti = nostri_fritti, contorni= contorni, frutta = frutta, dolci = dolci, bibite = bibite, 
    vini_al_calice = vini_al_calice, bar = bar, vini_bianchi_campania = vini_bianchi_campania,
    vini_rossi=vini_rossi, vini_bianchi_adige = vini_bianchi_adige, vini_bianchi_prosecco = vini_bianchi_prosecco)


@app.route("/services")
def services():
    return render_template("services.html")


@app.route("/about")
def about():
    return render_template("chi-siamo.html")


@app.route("/privacy")
def privacy():
    return render_template("privacy.html")



if __name__ == "__main__":
    app.run()



