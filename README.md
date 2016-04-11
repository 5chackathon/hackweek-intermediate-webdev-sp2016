Intro to Web Dev
================

*Brought to you by the [5CHackathon](http://5chackathon.com) at the Claremont
Colleges.*

> This guide assumes that you are working on a Mac or Linux computer. If you're
> on Windows (or just want to check out a neat, web-based development environment),
> we recommend creating a workspace at [Cloud9](https://c9.io/). This will help
> to simplify the steps to get started!

## Installation and Setup

> We encourage everyone to follow the step-by-step walk through below, but if
> you are pressed for time, please use this quick setup link: <setup-link>.

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
   $ git clone <repo-URL>
   ```
5. Change your working directory to that of the clone repo:
   ```bash
   $ cd <repoDir>
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

At this point, you should be ready to get started on the project. If at any point
you have questions -- including questions about any of the setup above -- please
let use know and we would be more than happy to answer them!
