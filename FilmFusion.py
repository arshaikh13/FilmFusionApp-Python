
class Movie:
    def __init__(self, title, description, lead_actor, lead_actress, support_actor1,
                 support_actor2, director_name, producer_name, studio_name, mpaa_rating,
                 year, box_office):
        self.title = title
        self.description = description
        self.lead_actor = lead_actor
        self.lead_actress = lead_actress
        self.support_actor1 = support_actor1
        self.support_actor2 = support_actor2
        self.director_name = director_name
        self.producer_name = producer_name
        self.studio_name = studio_name
        self.mpaa_rating = mpaa_rating
        self.year = year
        self.box_office = box_office

    def __str__(self):
        return f"Title: {self.title}, Year: {self.year}, Box Office: ${self.box_office}"


class FilmFusion:
    def __init__(self):
        self.movies = []
        self.user_search = ""

    def user_auth(self):
        expected_username = "admin"
        expected_password = "password"
        username = input("Enter username: ")
        password = input("Enter password: ")
        return username == expected_username and password == expected_password

    def main_menu(self):
        print("\nHello!\n")
        while True:
            print("\nMain Menu:\n1. Add Movie\n2. Display All Movies\n3. Search Movie\n4. Exit")
            try:
                choice = int(input("Enter your choice: "))
                if choice == 1:
                    self.add_movie()
                elif choice == 2:
                    self.display_all_movies()
                elif choice == 3:
                    self.search_movie()
                elif choice == 4:
                    print("Exiting...")
                    break
                else:
                    print("Invalid choice. Please select 1-4.")
            except ValueError:
                print("Invalid input. Enter a number.")

    def add_movie(self):
        if not self.user_auth():
            print("Authentication failed.")
            return
        print("Enter movie details:")
        title = input("Title: ")
        description = input("Description: ")
        lead_actor = input("Lead Actor: ")
        lead_actress = input("Lead Actress: ")
        support_actor1 = input("Supporting Actor 1: ")
        support_actor2 = input("Supporting Actor 2: ")
        director_name = input("Director: ")
        producer_name = input("Producer: ")
        studio_name = input("Studio: ")
        mpaa_rating = input("MPAA Rating: ")
        try:
            year = int(input("Year: "))
            box_office = int(input("Box Office Collection: "))
        except ValueError:
            print("Invalid number input.")
            return
        movie = Movie(title, description, lead_actor, lead_actress, support_actor1,
                      support_actor2, director_name, producer_name, studio_name, mpaa_rating,
                      year, box_office)
        self.movies.append(movie)
        print("Movie added successfully.")

    def display_all_movies(self):
        if not self.movies:
            print("No movies to display.")
        for movie in self.movies:
            print(movie)

    def search_movie(self):
        self.user_search = input("Enter title to search: ")
        found = False
        for movie in self.movies:
            if movie.title.lower() == self.user_search.lower():
                print(movie)
                found = True
        if not found:
            print("Movie not found.")


if __name__ == "__main__":
    app = FilmFusion()
    app.main_menu()
