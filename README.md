# Oauth Primer

Doing to a mini-project to help me get better at integarting Oauth into a project. Tried using the js/ts ecosystem, but it proved somewhat difficult (mostly dur to passportJs poor ts documenation). Decided to use my goto language for scripting and lightweight tasks, and that is why the project is coded primarily in python.

Packages used include:
- Flask
- SqlAlchemy
- bootstrap

a more comprehensive list can be found in the [`requiremnets.txt`](./requirements.txt) file

# Setup

1. To get started, you need to first create a virtual environment. A common and well thought out name is `.venv`, which is what I have called mine too:

```bash
python -m venv .venv
```

2. Next you need to activate the virtual environment:

```bash
source .venv/bin/activate
```

> [!NOTE]
>
> This method only works for Unix based operating systems, i.e Linux and MacOs. If you are using Windows, look for altenative means to startup you virtual environment.

3. Next, you install all dependencies in the `requirements.txt` file:

```bash
pip install -r requirements.txt
```

4. Finally, you will start the python server, and using the link outputted, navigate to the select web url:

```bash
python app.py
```

> [!WARNING]
>
> For a smooth worlflow as demonstarted above, First ensure that you have `python 3.*` and `pip` installed, since they are the major requirements for the entire project.
