

## Dadosfera Data App Template

This is a template for building data visualization applications using [Streamlit](https://streamlit.io/). It includes several examples of using components and templates to create interactive and engaging user interfaces.

All examples found in this project were developed using Streamlit's own [documentation](https://docs.streamlit.io/library/get-started/create-an-app).

Getting Started
To get started with this template, you can clone the repository using the following steps:

- Download de source code: 
    - [.zip format](https://github.com/dadosfera/data-app-templates/archive/refs/tags/v0.0.1.zip)
    - [.tar.gz format](https://github.com/dadosfera/data-app-templates/archive/refs/tags/v0.0.1.tar.gz)

Once you have the source code, you can run the data app using the following command:

Copy code
streamlit run app.py
This will start a local server and open the data app in your default web browser. From there, you can customize the application to your needs by adding new components, changing the layout, or incorporating your own data and models.

Deployment
To use this template in your intelligence module, follow this [tutorial](https://docs.dadosfera.ai/docs/data-app-com-streamlit).

Support
If you have any questions or issues with this template, please open an issue on the GitHub repository. We will do our best to provide timely support and address any concerns.

License
This template is released under the MIT License. Feel free to use it for personal or commercial projects. We appreciate any contributions or feedback that you may have.

---
To run the project locally navigate to the folder containing the project's source code and run the following commands:
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