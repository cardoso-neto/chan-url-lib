from chan_url_lib import ChanURI


def test_url():
    r = ChanURI.from_url("https://boards.4channel.org/a/thread/223061883#q223061883")
    assert str(r) == "4chan/a/223061883"
    assert repr(r) == "ChanURI(chan='4chan', board='a', thread_id=223061883)"
