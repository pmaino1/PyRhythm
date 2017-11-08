import note #filename.png (str), x, y, speed methods:create(), move()
import track #filename.png (str), x, y, methods: checkIfHit(), createNote()
import song #music.mp3 (str), some way to store notes(list or strings, list), bpm(int) methods: play()


def main():
    testNote = note.Note()

    print("testing move")
    testNote.move(1)
    assert testNote.y == -1

    print("testing create")
    testNote.create(1,2)
    assert testNote.x == 1
    assert testNote.y == 2


    testTrack = track.Track()

    print("testing check if hit")
    assert testTrack.checkIfHit(testNote) == "Perfect"
    assert testTrack.checkIfHit(testNote) == "Good"
    assert testTrack.checkIfHit(testNote) == "Miss"

    print("testing create note on a track")
    testTrack = createNote()
    assert newNote.x == testTrack.y     #newNote is a WIP



main()
