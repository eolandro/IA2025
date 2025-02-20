%Analizador Lexico y Sintactico%

dir("r").
dir("l").
dir("u").
dir("d").

reg("AX").
reg("BX").
reg("CX").
reg("DX").

sh("a").
sh("b").
sh("c").
sh("d").
sh("e").
sh("f").
sh(N) :- is_digit(N).

hex(["0","x",A,B]) :- sh(A),sh(B).

string_to_listchar("",[]).
string_to_listchar(Strs,R) :-
  string_codes(Strs,[F|C]),
  text_to_string([F],SF),
  text_to_string(C,CF),
  string_to_listchar(CF,RR),
  append([SF],RR,R).

s_hex("") :- !,fail.
s_hex(S) :- string_to_listchar(S,LC), hex(LC).

%only with an Upper letter followed by Upper letters or numbers.%
label([E]) :- is_alpha(E), is_upper(E).
label([F|C]) :- 
  label([F]), auxlab(C).

s_label("") :- !,fail.
s_label(S) :- string_to_listchar(S,LC), label(LC).

auxlab([F]) :- is_digit(F).
% auxlab([F]) :- slabel([F]).
auxlab([F]) :- is_alpha(F),is_upper(F).
auxlab([F|C]) :- auxlab([F]), auxlab(C).

dlabel([F|C]) :- 
  last([F|C],":"),
  reverse([F|C],[_|CC]),reverse(CC,R),
  label(R).

s_dlabel("") :- !,fail.
s_dlabel(S) :- string_to_listchar(S,LC), dlabel(LC).

mat("add").
mat("sub").
mat("mul").
mat("div").

opera_mat([Op,A,B,C]) :- mat(Op),reg(A),reg(B),reg(C).
opera_mat([Op,A,B,C]) :- mat(Op),s_hex(A),reg(B),reg(C).
opera_mat([Op,A,B,C]) :- mat(Op),reg(A),s_hex(B),reg(C).
opera_mat([Op,A,B,C]) :- mat(Op),s_hex(A),s_hex(B),reg(C).

s_opera_mat("") :- !,fail.
s_opera_mat(S) :- split_string(S," ","",LC), opera_mat(LC).


senact("mov").
senact("obs").

opera_senact([SA,D]) :- senact(SA),dir(D).

s_opera_senact("") :- !,fail.
s_opera_senact(S) :- split_string(S," ","",LC), opera_senact(LC).

saltos("je").
saltos("jne").

opera_salto([jump,A,B,LABEL]) :- saltos(jump),reg(A),reg(B),s_label(LABEL).
opera_salto([jump,A,B,LABEL]) :- saltos(jump),reg(A),s_hex(B),s_label(LABEL).
opera_salto([jump,A,B,LABEL]) :- saltos(jump),s_hex(A),reg(B),s_label(LABEL).
opera_salto([jump,A,B,LABEL]) :- saltos(jump),s_hex(A),s_hex(B),s_label(LABEL).

s_opera_salto("") :- !,fail.
s_opera_salto(S) :- split_string(S," ","",LC), opera_salto(LC).

%all the availabre actions%
linea_codigo(LC) :- s_opera_salto(LC).
linea_codigo(LC) :- s_opera_senact(LC).
linea_codigo(LC) :- s_opera_mat(LC).
linea_codigo(LC) :- s_dlabel(LC).
