from flask import Blueprint, jsonify, request


character_bp = Blueprint('characters', __name__)

#CRUD
#Create Read Update Delete

characters = [
    {
        'id': 1,
        'name': 'Gandalf',
        'quote': 'A wizard is never late, nor is he early. He arrives precisely when he means to.'
    },
    {
        'id': 2,
        'name': 'Frodo Baggins',
        'quote': 'I will take the Ring to Mordor. Though… I do not know the way.'
    },
]

character_next_id_counter = 3


@character_bp.route('/characters', methods=["GET"])
def get_characters():
    return  jsonify(characters), 200


@character_bp.route('/characters/<int:char_id>', methods=["GET"])
def get_character(char_id):
    for character in characters:
        if character["id"] == char_id:
            return jsonify(character), 200
    return jsonify({"error": "character not found"}), 404


@character_bp.route('/characters', methods=["POST"])
def create_character():
    data = request.get_json()
    required_fields = ["name", "quote"]
    missing = [field for field in required_fields if field not in data]
    if missing: 
        return jsonify({"error": f"Misssing fields: {missing}"}),400
    global character_next_id_counter
    data["id"] = character_next_id_counter
    characters.append(data)
    character_next_id_counter += 1
    return jsonify(characters), 200
    

@character_bp.route('/characters/<int:char_id>', methods=["PUT"])
def update_character(char_id):
    data = request.get_json()
    for character in characters:
        if character["id"] == char_id:
            character["name"] = data.get("name", character["name"])
            character["quote"] = data.get("quote", character["quote"])
            return jsonify(character), 200
    return jsonify({"error": "Character not found"}), 404
