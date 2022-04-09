# Gitea Mirror
Key idea for this project is to provide the simplest solution
to backup all Gitea repositories on daily basis with simple command

## How to use
This application requires only API key for Gitea.
Unfortunately it only allows to create root-level API keys.

You can generate one here:
```
https://YOUR_INSTANCE/user/settings/applications
```

Other methods are not supporting:
1. User/password is not safe and hard to use with 2FA enabled
2. With ssh only public repositories may be found.
  Which is acceptable for full account mirroring.

**Security notice.**
This application uses SSH as git transport layer.
It is safe enough with right use,
and for right use you need to save 
git server ssh digest (~/.ssh/known_hosts file).
To do this you just need to clone any repository over ssh first

**Config**. We use single config for this application.
It is slightly ancient solution for modern Docker/Kubernetes backends,
but provides configuration in one place and _secure enough_ place to save token.


Example config:
```ini
[main]
endpoint=https://example.com
token=XXXXX
format={owner}/{name}
out_dir=/home/user/repositories
ssh_key=/home/user/id_rsa
```


### Native
Not recommended, but more efficient in space
and does not require docker.
removing the ability to specify a user
1. Clone this repository (`git clone ...`)
2. Install dependencies (`pip3 install -r requirements.txt`).
  Venv-level is recommended.
3. Install git (`sudo apt install git`)
4. And run it with path to ini config.
```bash
python gitea-mirror.py config.ini
```


### Docker
The simplest way.

**TBD**

## How to develop
We use [pre-commit](https://pre-commit.com/) for basic
style fixes and checks.

Also, pytest is used for testing.
It can be installed with `pip install -r requirements.dev.txt`.

To run tests:
```bash
pytest --cov=src tests
```

## FAQ
- **Q:** Is it possible to specify user?

- **A:** This tool should be as simple as possible.
Token as the only one identifier is _good enough_ for 95% cases.


- **Q:** Why I can not just use gitea own `backup` command?

- **A:** For many personal instances or instances for small commands only repositories are important
  (not users, wiki, issues, etc).
  It _does not_ solve backup problem in general,
  but gives possibility to back up all personal repositories with ease.
  (And without access to root-level of Gitea instance)

- **Q:** Why Python with dependencies for so small application?

- **A:** Using libraries for specific cases is a good practice in industry.
  And it keeps code simple and easy to verify (for bugs or malicious actions).
  Which is much more important than one-time venv or Docker setup.