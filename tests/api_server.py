from flask import Flask, jsonify


def create_app():
    _app = Flask(__name__)
    add_routes(app=_app)
    return _app


def add_routes(app):
    @app.route('/', methods=['GET'])
    def get_index():
        return jsonify({'sever': 'Running'})

    @app.route('/get-test', methods=['GET'])
    def get_one():
        return jsonify({'Get-Test': 'A-OK'})

    @app.route('/post-test', methods=['POST'])
    def post_one():
        return jsonify({'Post-Test': 'A-OK'})

    @app.route('/put-test', methods=['PUT'])
    def put_one():
        return jsonify({'Put-Test': 'A-OK'})

    @app.route('/patch-test', methods=['PATCH'])
    def patch_one():
        return jsonify({'Patch-Test': 'A-OK'})

    @app.route('/delete-test', methods=['DELETE'])
    def delete_one():
        return jsonify({'Delete-Test': 'A-OK'})


if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
