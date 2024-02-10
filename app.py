from flask import Flask, render_template, request
# Import your data processing and visualization functions
from comparison_logic import compare_players, get_image_paths

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/compare', methods=['POST'])
def compare():
    player1 = request.form['player1']
    player2 = request.form['player2']

     # Get the image paths for the selected players
    result_paths = get_image_paths(player1, player2)
    
    # # Call your data processing and visualization function
    # result = compare_players(player1, player2)

    
    # Render a template or return a response with the results
    return render_template('comparison_result.html', result_paths=result_paths)

if __name__ == '__main__':
    app.run(debug=True)

    
