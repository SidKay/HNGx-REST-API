import requests
import db

base_url = 'http://localhost:5000/api'

def testCreate():
	data = {
		'name': 'Sidney',
		'track': 'backend',
		'age': 22
	}
	response = requests.post(f'{base_url}', json=data)
	assert response.status_code == 200
	print("Create Person: Passed")

def test_read_person():
    response = requests.get('{}/{}'.format(base_url, db.getid('Sidney')[0]))
    assert response.status_code == 200
    result = response.json()
    assert result['name'] == 'Sidney'
    print("Read Person: Passed")

def test_update_person():
    updated_data = {
		'name': 'Joseph',
		'track': 'Frontend',
		'age': 25
	}
    response = requests.put('{}/{}'.format(base_url, db.getid('Sidney')[0]), json=updated_data)
    assert response.status_code == 200
    result = response.json()
    assert result['message'] == f'Person has been updated successfully.'
    print("Update Person: Passed")

def test_delete_person():
    response = requests.delete('{}/{}'.format(base_url, db.getid('Joseph')[0]))
    assert response.status_code == 200
    result = response.json()
    assert result['message'] == 'Person deleted successfully.'
    print("Delete Person: Passed")

if __name__ == '__main__':
    try:
        testCreate()
        test_read_person()
        test_update_person()
        test_delete_person()
    except Exception as e:
        print(f"Test failed: {str(e)}")