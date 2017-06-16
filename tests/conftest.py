import pytest

from django_resource import Resource


@pytest.fixture
def gist_resource():
    class GistResource(Resource):
        endpoint = 'https://api.github.com/gists'
    return GistResource


@pytest.fixture
def gist_resource_manager(gist_resource):
    return gist_resource.objects


@pytest.fixture
def gist_id():
    return '522e0ee9dfa07d7a61651a22ce355590'


@pytest.fixture
def gist_data():
    return {
        'url': 'https://api.github.com/gists/522e0ee9dfa07d7a61651a22ce355590',
        'forks_url': 'https://api.github.com/gists/522e0ee9dfa07d7a61651a22ce355590/forks',
        'commits_url': 'https://api.github.com/gists/522e0ee9dfa07d7a61651a22ce355590/commits',
        'id': '522e0ee9dfa07d7a61651a22ce355590',
        'git_pull_url': 'https://gist.github.com/522e0ee9dfa07d7a61651a22ce355590.git',
        'git_push_url': 'https://gist.github.com/522e0ee9dfa07d7a61651a22ce355590.git',
        'html_url': 'https://gist.github.com/522e0ee9dfa07d7a61651a22ce355590',
        'files': {
            'b.js': {
                'filename': 'b.js',
                'type': 'application/javascript',
                'language': 'JavaScript',
                'raw_url': 'https://gist.githubusercontent.com/thangman22/522e0ee9dfa07d7a61651a22ce355590/raw/3b93c72de939b81830aee7eda84e8cdb4a36c99f/b.js',
                'size': 45,
                'truncated': False,
                'content': 'function b(){\n  return Promise.resolve(res)\n}'
            }
        },
        'public': True,
        'created_at': '2017-05-28T03:41:04Z',
        'updated_at': '2017-05-28T03:41:04Z',
        'description': '',
        'comments': 0,
        'user': None,
        'comments_url': 'https://api.github.com/gists/522e0ee9dfa07d7a61651a22ce355590/comments',
        'owner': {
            'login': 'thangman22',
            'id': 806893,
            'avatar_url': 'https://avatars0.githubusercontent.com/u/806893?v=3',
            'gravatar_id': '',
            'url': 'https://api.github.com/users/thangman22',
            'html_url': 'https://github.com/thangman22',
            'followers_url': 'https://api.github.com/users/thangman22/followers',
            'following_url': 'https://api.github.com/users/thangman22/following{/other_user}',
            'gists_url': 'https://api.github.com/users/thangman22/gists{/gist_id}',
            'starred_url': 'https://api.github.com/users/thangman22/starred{/owner}{/repo}',
            'subscriptions_url': 'https://api.github.com/users/thangman22/subscriptions',
            'organizations_url': 'https://api.github.com/users/thangman22/orgs',
            'repos_url': 'https://api.github.com/users/thangman22/repos',
            'events_url': 'https://api.github.com/users/thangman22/events{/privacy}',
            'received_events_url': 'https://api.github.com/users/thangman22/received_events',
            'type': 'User',
            'site_admin': False
        },
        'forks': [],
        'history': [{
            'user': {
                'login': 'thangman22',
                'id': 806893,
                'avatar_url': 'https://avatars0.githubusercontent.com/u/806893?v=3',
                'gravatar_id': '',
                'url': 'https://api.github.com/users/thangman22',
                'html_url': 'https://github.com/thangman22',
                'followers_url': 'https://api.github.com/users/thangman22/followers',
                'following_url': 'https://api.github.com/users/thangman22/following{/other_user}',
                'gists_url': 'https://api.github.com/users/thangman22/gists{/gist_id}',
                'starred_url': 'https://api.github.com/users/thangman22/starred{/owner}{/repo}',
                'subscriptions_url': 'https://api.github.com/users/thangman22/subscriptions',
                'organizations_url': 'https://api.github.com/users/thangman22/orgs',
                'repos_url': 'https://api.github.com/users/thangman22/repos',
                'events_url': 'https://api.github.com/users/thangman22/events{/privacy}',
                'received_events_url': 'https://api.github.com/users/thangman22/received_events',
                'type': 'User',
                'site_admin': False
            },
            'version': '1ad68e37327b6141bd806029fa1f628c4aeb31ac',
            'committed_at': '2017-05-28T03:41:04Z',
            'change_status': {
                'total': 3,
                'additions': 3,
                'deletions': 0
            },
            'url': 'https://api.github.com/gists/522e0ee9dfa07d7a61651a22ce355590/1ad68e37327b6141bd806029fa1f628c4aeb31ac'
        }],
        'truncated': False
    }


@pytest.fixture
def gists_data():
    return [{
        'url': 'https://api.github.com/gists/717414f47607c71e377a010c4f2a79e7',
        'forks_url': 'https://api.github.com/gists/717414f47607c71e377a010c4f2a79e7/forks',
        'commits_url': 'https://api.github.com/gists/717414f47607c71e377a010c4f2a79e7/commits',
        'id': '717414f47607c71e377a010c4f2a79e7',
        'git_pull_url': 'https://gist.github.com/717414f47607c71e377a010c4f2a79e7.git',
        'git_push_url': 'https://gist.github.com/717414f47607c71e377a010c4f2a79e7.git',
        'html_url': 'https://gist.github.com/717414f47607c71e377a010c4f2a79e7',
        'files': {
            'Образец патронажа к ребенку из неблагополучной семьи.md': {
                'filename': 'Образец патронажа к ребенку из неблагополучной семьи.md',
                'type': 'text/plain',
                'language': 'Markdown',
                'raw_url': 'https://gist.githubusercontent.com/anonymous/717414f47607c71e377a010c4f2a79e7/raw/b19477e0f2f661bc4fde104c76a2d00ad764c6e1/%D0%9E%D0%B1%D1%80%D0%B0%D0%B7%D0%B5%D1%86%20%D0%BF%D0%B0%D1%82%D1%80%D0%BE%D0%BD%D0%B0%D0%B6%D0%B0%20%D0%BA%20%D1%80%D0%B5%D0%B1%D0%B5%D0%BD%D0%BA%D1%83%20%D0%B8%D0%B7%20%D0%BD%D0%B5%D0%B1%D0%BB%D0%B0%D0%B3%D0%BE%D0%BF%D0%BE%D0%BB%D1%83%D1%87%D0%BD%D0%BE%D0%B9%20%D1%81%D0%B5%D0%BC%D1%8C%D0%B8.md',
                'size': 7890,
            }
        },
        'public': True,
        'created_at': '2017-06-15T22:09:42Z',
        'updated_at': '2017-06-15T22:09:43Z',
        'description': 'Образец патронажа к ребенку из неблагополучной семьи',
        'comments': 0,
        'user': None,
        'comments_url': 'https://api.github.com/gists/717414f47607c71e377a010c4f2a79e7/comments',
        'truncated': False
    }, {
        'url': 'https://api.github.com/gists/522e0ee9dfa07d7a61651a22ce355590',
        'forks_url': 'https://api.github.com/gists/522e0ee9dfa07d7a61651a22ce355590/forks',
        'commits_url': 'https://api.github.com/gists/522e0ee9dfa07d7a61651a22ce355590/commits',
        'id': '522e0ee9dfa07d7a61651a22ce355590',
        'git_pull_url': 'https://gist.github.com/522e0ee9dfa07d7a61651a22ce355590.git',
        'git_push_url': 'https://gist.github.com/522e0ee9dfa07d7a61651a22ce355590.git',
        'html_url': 'https://gist.github.com/522e0ee9dfa07d7a61651a22ce355590',
        'files': {
            'b.js': {
                'filename': 'b.js',
                'type': 'application/javascript',
                'language': 'JavaScript',
                'raw_url': 'https://gist.githubusercontent.com/thangman22/522e0ee9dfa07d7a61651a22ce355590/raw/3b93c72de939b81830aee7eda84e8cdb4a36c99f/b.js',
                'size': 45,
                'truncated': False,
                'content': 'function b(){\n  return Promise.resolve(res)\n}'
            }
        },
        'public': True,
        'created_at': '2017-05-28T03:41:04Z',
        'updated_at': '2017-05-28T03:41:04Z',
        'description': '',
        'comments': 0,
        'user': None,
        'comments_url': 'https://api.github.com/gists/522e0ee9dfa07d7a61651a22ce355590/comments',
        'truncated': False
    }]


@pytest.fixture
def fetch_url():
    return 'http://example.com/id/'


@pytest.fixture
def httpbin_url():
    return 'http://httpbin.org/'
