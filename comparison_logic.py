# comparison_logic.py

# Function to return the paths to the stats images for the players
def get_image_paths(player1, player2):
    # Dictionary mapping player names to the paths of their stats images
    player_images = {
        'Bam Adebayo': 'images/bamimg.png',
        'Jaylen Brown': 'images/brownimg.png',
        'Anthony Davis': 'images/Anthony_Davis_stats.png',
        'Anthony Edwards': 'images/Anthony_Edwards_stats.png',
        'Andrew Wiggins': 'images/Andrew_Wiggins_stats.png',
        'Draymond Green': 'images/Draymond_Green_stats.png',
        'Fred VanVleet': 'images/Fred_VanVleet_stats.png',
        'Chris Paul': 'images/Chris_Paul_stats.png'
    }

    # Construct a result dictionary with the paths for the selected players
    result_paths = {
        'player1_stats': player_images.get(player1),
        'player2_stats': player_images.get(player2)
    }
    
    return result_paths

# Example usage:
# result_paths = get_image_paths('Bam Adebayo', 'Andrew Wiggins')
# This will return {'player1_stats': 'images/Bam_Adebayo_stats.png', 'player2_stats': 'images/Andrew_Wiggins_stats.png'}