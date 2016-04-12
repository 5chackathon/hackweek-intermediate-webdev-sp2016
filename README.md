Intro to Web Dev
================

*Brought to you by the [5CHackathon](http://5chackathon.com) at the Claremont
Colleges.*

> This guide assumes that you are working on a Mac or Linux computer. If you're
> on Windows (or just want to check out a neat, web-based development environment),
> we recommend creating a workspace at [Cloud9](https://c9.io/). This will help
> to simplify the steps to get started!

## Table of Contents

- [About](#about)
- [Day I: Hello, Flask!](#day-i)
- [Installation and Setup](#installation-and-setup)
- [Getting a Yelp Developer Account and API Keys](#getting-a-yelp-developer-account)
- [Resources](#resources)

## About

This workshop is a two-day intro to concepts in web-development that aims to give
you a broad overview of some of the moving parts that go into making a web-application
function. It is by no means comprehensive, so we encourage you to checkout
the links and documentation for the various packages referenced and used.

If you have any question or comments at anytime throughout the evening or during
the hackathon, please let us know!


## Day I

### Setting Up Your Development Environment

In order to get started with the project, we will begin by installing the different
files and dependencies that our project will need to run. The overall instructions
are covered below in the section titled [Installation and Setup](#installation-and-setup);
however, we want to take a second to explain some of the install instructions
in a bit more detail (especially instructions that you will see with many projects),
so please follow them below, then scroll back up here to read the highlights.
(It may be helpful to read this section first, complete the setup, and then read
it again with more context.)

For this project, we will be using `pip` which is the [Python Package Index](https://pypi.python.org/pypi)
to install the dependencies which include [Flask][http://flask.pocoo.org/docs/0.10/],
the package responsible (including its own dependencies) for creating a server and
handling  server requests. `pip` allows
you to install other software projects written in Python. It's a convenient
way to install frameworks that take care of otherwise monotonous or repetitive
code. However, it should be noted that you're installing code someone else wrote,
so you will want to look into the reputability of the maintaners of the project as
well as the source code.

After installing `pip` we had everyone install `virtualenv` and created a
(relatively) isolated environment to install the specific project's dependencies.
It's helpful to use virtual environments to avoid creating dependency conflicts
between projects. (i.e. If one of my projects on my computer use version 0.5 of
Flask and another project uses version 1.0.) It's also helpful to use when you
are developing on different machines or with different people so individuals can
have continutity in the environment that they are running your project in.

The command `source env/bin/activate` is a way to execute an activation script
that sets variables in your shell environment so your code can run the dependencies
installed in the virtual envrionment instead of what is installed globally on your
machine.

> A different `pip` is run when you have `source`d activate versus when
> you open up a fresh shell session, so make sure you `source` the envronment
> before beginning each time you open a new terminal window!

If you were just beginning a project, you would likely use the command `pip install Flask`
or `pip install <some-dependency>` as you needed new dependencies. Since we wanted
everyone using the same packages, we created a file [`requirements.txt`](/requirements.txt)
that listed all the packages and the command `pip install -r requirements.txt`
installed everything at once.

> If you need to generate such a requirement file for your own project, you can
> use the command `pip freeze > requirements.txt` which will (create or overwrite)
> a file with all of `pip`s requirements running in your environment.

To check that all the dependencies were installed correctly, you can create
a file named `application.py` in the directory that conatins this `README` with
the following contents in it:

```python
from flask import Flask
app = Flask(__name__)

@app.route("/")
def index():
    return "Hello, 5CHackathon!"

if __name__ == "__main__":
    app.run()
```

To run it, `cd` into this directory, and type:

```bash
$ python application.py
```

If all goes well, you should see something like the following:

```
(env)rwoll-mac:hw-webdev rwoll$ python application.py
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```

You can then point your browser to `http://127.0.0.1:5000/` and you shoudl get
a greeting!

> **Trouble Shooting**
> - Make sure to use the `source` command to activate the environment. Your
>   command prompt should change to indicate this.
> - If you're getting dependency or package errors, be sure you have run
>   the `pip install` line. You can check the packages installed, by executing
>   `pip list`.

### Client-Server Relationship

Now that we have the setup and installation out of the way, we are going to begin
exploring the client-server relationship. What happens when you type in a URL
like https://github.com/5CHackathon into your browser to visit a web-page?

Your browser, which acts as the *client*, makes a request to the URL which is mapped
to some IP address that eventually finds its way to a *server* which has code on
it to handle your request and eventually return some data back to you which may
be in the form of another HTML page especially if you are making the request from
a browser. (Later, we will talk about JSON which is a data format often returned
by requests to API endpoints to power applications.)

> There is a good image and explantion here if you want to know more:
> [Mozilla Developer Network: What is a Web Server?][MDNWebServer].

When the server gets the request, it can always return one thing or you can
write code to parse the URL and add some logic to run differnt code and return different
information depdending on the URL. Luckily, Flask takes care of parsing the different
parts of the URL and allows us to easily execute different functions and logic
based on them.

Take a quick look though [Mozilla Developer Network: What is a URL?][MDNAboutURL]
for a formal explantion of URLs with emphasis on *parameters* and *"paths to files"*.

> In Flask, paramaters will be accessed through
> `request.args.get("paramater_name")` and "paths to files" will be accessed
> through decorators and function parameters. We will discuss this in the next
> section.

Here are two quick examples:

1. `https://github.com/5chackathon` where `/5chackathon` is considered a path to
   a file or resource (which we will treat abstractly).

2. `https://www.google.com/search?q=5chackathon` where there exists a parameter
   `q` with a value of `5chackathon`.

   > Not all characters can appear in URLs so you may see URLs with `%` signs that
   > are encoded by the browser and then decoded by the server.

### Hello, Flask!

### Hello, {{ templating }}!

### Integrating Yelp!


## Installation and Setup

1. To begin, open up a new Terminal window. (On Macs, you can use `cmd+spacebar`
   or search for it in Spotlight.)
2. Install `pip` which is a Python package manager. On the command-line, type:

   ```bash
   $ sudo easy_install pip
   ```

    > As a general note, the `sudo` command should be treated very carefully. It
    > allows you (or code you run with it) to operate at essentially the
    > root-level of your computer where you (or some malicious install scripts)
    > could do significant damage to your computer!

    After pressing enter, proceed by typing in your password.
3. Now that `pip` is installed, we will install a Python package with it called
   `virtualenv` with the following command:

   ```bash
   $ pip install --user virtualenv
   ```

   > The `--user` flag tells `pip` to only install it to your account instead of
   > globally on your system and does not require `sudo` privledges.

4. Now clone this repo with the following command:

   ```bash
   $ git clone https://github.com/5chackathon/hackweek-intermediate-webdev-sp2016.git hw-webdev
   ```
5. Change your working directory to that of the clone repo:

   ```bash
   $ cd hw-webdev
   ```
6. Create a new Python virtual environment:

   ```bash
   $ python -m virtualenv env
   ```

7. Activate the virtual environment:

   ```bash
   $ source env/bin/activate
   ```

   > If you want to deactivate your virtual environment at any point, simply
   > use the `deactivate` command.

8. Install this project dependencies:

   ```bash
   (env)$ pip install -r requirements.txt
   ```

## Getting a Yelp Developer Account

1. Go to [https://www.yelp.com/signup](https://www.yelp.com/signup).
2. Sign up for an account (and make sure to confirm it via email).
3. Acquire an API Key by visiting the [Manage API Keys](https://www.yelp.com/developers/manage_api_keys)
   page.

   > For *Website URL* use `http://localhost:5000` since we will only be
   > running this app on our local machines.

4. Once successfully submitting the form, you should see four different keys/secrets
   listed. We will come back to them later in the workshop, so copy and paste them
   somehwere safe or leave this tab open.

   > API Keys and secrets should be treated as if they are a password to your account.
   > Never commit your secrets into a source control repository where they
   > could be publicly accessed. Generally, avoid hard coding keys/secrets into
   > your code -- even if it is just to quickly test!

At this point, you should be ready to get started on the project. If at any point
you have questions -- including questions about any of the setup above -- please
let us know and we would be more than happy to answer them!

## Resources

- [Flask Docs][Flask]
- [Jinja2 Docs](http://jinja.pocoo.org/docs/dev/)
- [Semantic UI Docs](http://semantic-ui.com/)
- [Yelp API Documentation](https://www.yelp.com/developers/documentation/v2/overview)
- [Yelp API Python Wrapper](https://github.com/gfairchild/yelpapi)
- [MDN: What is a web server?][MDNWebServer]

[Flask]: http://flask.pocoo.org/docs/0.10/
[MDNWebServer]: https://developer.mozilla.org/en-US/Learn/Common_questions/What_is_a_web_server
[MDNAboutURL]: https://developer.mozilla.org/en-US/Learn/Common_questions/What_is_a_URL
