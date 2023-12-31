# Mengimpor modul-modul yang diperlukan dari library Flask
from flask import Flask, jsonify, render_template,json
from flask import request

# Membuat instance Flask dengan nama aplikasinya 'app'
app = Flask(__name__)

# Mendefinisikan list 'movies' yang berisi dua sub-list, masing-masing mewakili satu set film
movies = [
    # Sub list pertama!
    [
        # Informasi movies pertama dalam sub list pertama dalam bentuk dictionary
        {
            "image": "https://www.themoviedb.org/t/p/w188_and_h282_bestv2/hEhGrcST85vMd63PBDgPBqih2tR.jpg",
            "title": "Demon Slayer: Kimetsu no Yaiba -To the Swordsmith Village-",
            "release_date": "February 3, 2023",
            "description": "After his family is viciously murdered, a kind-hearted boy named Tanjiro Kamado resolves to become a Demon Slayer in hopes of turning his younger sister Nezuko back into a human. Together with his comrades, Zenitsu and Inosuke,"
        }, 
        # Informasi movies kedua dalam sub list pertama, bentuk dictionary
        {
            "image": "https://www.themoviedb.org/t/p/w188_and_h282_bestv2/9YEGawvjaRgnyW6QVcUhFJPFDco.jpg",
            "title": "Black Clover: Sword of the Wizard King",
            "release_date": "June 16, 2023",
            "description": "As a lionhearted boy who can’t wield magic strives for the title of Wizard King, four banished Wizard Kings of yore return to crush the Clover Kingdom."
        },
          # Informasi movies ketiga dalam sub list pertama, bentuk dictionary
        {
            "image": "https://www.themoviedb.org/t/p/w188_and_h282_bestv2/iTmJwZxGHYAk5EiVc68UvZTMSuP.jpg",
            "title": "Demon Slayer: Kimetsu no Yaiba the Hashira Meeting Arc",
            "release_date": "April 15, 2021",
            "description": "Tanjiro and his sister Nezuko have been apprehended by the Demon Slayer Hashira, a group of extremely skilled swordfighters. Tanjiro undergoes trial for violating the Demon Slayer code, specifically smuggling Nezuko, a Demon,"
        },
          # Informasi movies keempat dalam sub list pertama, bentuk dictionary
        {
            "image": "https://www.themoviedb.org/t/p/w188_and_h282_bestv2/mFp3l4lZg1NSEsyxKrdi0rNK8r1.jpg",
            "title": "To Catch a Killer",
            "release_date": "April 6, 2023",
            "description": "Baltimore. New Year's Eve. A talented but troubled police officer is recruited by the FBI's chief investigator to help profile and track down a mass murderer."
        },
          # Informasi movies kelima dalam sub list pertama, bentuk dictionary
        {
            "image": "https://www.themoviedb.org/t/p/w188_and_h282_bestv2/wq1UG5lPCKpOJgmgpKJszKvoMUe.jpg",
            "title": "Demon Slayer: Kimetsu no Yaiba Mt. Natagumo Arc",
            "release_date": "April 15, 2021",
            "description": "Tanjiro, now a registered Demon Slayer, teams up with fellow slayers Zenitsu and Inosuke to investigate missing person cases on the mountain Natagumo. After the group is split up during a fight with possessed swordfighters, they"
        },
          # Informasi movies keenam dalam sub list pertama, bentuk dictionary
        {

            "image": "https://www.themoviedb.org/movie/820232",
            "title": "Demon Slayer: Kimetsu no Yaiba Sibling's Bond",
            "relase_date": "March 29, 2019",
            "description" : "Tanjiro finds his family slaughtered and the lone survivor, his sister Nezuko Kamado, turned into a Demon. To his surprise, however, Nezuko still shows signs of human emotion and thought. Thus begins Tanjiro's journey to seek out the Demon who killed their family and turn his sister human again. A recap film of Kimetsu no Yaiba, covering episodes 1-5 with extra footage."
        },
          # Informasi movies ketujuh dalam sub list pertama, bentuk dictionary
        {
            "image": "https://www.themoviedb.org/movie/76597-k",
            "title": "K",
            "relase_date": "August 27, 1997",
            "description": "In this French crime film, set during the time of the Gulf War, an elderly German tourist is murdered in Paris by junk dealer Joseph Katz (Pinkas Braun), a friend of Paris detective Sam Bellamy (singer Patrick Bruel). Romantically involved with the victim's daughter Emma Guter (Isabella Ferrari), Bellamy covers up the crime he witnessed. Joseph then mysteriously vanishes, and Bellamy heads for Berlin"


        },
          # Informasi movies kedelapan dalam sub list pertama, bentuk dictionary
        {
            "image": "https://www.themoviedb.org/movie/895003",
            "title" : "Demon Slayer: Kimetsu no Yaiba - Asakusa Arc",
            "relase_date": "August 25, 2022",
            "description": "Tanjiro ventures to Asakusa, Tokyo for his second mission with the Demon Slayer Corps."
            
        },
          # Informasi movies kesembilan dalam sub list pertama, bentuk dictionary
        {
            "image": "https://www.themoviedb.org/movie/619329-munthiri-kaadu",
            "title": "Munthiri Kaadu",
            "relase_date": "April 7, 2023",
            "description": "In a Village Where they used to Honor Kill Love couples of the opposite cast and in that village A girl and boy from the opposite cast who used to be friends are getting pressure from village people that they love each other . What happens at the End?"
            
        },
          # Informasi movies kesepuluh dalam sub list pertama, bentuk dictionary
        {
            "image": "https://www.themoviedb.org/movie/895006",
            "title": "Demon Slayer: Kimetsu no Yaiba - Tsuzumi Mansion Arc",
            "relase_date": "September 15, 2022",
            "description": "Tanjiro ventures to the south-southeast where he encounters a cowardly young man named Zenitsu Agatsuma. He is a fellow survivor from Final Selection and his sparrow asks Tanjiro to help keep him in line."

        },
    ],
    # Sub list kedua!
    [
        # Informasi movies pertama dalam sub list kedua dalam bentuk dictionary
        {
            "image": "https://www.themoviedb.org/movie/985103-untitled-kral-sakir-sequel",
            "title": "July 14, 2022",
            "relase_date": "July 14, 2022",
            "description": "Scientists trying to solve the environmental crisis of pollution devise a way to send the collected garbage into space via rocket ships. When this garbage starts to land on alien planets, the outraged aliens head to Earth for revenge. King Shakir and his family must do"

        },
        # Informasi movies kedua dalam sub list kedua, bentuk dictionary
        {
            "image": "https://www.themoviedb.org/movie/635302",
            "title": "Demon Slayer -Kimetsu no Yaiba- The Movie: Mugen Train",
            "relase_date": "January 6, 2021",
            "description": "Tanjiro Kamado, joined with Inosuke Hashibira, a boy raised by boars who wears a boar's head, and Zenitsu Agatsuma, a scared boy who reveals his true power when he sleeps, boards the Infinity Train on a new mission with the Fire Hashira, Kyojuro Rengoku, to"

        },
         # Informasi movies ketiga dalam sub list kedua, bentuk dictionary
        {
            "image": "https://www.themoviedb.org/movie/113082-beruseruku-ougon-jidaihen-i-haou-no-tamago",
            "title": "Berserk: The Golden Age Arc I - The Egg of the King",
            "relase_date": "February 3, 2012",
            "description": "Guts, an immensely strong sword-for-hire, has little direction in his life, simply fighting one battle after the next. However, this all changes suddenly when he meets and is bested by Griffith, a beautiful and charismatic young man who leads the Band of the Hawk"
        }
        
    ]    
]

# Mendefinisikan list 'details' yang berisi dua dictionary yang mewakili informasi details tentang movies
details = [
    {
        "image": "https://www.themoviedb.org/movie/1067282",
        "title": "Demon Slayer: Kimetsu no Yaiba -To the Swordsmith Village",
        "relase_date": "02/03/2023",
        "genres": ["Action", "Animation", "Fantasy"],
        "duration": "1h 55m",
        "rating":  "74",
        "description": "After his family is viciously murdered, a kind-hearted boy named Tanjiro Kamado resolves to become a Demon Slayer in hopes of turning his younger sister Nezuko back into a human. Together with his comrades, Zenitsu and Inosuke, along with one of the top-ranking members of the Demon Slayer Corps, Tengen Uzui, Tanjiro embarks on a mission within the Entertainment District, where they encounter the formidable, high-ranking demons, Daki and Gyutaro."
    },
    {
        "image": "https://www.themoviedb.org/movie/113082-beruseruku-ougon-jidaihen-i-haou-no-tamago",
        "title": "Berserk: The Golden Age Arc I - The Egg of the King ",
        "relase_date": "02/03/2012",
        "genres": [ "Action & Adventure", "Fantasy", "Animation"],
        "duration": "1h 16m",
        "rating": "72",
        "description": "Guts, an immensely strong sword-for-hire, has little direction in his life, simply fighting one battle after the next. However, this all changes suddenly when he meets and is bested by Griffith, a beautiful and charismatic young man who leads the Band of the Hawk mercenary army. After Guts joins the Band and the relationship between the two men begins to blossom, Casca, the tough, lone swordswoman in the Band of the Hawk, struggles to accept Guts and the influence he has on the world around her. While the two men begin to fight together, Griffith continues to rise to power, all seemingly in order to reach his mysterious, prophesied goals. What lengths will Guts and Griffith go to in order to reach these goals, and where will fate take the two men?"

    },
    {
        "image": "https://www.themoviedb.org/movie/643215-asterix-obelix-l-empire-du-milieu",
        "title": "Asterix & Obelix: The Middle Kingdom",
        "relase_date": "02/01/2023 ",
        "genres": ["Comedy", "Adventure", "Family"],
        "duation": "1h 52m",
        "rating": "49",
        "description": "Gallic heroes and forever friends Asterix and Obelix journey to China to help Princess Sa See save the Empress and her land from a nefarious prince."
    },
    {
        "image": "https://www.themoviedb.org/movie/455476-knights-of-the-zodiac",
        "title": "Knights of the Zodiac",
        "relase_date": "04/28/2023",
        "genres": ["Fantasy", "Action", "Adventure"],
        "duration": "1h 52m",
        "rating": "65",
        "description": "When a headstrong street orphan, Seiya, in search of his abducted sister unwittingly taps into hidden powers, he discovers he might be the only person alive who can protect a reincarnated goddess, sent to watch over humanity. Can he let his past go and embrace his destiny to become a Knight of the Zodiac?"
    },
    {
        "image": "https://www.themoviedb.org/movie/948713-the-last-kingdom-seven-kings-must-die",
        "title": "The Last Kingdom: Seven Kings Must Die",
        "relase_date": "04/14/2023",
        "genres": ["Action", "Adventure", "War"],
        "duration": "1h 51m",
        "rating": "73",
        "description": "In the wake of King Edward's death, Uhtred of Bebbanburg and his comrades adventure across a fractured kingdom in the hopes of uniting England at last."
    },
    {
        "image": "https://www.themoviedb.org/movie/856245-matar-a-la-bestia",
        "title": "To Kill the Beast",
        "relase_date": "12/10/2021 ",
        "genres": ["Mystery", "Fantasy","Thriller"],
        "duration": "1h 29m",
        "rating": "62",
        "description": "Emilia arrives at her Aunt Inés' hostel located on the Argentina-Brazil border, looking for her missing brother. In this lush jungle a dangerous beast which takes the form of different animals seems to be roaming around."
    },
    {
        "image": "https://www.themoviedb.org/movie/377883-smeshariki-legenda-o-zolotom-drakone",
        "title": "Kikoriki. Legend of the Golden Dragon",
        "relase_date": "03/17/2016",
        "genres": ["Animation", "Family"],
        "duration": "1h 20m",
        "rating": "72",
        "description": "The lovably simple residents of peaceful Kikoriki Island are thrown kicking and screaming into big adventure, when their resident scientist invents an amazing device - a helmet called the Improverizor, which takes personality traits from one person and swaps them with traits of someone else. But when spineless young Wally tries to use the untested device to cure his cowardice, he ends up even more spineless - by getting accidentally body-switched with a squirmy little caterpillar. Now he has even more to fear than he could have ever imagined, and so do his fellow villagers, as they're dragged into a madcap adventure packed with plane crashes, mistaken identities, erupting volcanoes and angry primitives on the warpath. Boy, do the Kikoriki Crew wish they could switch place now - with anyone."
    },
    {
        "image": "https://www.themoviedb.org/movie/670327",
        "title": "Marudase Kintarou",
        "relase_date": "12/11/2020",
        "genres": ["Romance", "Comedy", "Animation"],
        "duration": "10m",
        "rating": "48",
        "description": "Makoto's grandfather was the principal of the great Onodera Academy, and when he passed away, he left Makoto and his school staff with one very important will - The one man who is able to seduce Makoto with his superb sexual techniques will be given the right to take over as Onodera Academy s new principal! Because of this ridiculous last request, Makoto is now every faculty member's target for sexual harassment! Desperate to protect his virginity, Makoto seeks help from his childhood friend (and the man who he has always loved), Kintaro."
    },
    {
        "image": "https://www.themoviedb.org/movie/849869",
        "title": "Kill Boksoon",
        "relase_date": "03/31/2023",
        "genres": ["Action", "Crime", "Thriller"],
        "duration": "2h 17m",
        "rating": "69",
        "description": "At work, she's a renowned assassin. At home, she's a single mom to a teenage daughter. Killing? That's easy. It's parenting that's the hard part."
    },
    {
        "image": "https://www.themoviedb.org/movie/406563-insidious-chapter-4",
        "title": "Insidious: The Last Key",
        "relase_date": "01/05/2018",
        "genres": ["Horror", "Mystery", "Thriller"],
        "duration": "1h 43m",
        "rating": "63",
        "description": "Parapsychologist Elise Rainier and her team travel to Five Keys, NM, to investigate a man’s claim of a haunting. Terror soon strikes when Rainier realizes that the house he lives in was her family’s old home."
    }
    
]

# Mendefinisikan list 'trandings' yang mewakili movies popular dengan informasi tambahan
trandings = [
    {
        "image": "https://www.themoviedb.org/movie/1067282",
        "title": "Demon Slayer: Kimetsu no Yaiba -To the Swordsmith Village",
        "relase_date": "02/03/2023",
        "genres": ["Action", "Animation", "Fantasy"],
        "duration": "1h 55m",
        "info": {"rating":74},
        "description": "After his family is viciously murdered, a kind-hearted boy named Tanjiro Kamado resolves to become a Demon Slayer in hopes of turning his younger sister Nezuko back into a human. Together with his comrades, Zenitsu and Inosuke, along with one of the top-ranking members of the Demon Slayer Corps, Tengen Uzui, Tanjiro embarks on a mission within the Entertainment District, where they encounter the formidable, high-ranking demons, Daki and Gyutaro."
    },
    {
        "image": "https://www.themoviedb.org/movie/113082-beruseruku-ougon-jidaihen-i-haou-no-tamago",
        "title": "Berserk: The Golden Age Arc I - The Egg of the King ",
        "relase_date": "02/03/2012",
        "genres": [ "Action & Adventure", "Fantasy", "Animation"],
        "duration": "1h 16m",
        "info": {"rating":72},
        "description": "Guts, an immensely strong sword-for-hire, has little direction in his life, simply fighting one battle after the next. However, this all changes suddenly when he meets and is bested by Griffith, a beautiful and charismatic young man who leads the Band of the Hawk mercenary army. After Guts joins the Band and the relationship between the two men begins to blossom, Casca, the tough, lone swordswoman in the Band of the Hawk, struggles to accept Guts and the influence he has on the world around her. While the two men begin to fight together, Griffith continues to rise to power, all seemingly in order to reach his mysterious, prophesied goals. What lengths will Guts and Griffith go to in order to reach these goals, and where will fate take the two men?"

    },
    {
        "image": "https://www.themoviedb.org/movie/643215-asterix-obelix-l-empire-du-milieu",
        "title": "Asterix & Obelix: The Middle Kingdom",
        "relase_date": "02/01/2023 ",
        "genres": ["Comedy", "Adventure", "Family"],
        "duation": "1h 52m",
        "info": {"rating":49},
        "description": "Gallic heroes and forever friends Asterix and Obelix journey to China to help Princess Sa See save the Empress and her land from a nefarious prince."
    },
    {
        "image": "https://www.themoviedb.org/movie/455476-knights-of-the-zodiac",
        "title": "Knights of the Zodiac",
        "relase_date": "04/28/2023",
        "genres": ["Fantasy", "Action", "Adventure"],
        "duration": "1h 52m",
        "info": {"rating":65},
        "description": "When a headstrong street orphan, Seiya, in search of his abducted sister unwittingly taps into hidden powers, he discovers he might be the only person alive who can protect a reincarnated goddess, sent to watch over humanity. Can he let his past go and embrace his destiny to become a Knight of the Zodiac?"
    },
    {
        "image": "https://www.themoviedb.org/movie/948713-the-last-kingdom-seven-kings-must-die",
        "title": "The Last Kingdom: Seven Kings Must Die",
        "relase_date": "04/14/2023",
        "genres": ["Action", "Adventure", "War"],
        "duration": "1h 51m",
        "info": {"rating":73},
        "description": "In the wake of King Edward's death, Uhtred of Bebbanburg and his comrades adventure across a fractured kingdom in the hopes of uniting England at last."
    },
    {
        "image": "https://www.themoviedb.org/movie/856245-matar-a-la-bestia",
        "title": "To Kill the Beast",
        "relase_date": "12/10/2021 ",
        "genres": ["Mystery", "Fantasy","Thriller"],
        "duration": "1h 29m",
        "info": {"rating":62},
        "description": "Emilia arrives at her Aunt Inés' hostel located on the Argentina-Brazil border, looking for her missing brother. In this lush jungle a dangerous beast which takes the form of different animals seems to be roaming around."
    },
    {
        "image": "https://www.themoviedb.org/movie/377883-smeshariki-legenda-o-zolotom-drakone",
        "title": "Kikoriki. Legend of the Golden Dragon",
        "relase_date": "03/17/2016",
        "genres": ["Animation", "Family"],
        "duration": "1h 20m",
        "info": {"rating":72},
        "description": "The lovably simple residents of peaceful Kikoriki Island are thrown kicking and screaming into big adventure, when their resident scientist invents an amazing device - a helmet called the Improverizor, which takes personality traits from one person and swaps them with traits of someone else. But when spineless young Wally tries to use the untested device to cure his cowardice, he ends up even more spineless - by getting accidentally body-switched with a squirmy little caterpillar. Now he has even more to fear than he could have ever imagined, and so do his fellow villagers, as they're dragged into a madcap adventure packed with plane crashes, mistaken identities, erupting volcanoes and angry primitives on the warpath. Boy, do the Kikoriki Crew wish they could switch place now - with anyone."
    },
    {
        "image": "https://www.themoviedb.org/movie/670327",
        "title": "Marudase Kintarou",
        "relase_date": "12/11/2020",
        "genres": ["Romance", "Comedy", "Animation"],
        "duration": "10m",
        "info": {"rating":40},
        "description": "Makoto's grandfather was the principal of the great Onodera Academy, and when he passed away, he left Makoto and his school staff with one very important will - The one man who is able to seduce Makoto with his superb sexual techniques will be given the right to take over as Onodera Academy s new principal! Because of this ridiculous last request, Makoto is now every faculty member's target for sexual harassment! Desperate to protect his virginity, Makoto seeks help from his childhood friend (and the man who he has always loved), Kintaro."
    },
    {
        "image": "https://www.themoviedb.org/movie/849869",
        "title": "Kill Boksoon",
        "relase_date": "03/31/2023",
        "genres": ["Action", "Crime", "Thriller"],
        "duration": "2h 17m",
        "info": {"rating":69},
        "description": "At work, she's a renowned assassin. At home, she's a single mom to a teenage daughter. Killing? That's easy. It's parenting that's the hard part."
    },
    {
        "image": "https://www.themoviedb.org/movie/406563-insidious-chapter-4",
        "title": "Insidious: The Last Key",
        "relase_date": "01/05/2018",
        "genres": ["Horror", "Mystery", "Thriller"],
        "duration": "1h 43m",
        "info": {"rating":69},
        "description": "Parapsychologist Elise Rainier and her team travel to Five Keys, NM, to investigate a man’s claim of a haunting. Terror soon strikes when Rainier realizes that the house he lives in was her family’s old home."
    }
    
]

secs= [
    {
        "image": "https://www.themoviedb.org/movie/1067282",
        "title": "DemonSlayer",
        "relase_date": "02/03/2023",
        "genres": ["Action", "Animation", "Fantasy"],
        "duration": "1h 55m",
        "info": {"rating":74},
        "description": "After his family is viciously murdered, a kind-hearted boy named Tanjiro Kamado resolves to become a Demon Slayer in hopes of turning his younger sister Nezuko back into a human. Together with his comrades, Zenitsu and Inosuke, along with one of the top-ranking members of the Demon Slayer Corps, Tengen Uzui, Tanjiro embarks on a mission within the Entertainment District, where they encounter the formidable, high-ranking demons, Daki and Gyutaro."
    },
    {
        "image": "https://www.themoviedb.org/movie/113082-beruseruku-ougon-jidaihen-i-haou-no-tamago",
        "title": "Berserk: The Golden Age",
        "relase_date": "02/03/2012",
        "genres": [ "Action & Adventure", "Fantasy", "Animation"],
        "duration": "1h 16m",
        "info": {"rating":72},
        "description": "Guts, an immensely strong sword-for-hire, has little direction in his life, simply fighting one battle after the next. However, this all changes suddenly when he meets and is bested by Griffith, a beautiful and charismatic young man who leads the Band of the Hawk mercenary army. After Guts joins the Band and the relationship between the two men begins to blossom, Casca, the tough, lone swordswoman in the Band of the Hawk, struggles to accept Guts and the influence he has on the world around her. While the two men begin to fight together, Griffith continues to rise to power, all seemingly in order to reach his mysterious, prophesied goals. What lengths will Guts and Griffith go to in order to reach these goals, and where will fate take the two men?"

    },
]
des= [
    {
        "image": "https://www.themoviedb.org/movie/1067282",
        "title": "DemonSlayer",
        "relase_date": "02/03/2023",
        "genres": ["Action", "Animation", "Fantasy"],
        "duration": "1h 55m",
        "info": {"rating":74},
        "description": "After his family is viciously murdered, a kind-hearted boy named Tanjiro Kamado resolves to become a Demon Slayer in hopes of turning his younger sister Nezuko back into a human. Together with his comrades, Zenitsu and Inosuke, along with one of the top-ranking members of the Demon Slayer Corps, Tengen Uzui, Tanjiro embarks on a mission within the Entertainment District, where they encounter the formidable, high-ranking demons, Daki and Gyutaro."
    },
    {
        "image": "https://www.themoviedb.org/movie/113082-beruseruku-ougon-jidaihen-i-haou-no-tamago",
        "title": "Berserk: The Golden Age",
        "relase_date": "02/03/2012",
        "genres": [ "Action & Adventure", "Fantasy", "Animation"],
        "duration": "1h 16m",
        "info": {"rating":72},
        "description": "Guts, an immensely strong sword-for-hire, has little direction in his life, simply fighting one battle after the next. However, this all changes suddenly when he meets and is bested by Griffith, a beautiful and charismatic young man who leads the Band of the Hawk mercenary army. After Guts joins the Band and the relationship between the two men begins to blossom, Casca, the tough, lone swordswoman in the Band of the Hawk, struggles to accept Guts and the influence he has on the world around her. While the two men begin to fight together, Griffith continues to rise to power, all seemingly in order to reach his mysterious, prophesied goals. What lengths will Guts and Griffith go to in order to reach these goals, and where will fate take the two men?"

    },
]

# Inisialisasi list kosong untuk menyimpan data film yang akan ditambahkan
add_movies = []

# Route utama ("/") untuk menampilkan list film yang telah ditambahkan
@app.route("/")
def index():
    return add_movies

# Route untuk menampilkan detail movie berdasarkan ID movie yang diberikan ("/details/<int:movie_id>">
@app.route("/details/<int:movie_id>")
def detail(movie_id):
    # Mengembalikan detail film berdasarkan ID yang diberikan
    return details[movie_id]

# Route untuk melakukan paginasi terhadap list film ("/movies")
@app.route("/movies")
def pagination():
    # Mendapatkan nomor halaman dari parameter query 'page' (jika tidak tidak ada, default ke 1)
    page = request.args.get('page', type=int)
    # Memastikan bahwa nomor halaman tidak kurang dari 1
    if page < 1:
        return "Page Minimal 1"
    # Mengembalikan list movie pada halaman yang diminta
    return movies[page - 1]

# Route untuk list film popular ("/popular") dengan metode GET
@app.route("/popular", methods=['GET'])
def get_popular():
    # Inisialisasi list kosong untuk menyimpan list movie popular
    popular_movies = []
    # Iterasi melalui list movie yang sedang tren (trandings)
    for tranding in trandings:
        # Memeriksa apakah rating film lebih besar atau sama dengan 70
        if tranding["info"]["rating"] >= 70:
            # Jika ya, tambahkan movie ke daftar popular
            popular_movies.append(tranding)
    # Mengembalikan list movie popular sebagai respons dari permintaan GET
    return popular_movies

# Route untuk melakukan pencarian ("/search") dengan metode GET
@app.route("/search", methods = ["GET"])
def get_search():
    # Mengembalikan nilai parameter 'data' dari query string
    data = request.args.get('data')
    # Memeriksa apakah parameter 'data' telah diberikan
    if data:
        # Membuat list hasil pencarian dengan menggunakan list comprehension
        # Mencari setiap elemen 'secs' yang memiliki judul yang mengandung string 'data' (case-insensitive)
        results_s = [item for item in secs if data.lower() in item["title"].lower()]
        # Memeriksa apakah ada hasil pencarian
        if results_s:
            # Jika ada hasil pencarian, mengembalikan hasil pencarian pertama sebagai JSON response
            return jsonify(results_s[0])
        else:
            # Jika tidak ada hasil pencarian, mengembalikan pesan bahwa data tidak ditemukan dengan status 404
            return jsonify({'message':'Data not found!'}), 404
    
    else:
        # Jika parameter 'data' tidak diberikan, mengembalikan pesan bahwa kunci pencarian tidak diberikan dengan status 404
        return jsonify({'message':'Search key not provided!'}), 404
        
# Route untuk menambahkan movie baru ("/movies") dengan metode post    
@app.route("/movies", methods=["POST"])
def add_movie():
    # Membuat objek movie baru berdasarkan data yang diterima dari form
    movie = {
        "title": request.form['title'],
        "description": request.form['description']
    }
    # Menambahkan movie baru ke dalam list add_movies
    add_movies.append(movie)
    # Mengembalikan pesan sukses beserta status 201 (created) sebagai respons dari permintaan POST
    return jsonify({'message':'Success Add Movie!'}), 201

# Route untuk menghapus movie berdasarkan ID ("/movies") dengan metode DELETE
@app.route("/movies", methods=["DELETE"])
def delete_movie():
    # Mengambil nilai parameter 'id' dari query string dan mengkonversinya ke tipe data int
    id = request.args.get('id', type=int)
    # Menghapus movie dari list add_movies berdasarkan ID yang diberikan
    add_movies.pop(id)
    # Mengembalikan pesan sukses beserta status 200 (OK) sebagai respon dari permintaan DELETE
    return jsonify({'message':'Success Delete Movie!'}), 200

#@app.route("/movies", methods=["PATCH"])
#def update_movie():
    # 1. Ambil index dari input (query params) dan title dari input (body params)
    # 2. Ambil array add_movies berdasarkan (query params)
    # 3. Update title berdasarkan input (body params)
