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
        self._empty = False


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
            return Chunk(self._start, self._end)


    def __repr__(self):
        return "({}, {})".format(self._start, self._end)


    def __eq__(self, other):
        return self._start == other.start() and self._end == other.end()


    def least_times(self, other):
        return self._start >= other.start() and self._end <= other.end()


    def mark_empty(self):
        self._start = None
        self._end = None
        self._empty = True
        return self

    def empty(self):
        return self._empty



class Block:
    """
    Time Block class consisting of time Chunks

    Allows intersection of Blocks

    Attributes:
            chunks: a list of chunks the block is made of
    """
    def __init__(self, chunks):
        self._chunks = self._merge_chunks(sorted(chunks))


    def _merge_chunks(self, chunks):
        worked_chunks = chunks  # List to check for work being done
        updated = True

        while updated:  # Only continue when work was done last pass

            updated = False
            chunks_length = len(chunks)

            index = 0
            while chunks_length > 1:  # To avoid index errors
                chunk = chunks[index]  # Current index chunk
                work_chunk = chunk  # Chunk to add to

                for j in range(index+1, chunks_length):
                    other_chunk = chunks[j]
                    work_chunk = work_chunk + other_chunk

                    # Second condition is to check if other_chunk is eclipsed by the work_chunks
                    # if so, it's redundant and should be marked for removal
                    if work_chunk != chunk or not work_chunk.least_times(other_chunk):
                        chunk = work_chunk  # Update chunk changes
                        worked_chunks[j] = worked_chunks[j].mark_empty()  # Mark removal of redundant chunk
                        updated = True  # Mark updated
                worked_chunks[index] = work_chunk

                # Remove redundant chunks from worked_chunks
                worked_chunks = [ chunk for chunk in worked_chunks if not chunk.empty() ]

                chunks = worked_chunks  # Update chunks list changes
                chunks_length = len(chunks)  # Update length of chunks list
                index += 1

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
