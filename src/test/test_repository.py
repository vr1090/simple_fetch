import fetch_repository

def test_should_save_content():
    repo = fetch_repository.SoupRepository()
    res =repo.save("test.html","<html></html>")
    assert res

def test_should_parse_content():
    repo = fetch_repository.SoupRepository()
    res =repo.analyze("test.net","<html><a /><img /></html>")
    assert res

def test_should_give_metadata():
    repo = fetch_repository.SoupRepository()
    res =repo.analyze("test.net","<html><a /><img /></html>")
    assert res
    metadata= repo.metadata("test.net")
    assert metadata


def test_should_give_empty_metadata():
    repo = fetch_repository.SoupRepository()
    metadata = repo.metadata("notexist.next")
    assert metadata == {}

   