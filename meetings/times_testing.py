import nose, arrow
from times import Chunk, Block


#
#  GLOBAL VARS
#


chunk_1 = Chunk(arrow.get("2017-11-16T09:00:00-08:00"),
                arrow.get("2017-11-16T17:00:00-08:00"))
chunk_2 = Chunk(arrow.get("2017-11-16T12:00:00-08:00"),
                arrow.get("2017-11-16T20:00:00-08:00"))
chunk_3 = Chunk(arrow.get("2017-11-16T02:00:00-08:00"),
                arrow.get("2017-11-16T20:00:00-08:00"))


#
#  CHUNK TESTING
#


def test_chunk_initialization():

    time_1 = arrow.get("2017-11-16T09:00:00-08:00")
    time_2 = arrow.get("2017-11-16T17:00:00-08:00")
    chunk = Chunk(time_1, time_2)

    # Testing start and end times
    assert chunk.start() == time_1
    assert chunk.end() == time_2

    print("Chunk initialization working!")


def test_chunk_subtraction():

    # Test __sub__ case 1
    assert (chunk_2 - chunk_1)[0] == Chunk(arrow.get("2017-11-16T17:00:00-08:00"),
                                           arrow.get("2017-11-16T20:00:00-08:00"))

    # Test __sub__ case 2
    assert (chunk_1 - chunk_2)[0] == Chunk(arrow.get("2017-11-16T09:00:00-08:00"),
                                           arrow.get("2017-11-16T12:00:00-08:00"))

    # Test __sub__ case 3
    assert (chunk_1 - chunk_3)[0] == None

    # Test __sub__ case
    assert (chunk_3 - chunk_1) == [ Chunk(arrow.get("2017-11-16T02:00:00-08:00"), arrow.get("2017-11-16T09:00:00-08:00")),
                                    Chunk(arrow.get("2017-11-16T17:00:00-08:00"), arrow.get("2017-11-16T20:00:00-08:00")) ]

    print("Chunk subtraction working!")


def test_chunk_addition():

    # Test __add__ case 1
    assert (chunk_2 + chunk_1) == Chunk(arrow.get("2017-11-16T09:00:00-08:00"),
                                        arrow.get("2017-11-16T20:00:00-08:00"))

    # Test __add__ case 2
    assert (chunk_1 + chunk_2) == Chunk(arrow.get("2017-11-16T09:00:00-08:00"),
                                        arrow.get("2017-11-16T20:00:00-08:00"))

    # Test __add__ case 3
    assert (chunk_3 + chunk_1) == chunk_3

    # Test __add__ case 4
    assert (chunk_1 + chunk_3) == chunk_3

    print("Chunk addition working!")


#
#  BLOCK TESTING
#


def test_block_initialization():

    chunk_4 = Chunk(arrow.get("2017-11-16T02:00:00-08:00"),
                    arrow.get("2017-11-16T06:00:00-08:00"))
    chunk_5 = Chunk(arrow.get("2017-11-16T04:00:00-08:00"),
                    arrow.get("2017-11-16T08:00:00-08:00"))
    chunk_6 = Chunk(arrow.get("2017-11-16T10:00:00-08:00"),
                    arrow.get("2017-11-16T18:00:00-08:00"))
    chunk_7 = Chunk(arrow.get("2017-11-16T12:00:00-08:00"),
                    arrow.get("2017-11-16T20:00:00-08:00"))

    # Test to see if blocks combine chunks at init
    block = Block([chunk_4, chunk_5, chunk_6, chunk_7])
    #assert  == [ Chunk(arrow.get("2017-11-16T02:00:00-08:00"),
    #                                                              arrow.get("2017-11-16T20:00:00-08:00")) ]
    print(block.chunks())
    print("Block initialiation working!")


def test_block_subtraction():

    # Test to see if block subtraction works
    return None


if __name__ == "__main__":
    test_chunk_initialization()
    test_chunk_subtraction()
    test_chunk_addition()

    test_block_initialization()
