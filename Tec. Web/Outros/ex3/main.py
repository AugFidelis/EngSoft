from flask import Flask
from website import create_app #Tudo que ta na __init__.py pode ser importado diretamente por ser package

app = create_app()

if(__name__ == '__main__'):
    app.run(debug=True)