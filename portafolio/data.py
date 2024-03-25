import json


class Media:
    def __init__(self, email, cv, github, linkedin):
        self.email = email
        self.cv = cv
        self.github = github
        self.likedin = linkedin


class Technology:
    def __init__(self, icon, name):
        self.icon = icon
        self.name = name


class Info:
    def __init__(self, icon, title, subtitle, description, date="", certificate="", technologies=[], image="", url="", github=""):
        self.icon = icon
        self.title = title
        self.subtitle = subtitle
        self.description = description
        self.date = date
        self.certificate = certificate
        self.technologies = [Technology(**tech) for tech in technologies]
        self.image = image
        self.url = url
        self.github = github


class Extra:
    def __init__(self, image, title, description, url):
        self.image = image
        self.title = title
        self.description = description
        self.descriptionone = description
        self.url = url


class Data:
    def __init__(
        self,
            title,
            description,
            image,
            avatar,
            name,
            skill,
            location,
            media,
            about,
            tech_stack,
            experience,
            projects,
            training,
            extras
    ):
        self.title = title
        self.description = description
        self.image = image
        self.avatar = avatar
        self.name = name
        self.skill = skill
        self.location = location
        self.media = Media(**media)
        self.about = about
        self.tech_stack = [Technology(**tech) for tech in tech_stack]  # Cambiado de self.technologies a self.tech_stack
        self.experience = [Info(**info) for info in experience]
        self.projects = [Info(**info) for info in projects]
        self.training = [Info(**info) for info in training]
        self.extras = [Extra(**info) for info in extras]


with open("assets/data/data.json", 'r', encoding='utf-8') as file:
    json_data = json.load(file)

data = Data(**json_data)
