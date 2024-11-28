from flask import Flask, render_template, url_for
import subprocess
import os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/snake')
@app.route('/snake')
def snake():
    try:
        # Use the full absolute path to the game
        script_path = r"E:/Coding/Training-Plan/Project/games/snake_game.py"
        print(f"Launching: python {script_path}")

        # Execute the game script
        subprocess.Popen(['python', script_path])
    except Exception as e:
        return f"Error launching Snake game: {e}"

    # Render the Snake page after launching the game
    return render_template('snake.html')


@app.route('/pong')
def pong():
    try:
        # Use the full absolute path to the Pong game
        script_path = r"E:/Coding/Training-Plan/Project/games/pong_game.py"
        print(f"Launching: python {script_path}")

        # Execute the game script
        subprocess.Popen(['python', script_path])
    except Exception as e:
        return f"Error launching Pong game: {e}"

    # Render the Pong page after launching the game
    return render_template('pong.html')

@app.route('/tic-tac-toe')
def tic_tac_toe():
    try:
        # Use the full absolute path to the Tic-Tac-Toe game
        script_path = r"E:/Coding/Training-Plan/Project/games/tic_tac_toe_game.py"
        print(f"Launching: python {script_path}")

        # Execute the game script
        subprocess.Popen(['python', script_path])
    except Exception as e:
        return f"Error launching Tic-Tac-Toe game: {e}"

    # Render the Tic-Tac-Toe page after launching the game
    return render_template('tic_tac_toe.html')

@app.route('/2048')
def game_2048():
    try:
        # Use the full absolute path to the 2048 game
        script_path = r"E:/Coding/Training-Plan/Project/games/2048_game.py"
        print(f"Launching: python {script_path}")

        # Execute the game script
        subprocess.Popen(['python', script_path])
    except Exception as e:
        return f"Error launching 2048 game: {e}"

    # Render the 2048 page after launching the game
    return render_template('2048.html')




if __name__ == "__main__":
    app.run(debug=True)
