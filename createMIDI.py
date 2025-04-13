import mido
from mido import Message, MidiFile, MidiTrack, MetaMessage

bpm = 35
ticks_per_beat = 480  
midi = MidiFile(ticks_per_beat=ticks_per_beat)
track = MidiTrack()
midi.tracks.append(track)


track.append(MetaMessage('set_tempo', tempo=mido.bpm2tempo(bpm)))
track.append(MetaMessage('time_signature', numerator=4, denominator=4))


note_map = {'C': 60, 'D': 62, 'E': 64, 'F': 65, 'G': 67, 'A': 69}


def dur(fraction):
    return int(ticks_per_beat * fraction)


def add_note(track, note, length):
    track.append(Message('note_on', note=note_map[note], velocity=64, time=0))
    track.append(Message('note_off', note=note_map[note], velocity=64, time=length))


def add_sequence():
    
    track.append(Message('note_off', note=0, velocity=0, time=dur(1/4)))
    track.append(Message('note_off', note=0, velocity=0, time=dur(1/4)))
    track.append(Message('note_off', note=0, velocity=0, time=dur(1/4)))

    
    for note in ['C', 'D', 'C', 'D']:
        add_note(track, note, dur(1/16))

    
    track.append(Message('note_on', note=note_map['A'], velocity=64, time=0))
    track.append(Message('note_off', note=note_map['A'], velocity=64, time=dur(5/16)))

    
    track.append(Message('note_on', note=note_map['G'], velocity=64, time=0))
    track.append(Message('note_off', note=note_map['G'], velocity=64, time=dur(3/8)))

    
    for note in ['C', 'D', 'F', 'D']:
        add_note(track, note, dur(1/16))

   
    track.append(Message('note_on', note=note_map['G'], velocity=64, time=0))
    track.append(Message('note_off', note=note_map['G'], velocity=64, time=dur(5/16)))

    
    track.append(Message('note_on', note=note_map['F'], velocity=64, time=0))
    track.append(Message('note_off', note=note_map['F'], velocity=64, time=dur(3/16)))

    
    add_note(track, 'E', dur(1/16))
    add_note(track, 'D', dur(1/8))
    for note in ['C', 'D', 'F', 'D']:
        add_note(track, note, dur(1/16))

    
    add_note(track, 'F', dur(1/4))
    add_note(track, 'G', dur(1/8))
    track.append(Message('note_on', note=note_map['E'], velocity=64, time=0))
    track.append(Message('note_off', note=note_map['E'], velocity=64, time=dur(3/16)))

    
    add_note(track, 'D', dur(1/16))
    add_note(track, 'C', dur(1/4))
    add_note(track, 'C', dur(1/8))

    
    add_note(track, 'G', dur(1/4))
    add_note(track, 'F', dur(1/2))


for _ in range(30):
    add_sequence()


midi.save('melody.mid')