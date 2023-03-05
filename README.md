Para rodar localmente

```sh
    # Crie o virtual env para não poluir sua máquina
    $ python3 -m venv .venv
    # ative seu virtual env
    $ source ./venv/bin/activate
    # navegue para pasta app
    $ cd app/
    # instale as dependencias do projeto
    $ pip install -r requirements.txt
    # inicie o projeto
    $ streamlit run Home.py
```