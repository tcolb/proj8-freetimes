class Chunk(object):
    """
    Time Chunk class, a Chunk of time with start and end times

    Allows refactoring of start and end times

    Attributes:
            start: a starting time for the chunk (isoformat)
              end: an ending time for the chunk (isoformat)
    """

    def __init__(self, start, end):
        self._start = start
        self._end = end


    def start(self):
        return self._start


    def end(self):
        return self._end


    def __sub__(self, other):
        """
        Cases:
            1. o_start <= start and o_end <  end, slice top half
            2. o_start >  start and o_end >= end, slice bot half
            3. o_start <= start and o_end >= end, remove chunk
            4. o_start >  start and 0_end <  end, split mid

        Returns:
            list containing new chunk object(s)
        """
        ret = [ ]
        o_start = other.start()
        o_end = other.end()

        if o_start <= this._start and o_end <= this._end:
            ret.append(tuple(o_start, this._end))
        elif o_start >= this._start: and o_end >= this._end:
            ret.append(tuple(this._start, o_end))
        elif o_start <= this._start and o_end >= this._end:
            ret.append(tuple(o_start, o_end))
        else
            ret.append(tuple(this._start, o_start))
            ret.append(tuple(o_end, this._end))

        return ret


    def compare_start(self, other):
        return self.start() < other.start()


    def compare_end(self, other):
        return self.end() < other.end()


    def refactor_start(self, replace):
        self._start = replace


    def refactor_end(self, replace):
        self._end = replace




class Block(object):
    """
    Time Block class consisting of time Chunks

    Allows intersection of Blocks

    Attributes:
            chunks: a list of chunks the block is made of
    """

    def __init__(self, chunks):
        self._chunks = chunks


    def __sub__(self, other):
        # Usage ex: master block - conflict block

        for chunk in this._chunks:
            for o_chunk in other.chunks():

                if o_chunk.overlaps(chunk):




    def __slice(base_chunk, sub_chunk):



    def chunks(self):
        return self._chunks
