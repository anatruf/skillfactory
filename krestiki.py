{\rtf1\ansi\ansicpg1251\cocoartf1671\cocoasubrtf600
{\fonttbl\f0\fmodern\fcharset0 Courier;\f1\fnil\fcharset0 Monaco;}
{\colortbl;\red255\green255\blue255;\red117\green114\blue185;\red32\green32\blue32;\red153\green168\blue186;
\red88\green118\blue71;\red86\green132\blue173;\red191\green100\blue38;\red254\green187\blue91;}
{\*\expandedcolortbl;;\csgenericrgb\c45882\c44706\c72549;\csgenericrgb\c12549\c12549\c12549;\csgenericrgb\c60000\c65882\c72941;
\csgenericrgb\c34510\c46275\c27843;\csgenericrgb\c33725\c51765\c67843;\csgenericrgb\c74902\c39216\c14902;\csgenericrgb\c99608\c73333\c35686;}
\paperw11900\paperh16840\margl1440\margr1440\vieww10800\viewh8400\viewkind0
\pard\tx560\tx1120\tx1680\tx2240\tx2800\tx3360\tx3920\tx4480\tx5040\tx5600\tx6160\tx6720\pardirnatural\partightenfactor0

\f0\fs26 \cf2 \cb3 print\cf4 (\cf5 "
\f1 \uc0\u1055 \u1088 \u1080 \u1074 \u1077 \u1090 
\f0 "\cf4 )\
field = \cf2 list\cf4 (\cf2 range\cf4 (\cf6 1\cf7 , \cf6 10\cf4 ))\
\
\
\cf7 def \cf8 make_field\cf4 ():\
    \cf7 for \cf4 i \cf7 in \cf2 range\cf4 (\cf6 3\cf4 ):\
        \cf2 print\cf4 (field[\cf6 0 \cf4 + i * \cf6 3\cf4 ]\cf7 , \cf4 field[\cf6 1 \cf4 + i * \cf6 3\cf4 ]\cf7 , \cf4 field[\cf6 2 \cf4 + i * \cf6 3\cf4 ])\
\
\
\cf7 def \cf8 x0_input\cf4 (player):\
    \cf7 while True\cf4 :\
        player_answer = \cf2 input\cf4 (\cf5 "
\f1 \uc0\u1050 \u1091 \u1076 \u1072 
\f0  
\f1 \uc0\u1087 \u1086 \u1089 \u1090 \u1072 \u1074 \u1080 \u1090 \u1100 
\f0  " \cf4 + player)\
        \cf7 try\cf4 :\
            player_answer = \cf2 int\cf4 (player_answer)\
        \cf7 except\cf4 :\
            \cf2 print\cf4 (\cf5 "
\f1 \uc0\u1053 \u1077 \u1082 \u1086 \u1088 \u1088 \u1077 \u1082 \u1090 \u1085 \u1086 
\f0 "\cf4 )\
            \cf7 continue\
        if \cf4 player_answer >= \cf6 1 \cf7 and \cf4 player_answer <= \cf6 9\cf4 :\
            \cf7 if \cf4 field[player_answer - \cf6 1\cf4 ] != \cf5 "X" \cf7 and \cf4 field[player_answer - \cf6 1\cf4 ] != \cf5 "0"\cf4 :\
                field[player_answer - \cf6 1\cf4 ] = player\
                \cf7 break\
\
\
def \cf8 check_win\cf4 ():\
    win_combinations = ((\cf6 0\cf7 , \cf6 1\cf7 , \cf6 2\cf4 )\cf7 , \cf4 (\cf6 3\cf7 , \cf6 4\cf7 , \cf6 5\cf4 )\cf7 , \cf4 (\cf6 6\cf7 , \cf6 7\cf7 , \cf6 8\cf4 )\cf7 , \cf4 (\cf6 0\cf7 , \cf6 3\cf7 , \cf6 6\cf4 )\cf7 , \cf4 (\cf6 1\cf7 , \cf6 4\cf7 , \cf6 7\cf4 )\cf7 , \cf4 (\cf6 2\cf7 , \cf6 5\cf7 , \cf6 8\cf4 )\cf7 , \cf4 (\cf6 0\cf7 , \cf6 4\cf7 , \cf6 8\cf4 )\cf7 , \cf4 (\cf6 2\cf7 , \cf6 4\cf7 , \cf6 6\cf4 ))\
    \cf7 for \cf4 each \cf7 in \cf4 win_combinations:\
        \cf7 if \cf4 field[each[\cf6 0\cf4 ]] == field[each[\cf6 1\cf4 ]] == field[each[\cf6 2\cf4 ]]:\
            \cf7 return \cf4 field[each[\cf6 0\cf4 ]]\
    \cf7 return False\
\
\
def \cf8 main\cf4 ():\
    count = \cf6 0\
    \cf7 while True\cf4 :\
        make_field()\
        \cf7 if \cf4 count % \cf6 2 \cf4 == \cf6 0\cf4 :\
            x0_input(\cf5 "X"\cf4 )\
        \cf7 else\cf4 :\
            x0_input(\cf5 "0"\cf4 )\
        count += \cf6 1\
        \cf7 if \cf4 count > \cf6 4\cf4 :\
            win = check_win()\
            \cf7 if \cf4 win:\
                \cf2 print\cf4 (\cf5 "
\f1 \uc0\u1042 \u1099 \u1080 \u1075 \u1088 \u1072 \u1083 
\f0  " \cf4 + (\cf5 "0" \cf7 if \cf4 count % \cf6 2 \cf4 == \cf6 0 \cf7 else \cf5 "X"\cf4 ))\
                \cf7 break\
        if \cf4 count == \cf6 9\cf4 :\
            \cf2 print\cf4 (\cf5 "
\f1 \uc0\u1053 \u1080 \u1095 \u1100 \u1103 
\f0 "\cf4 )\
    make_field()\
\
\
main()\
\
}