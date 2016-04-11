Intro to Web Dev
================

*Brought to you by the [5CHackathon](http://5chackathon.com) at the Claremont
Colleges.*

> This guide assumes that you are working on a Mac or Linux computer. If you're
> on Windows (or just want to check out a neat, web-based development environment),
> we recommend creating a workspace at [Cloud9](https://c9.io/). This will help
> to simplify the steps to get started!

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
   $ virtualenv env
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

***

## Client-Server Relationship

## Hello, Flask!

## Hello, {{ templating }}!

## Integrating Yelp!

***

## Resources

- [Flask Docs](http://flask.pocoo.org/docs/0.10/)
- [Jinja2 Docs](http://jinja.pocoo.org/docs/dev/)
- [Semantic UI Docs](http://semantic-ui.com/)
- [Yelp API Documentation](https://www.yelp.com/developers/documentation/v2/overview)
- [Yelp API Python Wrapper](https://github.com/gfairchild/yelpapi)
