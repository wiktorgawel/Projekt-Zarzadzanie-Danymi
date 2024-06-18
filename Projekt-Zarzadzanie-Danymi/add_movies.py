from app import app, db, Movie


sample_movies = [
    {"title": "Gladiator", "description": "Rzymski generał zostaje zdradzony i jego rodzina zamordowana przez skorumpowanego syna cesarza. Przychodzi do Rzymu jako gladiator, aby szukać zemsty.", "rating": 8.5, "year": 2000, "genre": "Akcja", "image_url": "images/gladiator.jpg"},
    {"title": "Skazani na Shawshank", "description": "Dwóch więźniów zbliża się do siebie przez lata, znajdując pocieszenie i ostateczne odkupienie dzięki aktom wspólnej przyzwoitości.", "rating": 9.3, "year": 1994, "genre": "Dramat", "image_url": "images/shawshank.jpg"},
    {"title": "Leon Zawodowiec", "description": "12-letnia dziewczynka zostaje niechętnie przyjęta przez Léona, zawodowego zabójcę, po tym jak jej rodzina zostaje zamordowana.", "rating": 8.5, "year": 1994, "genre": "Thriller", "image_url": "images/leon.jpg"},
    {"title": "Lot nad kukułczym gniazdem", "description": "Buntowniczy więzień udaje chorobę psychiczną, aby uniknąć pracy w więzieniu. Trafia do szpitala psychiatrycznego, gdzie staje się świadkiem okrutnych praktyk medycznych.", "rating": 8.7, "year": 1975, "genre": "Dramat", "image_url": "images/lot.jpg"},
    {"title": "Władca Pierścieni: Powrót Króla", "description": "Ostateczna bitwa o Śródziemie. Frodo i Sam zbliżają się do Góry Przeznaczenia, aby zniszczyć Jedynego Pierścienia.", "rating": 8.9, "year": 2003, "genre": "Fantasy", "image_url": "images/wladca.jpg"},
    {"title": "Lista Schindlera", "description": "Prawdziwa historia Oskara Schindlera, który uratował ponad tysiąc Żydów podczas Holokaustu.", "rating": 8.9, "year": 1993, "genre": "Historyczny", "image_url": "images/lista.jpg"},
    {"title": "Pulp Fiction", "description": "Historia kilku postaci związanych z przestępczym półświatkiem Los Angeles.", "rating": 8.9, "year": 1994, "genre": "Kryminał", "image_url": "images/pulp.jpg"},
    {"title": "Podziemny Krąg", "description": "Młody mężczyzna cierpiący na bezsenność tworzy nielegalny klub walki z charyzmatycznym Tylerem Durdenem.", "rating": 8.8, "year": 1999, "genre": "Dramat", "image_url": "images/podziemny.jpg"},
    {"title": "Forrest Gump", "description": "Historia życia Forresta Gumpa, człowieka o niskim ilorazie inteligencji, który dzięki swej dobroci osiąga niezwykłe rzeczy.", "rating": 8.8, "year": 1994, "genre": "Dramat", "image_url": "images/forrest.jpg"},
    {"title": "Incepcja", "description": "Złodziej, który potrafi kraść sekrety z podświadomości podczas snu, dostaje zadanie wszczepienia idei w umyśle miliardera.", "rating": 8.8, "year": 2010, "genre": "Sci-Fi", "image_url": "images/incepcja.jpg"},
    {"title": "Contra tiempo Niewidzialny gość", "description": "Młody biznesmen budzi się w zamkniętym pokoju hotelowym obok ciała swojej martwej kochanki. Zatrudnia prestiżową prawniczkę, aby go broniła, i razem próbują odkryć, co się stało.", "rating": 8.7, "year": 1999, "genre": "Sci-Fi", "image_url": "images/contra.jpg"},
    {"title": "Joker", "description": "Strudzony życiem komik popada w obłęd i staje się psychopatycznym mordercą.", "rating": 8, "year": 2019, "genre": "Dramat", "image_url": "images/joker.jpg"},
    {"title": "Król Lew", "description": "Młody lew o imieniu Simba musi przezwyciężyć swoje obawy i odzyskać swoje miejsce jako prawowity król Lwiej Ziemi po tragicznej śmierci swojego ojca.", "rating": 8.5, "year": 1994, "genre": "Animacja", "image_url": "images/krollew.jpg"},
    {"title": "Chłopiec w pasiastej piżamie", "description": "Niewinna przyjaźń między ośmioletnim chłopcem a żydowskim chłopcem w obozie koncentracyjnym prowadzi do tragicznych konsekwencji.", "rating": 7.8, "year": 2008, "genre": "Dramat", "image_url": "images/pasiastej.jpg"},
    {"title": "Interstellar", "description": "Zespół astronautów podróżuje przez tunel czasoprzestrzenny w poszukiwaniu nowego domu dla ludzkości.", "rating": 8.6, "year": 2014, "genre": "Sci-Fi", "image_url": "images/inter.jpg"},
    {"title": "Oppenheimer", "description": "Biografia J. Roberta Oppenheimera, twórcy bomby atomowej, ukazująca jego życie i moralne dylematy związane z wynalezieniem broni masowego rażenia.", "rating": 8.5, "year": 2023, "genre": "Biograficzny", "image_url": "images/oppen.jpg"},
    {"title": "Bohemian Rhapsody", "description": "Historia legendarnego zespołu Queen i ich charyzmatycznego wokalisty Freddiego Mercury'ego.", "rating": 8, "year": 2018, "genre": "Biograficzny", "image_url": "images/bohemian.jpg"},
    {"title": "Shrek", "description": "Ogr Shrek wyrusza na misję ratunkową, aby uwolnić księżniczkę Fionę z zamku strzeżonego przez smoka.", "rating": 8.1, "year": 2001, "genre": "Animacja", "image_url": "images/shrek.jpg"},
    {"title": "Chłopaki nie płaczą", "description": "Dwóch młodych mężczyzn wplątuje się w niebezpieczne sytuacje, starając się zdobyć serca swoich wybranek.", "rating": 7.6, "year": 2000, "genre": "Komedia", "image_url": "images/chlopaki.jpg"},
    {"title": "Piraci z Karaibów: Klątwa Czarnej Perły", "description": "Kapitan Jack Sparrow wyrusza na poszukiwanie swojego skradzionego statku, jednocześnie ratując córkę gubernatora z rąk przeklętych piratów.", "rating": 8, "year": 2003, "genre": "Przygodowy", "image_url": "images/piraciklatwa.jpg"},
    {"title": "Wilk z Wall Street", "description": "Historia Jordana Belforta, maklera giełdowego, który zdobył ogromne bogactwo i władzę, ale jego życie pogrążyło się w korupcji i nadużyciach.", "rating": 8.2, "year": 2013, "genre": "Biograficzny", "image_url": "images/wilk.jpg"},
    {"title": "Harry Potter i Czara Ognia", "description": "Harry Potter bierze udział w prestiżowym Turnieju Trójmagicznym, gdzie musi stawić czoła niebezpiecznym wyzwaniom i odkryć mroczne tajemnice.", "rating": 7.7, "year": 2005, "genre": "Fantasy", "image_url": "images/czara.jpg"},
    {"title": "Życie jest piękne", "description": "Włoski Żyd stara się chronić swojego syna przed okropnościami obozu koncentracyjnego, przekonując go, że to tylko gra.", "rating": 8.6, "year": 1997, "genre": "Dramat", "image_url": "images/zycie.jpg"},
    {"title": "Matrix", "description": "Programista odkrywa, że rzeczywistość, w której żyje, jest tylko wirtualną iluzją stworzona przez inteligentne maszyny, które zniewoliły ludzkość.", "rating": 8.7, "year": 1999, "genre": "Sci-Fi", "image_url": "images/matrix.jpg"},
    {"title": "Zielona mila", "description": "Strażnik więzienny na oddziale śmierci nawiązuje niezwykłą więź z więźniem obdarzonym nadnaturalnymi zdolnościami.", "rating": 8.6, "year": 1999, "genre": "Dramat", "image_url": "images/zielona.jpg"},
    {"title": "Ojciec chrzestny", "description": "Historia potężnej rodziny mafijnej Corleone, która stara się utrzymać swoją pozycję w świecie przestępczym.", "rating": 9.2, "year": 1972, "genre": "Kryminał", "image_url": "images/ojciec.jpg"},
    {"title": "Titanic", "description": "Opowieść o miłości między Jackiem i Rose na pokładzie nieszczęsnego Titanica, który zatonął podczas swojego dziewiczego rejsu.", "rating": 7.8, "year": 1997, "genre": "Romans", "image_url": "images/titanic.jpg"},
    {"title": "Władca Pierścieni: Powrót Króla", "description": "Frodo i Sam zbliżają się do Góry Przeznaczenia, aby zniszczyć Jedyny Pierścień, podczas gdy Aragorn prowadzi swoich ludzi do ostatniej bitwy.", "rating": 8.9, "year": 2003, "genre": "Fantasy", "image_url": "images/wladca.jpg"},
    {"title": "Pamiętnik", "description": "Młoda kobieta zakochuje się w mężczyźnie z niższej klasy społecznej, a ich miłość przetrwała próbę czasu mimo wielu przeciwności.", "rating": 7.8, "year": 2004, "genre": "Romans", "image_url": "images/pamietnik.jpg"},
    {"title": "Hobbit: Niezwykła podróż", "description": "Bilbo Baggins wyrusza na epicką wyprawę, aby pomóc krasnoludom odzyskać ich zaginione królestwo.", "rating": 7.8, "year": 2012, "genre": "Fantasy", "image_url": "images/hobbit.jpg"},
    {"title": "Siedem", "description": "Detektyw bada sprawę seryjnego mordercy, który zabija swoje ofiary na podstawie siedmiu grzechów głównych.", "rating": 8.6, "year": 1995, "genre": "Thriller", "image_url": "images/siedem.jpg"},
    {"title": "Marsjanin", "description": "Astronauta zostaje przypadkowo pozostawiony na Marsie i musi wykorzystać swoje umiejętności, aby przetrwać i znaleźć sposób na powrót na Ziemię.", "rating": 8, "year": 2015, "genre": "Sci-Fi", "image_url": "images/mars.jpg"}
]
with app.app_context():
    db.drop_all()
    db.create_all()
    
    for movie in sample_movies:
        new_movie = Movie(
            title=movie["title"],
            description=movie["description"],
            rating=movie["rating"],
            year=movie["year"],
            genre=movie["genre"],
            image_url=movie["image_url"]
        )
        db.session.add(new_movie)
    
    db.session.commit()

print("Filmy zostały dodane do bazy danych")
