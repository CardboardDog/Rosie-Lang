import py2exe
files = [
    ""
]
py2exe.freeze(
    console=[
        "Rosie.py"
    ],
    options={"py2exe":{"bundle_files":1,'compressed': True}},
    zipfile=None
)