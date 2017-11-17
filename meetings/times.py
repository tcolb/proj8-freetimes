class Chunk:
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


    def __lt__(self, other):
        return self._start < other.start()


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

        if o_start <= self._start and o_end < self._end:
            ret.append(Chunk(o_end, self._end))
        elif o_start > self._start and o_end >= self._end:
            ret.append(Chunk(self._start, o_start))
        elif o_start <= self._start and o_end >= self._end:
            return [ None ]
        elif o_start > self._start and o_end < self._end:
            ret.append(Chunk(self._start, o_start))
            ret.append(Chunk(o_end, self._end))

        return ret


    def __add__(self, other):
        """
        Cases:
            1. o_start < start and o_end <= end, new start = o_start
            2. o_start <= start and o_end >= end, new start = o_start, new end = o_end
            3. o_start >= start and o_end > end, new end = compare_end
            4. else return current chunk

        Returns:
            new chunk object
        """
        o_start = other.start()
        o_end = other.end()

        if o_start <= self._start and o_end >= self._end:
            return Chunk(o_start, o_end)
        elif o_start < self._start and o_end <= self._end:
            return Chunk(o_start, self._end)
        elif o_start >= self._start and o_end > self._end:
            return Chunk(self._start, o_end)
        else:
            return self


    def __repr__(self):
        return "({}, {})".format(self._start, self._end)


    def __eq__(self, other):
        return self._start == other.start() and self._end == other.end()


    def refactor_start(self, replace):
        self._start = replace


    def refactor_end(self, replace):
        self._end = replace




class Block:
    """
    Time Block class consisting of time Chunks

    Allows intersection of Blocks

    Attributes:
            chunks: a list of chunks the block is made of
    """
    def __init__(self, chunks):
        s_chunks = sorted(chunks)
        self._chunks = self._clean_chunks(s_chunks)


    def _clean_chunks(self, chunks):

        worked_chunks = chunks  # Comparison list to check for work being done
        updated = True

        while updated:  # Only continue when work was done last iteration
            updated = False
            chunks_length = len(chunks)  # Remove redundency
            for i in range(chunks_length - 1):
                chunk = chunks[i]
                add_chunk = chunk
                for j in range(i+1, chunks_length):
                    add_chunk =+ chunks[j]
                    if add_chunk != chunk: # Check to see if chunk changed
                        chunk = add_chunk  # To prevent from always triggering
                        worked_chunks[j] = None  # Mark removal of redundant
                        updated = True  # Mark updated
                worked_chunks[i] = add_chunk

            # Remove redundant chunks from worked_chunks
            worked_chunks = [ chunk for chunk in worked_chunks if chunk != None ]
            # Set chunks list to worked_chunks
            chunks = worked_chunks

        return chunks


    def __sub__(self, other):
        # Usage ex: master block - conflict block
        result = [ ]
        for chunk in this._chunks:  # iterate through this chunks
            for o_chunk in other.chunks():  # iterate through other chunks
                alter_chunks = chunk - o_chunk  # sub other chunk from this chunk
            [ result.append(c) for c in alter_chunks ]  # append worked on chunk

        return Block(result)


    def chunks(self):
        return self._chunks
