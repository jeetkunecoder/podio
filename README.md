# Podio

This project is an implementation to demo the usage of multiple user types. In this app, teachers can create quizzes and students can sign up and take quizzes related to their interests.

## Running the Project Locally

First, clone the repository to your local machine:

```bash
git clone https://github.com/jeetkunecoder/podio.git
```

Install the requirements:

```bash
pip install -r requirements.txt
```

Create the database:

```bash
python manage.py migrate
```

Finally, run the development server:

```bash
python manage.py runserver
```

The project will be available at **127.0.0.1:8000**.


## License

The source code is released under the [MIT License](https://github.com/sibtc/django-multiple-user-types-example/blob/master/LICENSE).
