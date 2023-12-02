import fetch_parser

def test_should_parse_args():
    parser = fetch_parser.getParser()
    args = parser.parse_args(['1','2','3','4','5'])
    assert len(args.webs) == 5

def test_should_have_summary():
    parser = fetch_parser.getParser()
    args = parser.parse_args(['--metadata'])
    assert args.metadata

def test_should_have_summary_with_webs():
    parser = fetch_parser.getParser()
    args = parser.parse_args(["-m", "1","2"])
    assert args.metadata
    assert len(args.webs) == 2

