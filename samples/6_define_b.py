DEFINE turn_right(s,t)=OnFwd(OUT_A, s);OnRev(OUT_B, s);Wait(t);
DEFINE turn_left(s,t)=OnRev(OUT_A, s);OnFwd(OUT_B, s);Wait(t);
DEFINE forwards(s,t)=OnFwd(OUT_AB, s);Wait(t);
DEFINE backwards(s,t)=OnRev(OUT_AB, s);Wait(t);

def main():

    backwards(50,10000)
    forwards(50,10000)
    turn_left(75,750)
    forwards(75,1000)
    backwards(75,2000)
    forwards(75,1000)
    turn_right(75,750)
    forwards(30,2000)
    Off(OUT_AB)
