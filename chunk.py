def count_chunks(h, ref):
    chunks = 1
    segment = h[0] + " "
    for i, word in enumerate(h):
        if segment not in ref:
            chunks+=1
            segment = ""
            segment+=word + " "
        else:
            if i != 0:
                segment+=h[i] + " "
        print segment
    return chunks

h1 = "the cat sat on the mat"
ref = "the sat cat on the mat"

print count_chunks(h1.split(" "), ref)
