# meuBlog

### Pre-requisitos
```sh
    sudo apt install python3-pip python-dev build-essential
```

```sh
    sudo pip3 install virtualenv virtualenvwrapper
```

- Cria um venv com uma versão específica do python
```sh
    mkvirtualenv name_env --python=python3
```

- Cria um venv com um módulo pré-instalado
```
    mkvirtualenv name_env --python=python3 -i name_module
```

### Instalar projeto
 - Criar file **.env** raiz projeto e nele definir variaveis de ambiente:
```sh
    SECRET_KEY=your_key
    DEBUG=False (true or false)
```
