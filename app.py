from flask import Flask, request, jsonify, render_template
import requests

app = Flask(__name__)

projects = {}

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/api/projects', methods=['POST'])
def create_project():
    data = request.get_json()
    project_name = data['name']
    packages = data['packages']

    for package in packages:
        package_name = package['name']
        package_version = package.get('version')

        if not package_version:
            response = requests.get(f'https://pypi.org/pypi/{package_name}/json')
            if response.status_code == 200:
                data = response.json()
                package['version'] = data['info']['version']
            else:
                return jsonify({'error': "One or more packages doesn't exist"}), 400
        else:
            response = requests.get(f'https://pypi.org/pypi/{package_name}/{package_version}/json')
            if response.status_code != 200:
                return jsonify({'error': "One or more packages doesn't exist"}), 400

    projects[project_name] = packages
    return jsonify({'name': project_name, 'packages': packages}), 201

@app.route('/api/projects/<project_name>', methods=['GET'])
def get_project(project_name):
    if project_name in projects:
        return jsonify({'name': project_name, 'packages': projects[project_name]})
    else:
        return jsonify({'error': 'Project not found'}), 404

@app.route('/api/projects/<project_name>', methods=['DELETE'])
def delete_project(project_name):
    if project_name in projects:
        del projects[project_name]
        return '', 204
    else:
        return jsonify({'error': 'Project not found'}), 404

if __name__ == '__main__':
    app.run()