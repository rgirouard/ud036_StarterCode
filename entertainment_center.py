import fresh_tomatoes
import media


wonderful_life = media.Movie("It's a Wonderful Life",
                        "An angel is sent from Heaven to help a desperately frustrated businessman by showing him what life would have been like if he had never existed.",
                        "https://upload.wikimedia.org/wikipedia/en/9/95/Its_A_Wonderful_Life_Movie_Poster.jpg",
                        "https://www.youtube.com/watch?v=LJfZaT8ncYk")

princess_bride = media.Movie("The Princess Bride",
                     "While home sick in bed, a young boy's grandfather reads him a story called The Princess Bride.",
                     "https://upload.wikimedia.org/wikipedia/en/d/db/Princess_bride.jpg",
                     "https://www.youtube.com/watch?v=VYgcrny2hRs")

serenity = media.Movie("Serenity",
                     "The crew of the ship Serenity try to evade an assassin sent to recapture one of their members who is telepathic.",
                     "https://upload.wikimedia.org/wikipedia/en/9/9e/Serenity_One_Sheet.jpg",
                     "https://www.youtube.com/watch?v=ZLv_GTmAbEE")

holy_grail = media.Movie("Monty Python And The Holy Grail",
                     "King Arthur and his knights embark on a low-budget search for the Grail, encountering many, very silly obstacles.",
                     "https://upload.wikimedia.org/wikipedia/en/0/08/Monty-Python-1975-poster.png",
                     "https://www.youtube.com/watch?v=urRkGvhXc8w")

rogue_one = media.Movie("Rogue One",
                     "The Rebel Alliance makes a risky move to steal the plans for the Death Star, setting up the epic saga to follow.",
                     "https://upload.wikimedia.org/wikipedia/en/d/d4/Rogue_One%2C_A_Star_Wars_Story_poster.png",
                     "https://www.youtube.com/watch?v=frdj1zb9sMY")

oh_brother = media.Movie("Oh Brother, Where Art Thou",
                     "In the deep south during the 1930s, three escaped convicts search for hidden treasure while a relentless lawman pursues them.",
                     "https://upload.wikimedia.org/wikipedia/en/5/5b/O_brother_where_art_thou_ver1.jpg",
                     "https://www.youtube.com/watch?v=eW9Xo2HtlJI")
movies = [wonderful_life, princess_bride, serenity, holy_grail, rogue_one, oh_brother]

fresh_tomatoes.open_movies_page(movies)



