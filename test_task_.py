import pytest
from task_ import get_posts

# def test_step(get_token):
#     result = get(get_token)
#     lst = result['data']
#     lst_id = [el["id"] for el in lst]
#     assert 79746 in lst_id

#
# проверка наличия поста

def test_step2(get_token):
    result = get_posts(get_token)
    lst = result['data']
    lst_discr = [el['description'] for el in lst]
    assert 'gggggggggggggggggggggggggggggggg' in lst_discr

if __name__ == '__main__':
    pytest.main(['-v'])
