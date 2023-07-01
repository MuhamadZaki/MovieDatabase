from flask import Flask

app = Flask(__name__)

movies = [
    {
        "image": "https://www.themoviedb.org/t/p/w188_and_h282_bestv2/hEhGrcST85vMd63PBDgPBqih2tR.jpg",
        "title": "Demon Slayer: Kimetsu no Yaiba -To the Swordsmith Village-",
        "release_date": "February 3, 2023",
        "description": "After his family is viciously murdered, a kind-hearted boy named Tanjiro Kamado resolves to become a Demon Slayer in hopes of turning his younger sister Nezuko back into a human. Together with his comrades, Zenitsu and Inosuke,"
    }, 
    {
        "image": "https://www.themoviedb.org/t/p/w188_and_h282_bestv2/9YEGawvjaRgnyW6QVcUhFJPFDco.jpg",
        "title": "Black Clover: Sword of the Wizard King",
        "release_date": "June 16, 2023",
        "description": "As a lionhearted boy who can’t wield magic strives for the title of Wizard King, four banished Wizard Kings of yore return to crush the Clover Kingdom."
    },
    {
        "image": "https://www.themoviedb.org/t/p/w188_and_h282_bestv2/iTmJwZxGHYAk5EiVc68UvZTMSuP.jpg",
        "title": "Demon Slayer: Kimetsu no Yaiba the Hashira Meeting Arc",
        "release_date": "April 15, 2021",
        "description": "Tanjiro and his sister Nezuko have been apprehended by the Demon Slayer Hashira, a group of extremely skilled swordfighters. Tanjiro undergoes trial for violating the Demon Slayer code, specifically smuggling Nezuko, a Demon,"
    },
    {
        "image": "https://www.themoviedb.org/t/p/w188_and_h282_bestv2/mFp3l4lZg1NSEsyxKrdi0rNK8r1.jpg",
        "title": "To Catch a Killer",
        "release_date": "April 6, 2023",
        "description": "Baltimore. New Year's Eve. A talented but troubled police officer is recruited by the FBI's chief investigator to help profile and track down a mass murderer."
    },
    {
        "image": "https://www.themoviedb.org/t/p/w188_and_h282_bestv2/wq1UG5lPCKpOJgmgpKJszKvoMUe.jpg",
        "title": "Demon Slayer: Kimetsu no Yaiba Mt. Natagumo Arc",
        "release_date": "April 15, 2021",
        "description": "Tanjiro, now a registered Demon Slayer, teams up with fellow slayers Zenitsu and Inosuke to investigate missing person cases on the mountain Natagumo. After the group is split up during a fight with possessed swordfighters, they"
    },
    {

        "image": "https://www.themoviedb.org/movie/820232",
        "title": "Demon Slayer: Kimetsu no Yaiba Sibling's Bond",
        "relase_date": "March 29, 2019",
        "description" : "Tanjiro finds his family slaughtered and the lone survivor, his sister Nezuko Kamado, turned into a Demon. To his surprise, however, Nezuko still shows signs of human emotion and thought. Thus begins Tanjiro's journey to seek out the Demon who killed their family and turn his sister human again. A recap film of Kimetsu no Yaiba, covering episodes 1-5 with extra footage."
    },
    {
        "image": "https://www.themoviedb.org/movie/76597-k",
        "title": "K",
        "relase_date": "August 27, 1997",
        "description": "In this French crime film, set during the time of the Gulf War, an elderly German tourist is murdered in Paris by junk dealer Joseph Katz (Pinkas Braun), a friend of Paris detective Sam Bellamy (singer Patrick Bruel). Romantically involved with the victim's daughter Emma Guter (Isabella Ferrari), Bellamy covers up the crime he witnessed. Joseph then mysteriously vanishes, and Bellamy heads for Berlin"


    },
    {
        "image": "https://www.themoviedb.org/movie/895003",
        "title" : "Demon Slayer: Kimetsu no Yaiba - Asakusa Arc",
        "relase_date": "August 25, 2022",
        "description": "Tanjiro ventures to Asakusa, Tokyo for his second mission with the Demon Slayer Corps."
        
    },
    {
        "image": "https://www.themoviedb.org/movie/619329-munthiri-kaadu",
        "title": "Munthiri Kaadu",
        "relase_date": "April 7, 2023",
        "description": "In a Village Where they used to Honor Kill Love couples of the opposite cast and in that village A girl and boy from the opposite cast who used to be friends are getting pressure from village people that they love each other . What happens at the End?"
        
    },
    {
        "image": "https://www.themoviedb.org/movie/895006",
        "title": "Demon Slayer: Kimetsu no Yaiba - Tsuzumi Mansion Arc",
        "relase_date": "September 15, 2022",
        "description": "Tanjiro ventures to the south-southeast where he encounters a cowardly young man named Zenitsu Agatsuma. He is a fellow survivor from Final Selection and his sparrow asks Tanjiro to help keep him in line."

    },
    {
        "image": "https://www.themoviedb.org/movie/985103-untitled-kral-sakir-sequel",
        "title": "July 14, 2022",
        "relase_date": "July 14, 2022",
        "description": "Scientists trying to solve the environmental crisis of pollution devise a way to send the collected garbage into space via rocket ships. When this garbage starts to land on alien planets, the outraged aliens head to Earth for revenge. King Shakir and his family must do"

    },
    {
        "image": "https://www.themoviedb.org/movie/635302",
        "title": "Demon Slayer -Kimetsu no Yaiba- The Movie: Mugen Train",
        "relase_date": "January 6, 2021",
        "description": "Tanjiro Kamado, joined with Inosuke Hashibira, a boy raised by boars who wears a boar's head, and Zenitsu Agatsuma, a scared boy who reveals his true power when he sleeps, boards the Infinity Train on a new mission with the Fire Hashira, Kyojuro Rengoku, to"

    },
    {
        "image": "https://www.themoviedb.org/movie/113082-beruseruku-ougon-jidaihen-i-haou-no-tamago",
        "title": "Berserk: The Golden Age Arc I - The Egg of the King",
        "relase_date": "February 3, 2012",
        "description": "Guts, an immensely strong sword-for-hire, has little direction in his life, simply fighting one battle after the next. However, this all changes suddenly when he meets and is bested by Griffith, a beautiful and charismatic young man who leads the Band of the Hawk"
    }
]

@app.route("/")
def index():
    return movies