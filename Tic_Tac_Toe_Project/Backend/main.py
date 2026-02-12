from fastapi import FastAPI, Request, Form
from fastapi.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from database import get_connection
import random
import time

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

class Game:
    def __init__(self):
        self.reset_all()

    def reset_all(self):
        self.board = [""] * 9
        self.move_history = []
        self.winning_cells = []
        self.player1 = ""
        self.player2 = ""
        self.player1_symbol = "X"
        self.player2_symbol = "O"
        self.current_player = "X"
        self.mode = ""
        self.difficulty = "easy"
        self.p1_score = 0
        self.p2_score = 0
        self.tie_score = 0
        self.round = 1
        self.last_move_time = None

game = Game()

WIN_PATTERNS = [
    [0,1,2],[3,4,5],[6,7,8],
    [0,3,6],[1,4,7],[2,5,8],
    [0,4,8],[2,4,6]
]

def check_winner(board):
    for pattern in WIN_PATTERNS:
        if board[pattern[0]] != "" and \
           board[pattern[0]] == board[pattern[1]] == board[pattern[2]]:
            game.winning_cells = pattern
            return board[pattern[0]]
    if "" not in board:
        return "Tie"
    return None

def minimax(board, is_max):
    result = check_winner(board)
    if result == game.player2_symbol:
        return 1
    if result == game.player1_symbol:
        return -1
    if result == "Tie":
        return 0

    if is_max:
        best = -100
        for i in range(9):
            if board[i] == "":
                board[i] = game.player2_symbol
                score = minimax(board, False)
                board[i] = ""
                best = max(best, score)
        return best
    else:
        best = 100
        for i in range(9):
            if board[i] == "":
                board[i] = game.player1_symbol
                score = minimax(board, True)
                board[i] = ""
                best = min(best, score)
        return best

def best_move():
    best_score = -100
    move = None
    for i in range(9):
        if game.board[i] == "":
            game.board[i] = game.player2_symbol
            score = minimax(game.board, False)
            game.board[i] = ""
            if score > best_score:
                best_score = score
                move = i
    return move

def random_move():
    empty = [i for i in range(9) if game.board[i] == ""]
    return random.choice(empty) if empty else None

def update_leaderboard(winner):
    if winner == "Tie":
        return
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT wins FROM leaderboard WHERE player_name=%s", (winner,))
    result = cursor.fetchone()
    if result:
        cursor.execute("UPDATE leaderboard SET wins=wins+1 WHERE player_name=%s", (winner,))
    else:
        cursor.execute("INSERT INTO leaderboard (player_name, wins) VALUES (%s,1)", (winner,))
    conn.commit()
    cursor.close()
    conn.close()

def save_game(winner):
    if winner == game.player1_symbol:
        game.p1_score += 1
        winner_name = game.player1
    elif winner == game.player2_symbol:
        game.p2_score += 1
        winner_name = game.player2
    else:
        game.tie_score += 1
        winner_name = "Tie"

    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO game_history (player1, player2, winner, result)
        VALUES (%s,%s,%s,%s)
    """, (game.player1, game.player2, winner_name,
          "Tie" if winner == "Tie" else "Win"))
    conn.commit()
    cursor.close()
    conn.close()

    update_leaderboard(winner_name)

@app.get("/")
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/mode")
def mode(mode: str = Form(...)):
    game.reset_all()
    game.mode = mode
    return RedirectResponse("/setup", status_code=303)

@app.get("/setup")
def setup(request: Request):
    return templates.TemplateResponse("setup.html", {"request": request, "mode": game.mode})

@app.post("/start")
def start(p1: str = Form(...),
          p2: str = Form(None),
          symbol: str = Form(...),
          level: str = Form(None)):
    game.player1 = p1
    game.player1_symbol = symbol
    game.player2_symbol = "O" if symbol == "X" else "X"
    if game.mode == "single":
        game.player2 = "Computer"
        game.difficulty = level
    else:
        game.player2 = p2
    return RedirectResponse("/game", status_code=303)

@app.get("/game")
def game_page(request: Request):
    winner = check_winner(game.board)
    return templates.TemplateResponse("game.html", {"request": request, "game": game, "winner": winner})

@app.post("/move/{pos}")
def move(pos: int):
    if game.board[pos] == "" and not check_winner(game.board):
        game.board[pos] = game.current_player
        game.move_history.append(pos)
        game.last_move_time = time.time()
        game.current_player = game.player2_symbol if game.current_player == game.player1_symbol else game.player1_symbol
        if game.mode == "single" and game.current_player == game.player2_symbol:
            if game.difficulty == "easy":
                ai = random_move()
            elif game.difficulty == "medium":
                ai = random_move() if random.random() < 0.5 else best_move()
            else:
                ai = best_move()
            if ai is not None:
                game.board[ai] = game.player2_symbol
                game.move_history.append(ai)
            game.current_player = game.player1_symbol
    winner = check_winner(game.board)
    if winner:
        save_game(winner)
    return RedirectResponse("/game", status_code=303)

@app.post("/undo")
def undo():
    if game.move_history and time.time() - game.last_move_time <= 3:
        last = game.move_history.pop()
        game.board[last] = ""
    return RedirectResponse("/game", status_code=303)

@app.post("/restart")
def restart():
    game.board = [""] * 9
    game.move_history = []
    game.winning_cells = []
    game.round += 1
    return RedirectResponse("/game", status_code=303)

@app.post("/reset_score")
def reset_score():
    game.p1_score = 0
    game.p2_score = 0
    game.tie_score = 0
    return RedirectResponse("/game", status_code=303)

@app.post("/quit")
def quit_game():
    return RedirectResponse("/", status_code=303)

@app.get("/leaderboard")
def leaderboard_page(request: Request):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT player_name, wins FROM leaderboard ORDER BY wins DESC")
    players = cursor.fetchall()
    cursor.close()
    conn.close()
    return templates.TemplateResponse("leaderboard.html", {"request": request, "players": players})
