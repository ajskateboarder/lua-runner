# Lua runner

Small Flask app which can execute Lua and send a response back. Not supposed to be maintained, just a little side project.

## Highlights

- Sandboxed to prevent malicious code (operation limit of 100000)
- Rate-limited by Flask-Limiter
- Simple to understand UI (albeit pretty minimal)

## Usage

Make sure you have Python and Lua installed (latest version recommended).

Install the Python dependencies:

```bash
pip install -r requirements.txt
```

Start the app:

```bash
python3 app.py
```

Your app should be running on [localhost:5000](http://localhost:5000). That's it, enjoy :)
