from testing.api.base import RekonoTestCase
from users.models import User


class ProjectsTest(RekonoTestCase):
    '''Test cases for Projects module.'''

    def setUp(self) -> None:
        '''Create initial data before run tests.'''
        super().setUp()
        self.endpoint = '/api/projects/'                                        # Projects API endpoint
        # Data for testing
        self.create_data = {'name': 'Project Test', 'description': 'Project Test', 'tags': ['test']}
        self.new_data = {'name': 'New Test', 'description': 'New Test', 'tags': ['new']}
        # Create project for testing
        self.project = self.api_test(self.rekono.post, self.endpoint, 201, self.create_data, self.create_data)
        self.user = User.objects.create(username='project', email='project@project.project', password='project')

    def test_create(self) -> None:
        '''Test project creation feature.'''
        self.api_test(self.rekono.post, self.endpoint, 201, self.new_data, self.new_data)           # Create new project

    def test_invalid_create(self) -> None:
        '''Test project creation feature with invalid data.'''
        self.api_test(self.rekono.post, self.endpoint, 400, self.create_data)   # Project already exists

    def test_update(self) -> None:
        '''Test project update feature.'''
        data = {'name': 'Update Test', 'description': 'Update Test', 'tags': ['update']}
        self.api_test(self.rekono.put, f'{self.endpoint}{self.project["id"]}/', 200, data, data)    # Update project

    def test_invalid_update(self) -> None:
        '''Test project update feature with invalid data.'''
        # Create new project
        content = self.api_test(self.rekono.post, self.endpoint, 201, self.new_data, self.new_data)
        # Project already exists
        self.api_test(self.rekono.put, f'{self.endpoint}{content["id"]}/', 400, self.create_data)

    def test_delete(self) -> None:
        '''Test project deletion feature.'''
        self.api_test(self.rekono.delete, f'{self.endpoint}{self.project["id"]}/', 204)             # Delete new project
        self.api_test(self.rekono.get, f'{self.endpoint}{self.project["id"]}/', 404)

    def test_add_member(self) -> None:
        '''Test add project member feature.'''
        # Add member to the testing project
        self.api_test(self.rekono.post, f'{self.endpoint}{self.project["id"]}/members/', 201, {'user': self.user.id})

    def test_add_not_found_member(self) -> None:
        '''Test add project member feature with not found user.'''
        # Add unexisting member to the testing project
        self.api_test(self.rekono.post, f'/api/projects/{self.project["id"]}/members/', 404, {'user': -1})

    def test_add_invalid_member(self) -> None:
        '''Test add project member feature with invalid data.'''
        self.api_test(self.rekono.post, f'/api/projects/{self.project["id"]}/members/', 400)        # User is required

    def test_remove_member(self) -> None:
        '''Test remove project member feature.'''
        # Add member to the testing project
        self.api_test(self.rekono.post, f'{self.endpoint}{self.project["id"]}/members/', 201, {'user': self.user.id})
        # Remove project member
        self.api_test(self.rekono.delete, f'/api/projects/{self.project["id"]}/members/{self.user.id}/', 204)

    def test_remove_not_found_member(self) -> None:
        '''Test remove project member feature with not found user.'''
        # Remove unexisting member from testing project
        self.api_test(self.rekono.delete, f'/api/projects/{self.project["id"]}/members/0/', 404)

    def test_remove_invalid_member(self) -> None:
        '''Test remove project member feature with invalid data.'''
        # Project owner can't be removed
        self.api_test(self.rekono.delete, f'/api/projects/{self.project["id"]}/members/{self.admin.id}/', 400)