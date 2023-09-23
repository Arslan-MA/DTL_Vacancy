from random import randint, choice
import string

it_companies = ["Google", "Apple", "Microsoft", "Amazon", "Facebook",
                "IBM", "Oracle", "Intel", "Adobe", "NVIDIA", ]

status = ["Senior", "Middle", "Junior"]

p_languages = ["Python", "JavaScript", "Java", "C++", "Ruby",
               "Go", "Swift", "PHP", "Rust", "TypeScript", ]

job_requirements = [
    "Опыт разработки на Python не менее 3 лет",
    "Знание фреймворков Django и Flask",
    "Умение работать с базами данных, включая SQL и NoSQL",
    "Знание JavaScript, HTML, и CSS",
    "Опыт работы с системами контроля версий, такими как Git",
    "Умение разрабатывать RESTful API",
    "Знание английского языка на техническом уровне",
    "Умение писать чистый и эффективный код",
    "Опыт разработки мобильных приложений (Android/iOS) - преимущество",
    "Знание алгоритмов и структур данных",
    "Опыт работы с системами сборки и автоматизации (например, Jenkins, Travis CI)",
    "Знание Docker и контейнеризации",
    "Умение работать в команде и обучать новичков",
    "Опыт работы с архитектурными паттернами",
    "Умение работать в Agile/Scrum методологии",
    "Знание тестирования и отладки кода",
    "Опыт оптимизации производительности приложений",
    "Знание систем развертывания, таких как AWS, Heroku или Azure",
    "Опыт работы с библиотеками и фреймворками для машинного обучения - преимущество",
    "Умение принимать технические решения и решать сложные задачи"
]


def get_description():
    return str([choice(string.ascii_letters) for _ in range(500)])


def get_vacancy():
    return f"{choice(status)} {choice(p_languages)} Developer"


def get_salary():
    return randint(1000, 10000)




