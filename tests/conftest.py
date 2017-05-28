import pytest

from reqset import Client


@pytest.fixture
def gist_client():
    class GistClient(Client):
        endpoint = 'https://api.github.com/gists'
    return GistClient


@pytest.fixture
def gist_client_manager(gist_client):
    return gist_client.objects


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
        'forks': [

        ],
        'history': [
          {
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
          }
        ],
        'truncated': False
    }

@pytest.fixture
def fetch_url():
    return 'http://example.com/id/'
