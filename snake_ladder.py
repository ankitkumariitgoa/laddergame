import streamlit as st
import matplotlib.pyplot as plt
import random
import numpy as np
import time
from PIL import Image


st.write("""
# 1 vs 1 Snake ladder game
""")

c1,c2=st.columns(2)
p1=c1.text_input('Player 1 Name:','Type name here..')
color1=c1.selectbox("Select Color For player 1",['blue','green','purple','pink','voilet','orange','purple','magneta','gray'])
p2=c2.text_input('Player 2 Name','Type name here..')
color2=c2.selectbox("Select Color For Player 2",['pink','green','purple','magneta','voilet','orange','purple','magneta','gray'])
d1,d2=st.columns(2)

with d1:
    col1,col2,col3,col4=st.columns(4)
    if "player1_position" not in st.session_state:
        st.session_state.player1_position = 1

    if "player2_position" not in st.session_state:
        st.session_state.player2_position = 1

    if 'turn' not in st.session_state:
        st.session_state.turn = 1
    
    if 'message' not in st.session_state:
        st.session_state.message = ""

    
    a=0
    b=0

    with col2:
        st.write("""
    # Player 1""")
        button1=st.button("Player 1 Move")
        if button1:
            image=["C:\\Users\\ANKIT KUMAR\\Downloads\\face_1.png","C:\\Users\\ANKIT KUMAR\\Downloads\\face_2.png","C:\\Users\\ANKIT KUMAR\\Downloads\\face_3.png","C:\\Users\\ANKIT KUMAR\\Downloads\\face_4.png","C:\\Users\\ANKIT KUMAR\\Downloads\\face_5.png","C:\\Users\\ANKIT KUMAR\\Downloads\\face_6.png"
    ]
            lst=[]
            for i in range(random.randint(1,4)):
                random.shuffle(image)
                lst=lst+image
            placeholder = st.empty()
            if True:
                for image_path in lst:
                    img = Image.open(image_path)
                    placeholder.image(img)
                    time.sleep(0.1)
            a=lst[-1][-5]
            


    with col3:
        st.write("""
    # Player 2""")
        button2=st.button('Player 2 Move')
        if button2:
            lst1=[]
            image=image=["C:\\Users\\ANKIT KUMAR\\Downloads\\face_1.png","C:\\Users\\ANKIT KUMAR\\Downloads\\face_2.png","C:\\Users\\ANKIT KUMAR\\Downloads\\face_3.png","C:\\Users\\ANKIT KUMAR\\Downloads\\face_4.png","C:\\Users\\ANKIT KUMAR\\Downloads\\face_5.png","C:\\Users\\ANKIT KUMAR\\Downloads\\face_6.png"
    ]
            for i in range(random.randint(1,4)):
                random.shuffle(image)
                lst1=lst1+image
            placeholder = st.empty()
            if True:
                for image_path in lst1:
                    img = Image.open(image_path)
                    placeholder.image(img)
                    time.sleep(0.1)
            b=lst1[-1][-5]

        
    st.write(""" 
    # First Player Move -> """,a)
    st.write("""
    # First Player Position -> """, st.session_state.player1_position)
    st.write("""
    # Second Player Move -> """,b)
    st.write("""
    # Second Player Position""", st.session_state.player2_position)

fig,ax=plt.subplots()
lst1=[st.session_state.player1_position,st.session_state.player2_position]
ax.bar(np.array(['Player 1','Player2']),np.array(lst1),color=['blue','orange'],width=1)
plt.legend()
st.pyplot(fig)

snake = [(16, 7), (49, 11), (62, 19), (93, 90), (95, 61), (98, 78),(66,50)]
ladder = [(1, 38), (4, 14), (9, 31), (21, 42), (28, 84), (51, 67), (71, 92), (80, 99)]
snakes={i[0]:i[1] for i in snake}
ladders={j[0]:j[1] for j in ladder}



def draw_board(player1_position, player2_position):
    fig, ax = plt.subplots(figsize=(8, 8))
    for row in range(10):
        for col in range(10):
            cell_num = (9 - row) * 10 + col + 1 if row % 2 == 0 else (9 - row) * 10 + (9 - col) + 1
            # Highlight cells where players are currently located
            if cell_num == player1_position and cell_num == player2_position:
                color = 'purple'  # Both players in the same cell
            elif cell_num == player1_position:
                color =f'{color2}'
            elif cell_num == player2_position:
                color = f'{color1}'
            else:
                color = 'white'
            ax.text(col + 0.5, 9 - row + 0.5, str(cell_num), va='center', ha='center',
                    bbox=dict(facecolor=color, edgecolor='black', boxstyle='round,pad=0.3'), fontsize=12)
            # Draw grid cell borders
            ax.plot([col, col + 1], [9 - row, 9 - row], color='black')
            ax.plot([col, col + 1], [10 - row, 10 - row], color='black')
            ax.plot([col, col], [9 - row, 10 - row], color='black')
            ax.plot([col + 1, col + 1], [9 - row, 10 - row], color='black')

    # Draw snakes and ladders
    for start, end in snakes.items():
        start_x, start_y = (start - 1) % 10, 9 - (start - 1) // 10
        end_x, end_y = (end - 1) % 10, 9 - (end - 1) // 10
        ax.plot([start_x + 0.5, end_x + 0.5], [start_y + 0.5, end_y + 0.5], 'r', linewidth=10, alpha=0.5)
    for start, end in ladders.items():
        start_x, start_y = (start - 1) % 10, 9 - (start - 1) // 10
        end_x, end_y = (end - 1) % 10, 9 - (end - 1) // 10
        ax.plot([start_x + 0.5, end_x + 0.5], [start_y + 0.5, end_y + 0.5], 'g', linewidth=10, alpha=0.5)
    
    ax.axis('off')
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    return fig

def move_player(position, roll):
    new_position = position + roll
    # if new_position in snakes.keys():
    #     new_position = snakes[new_position]
    # if new_position in ladders.keys():
    #     new_position = ladders[new_position]
    if new_position > 100:
        new_position = position
        st.session_state.message = "Roll exceeded 😔 !! Try Again"

    return new_position

if button1:

    if st.session_state.turn == 1:
        st.session_state.player1_position = move_player(st.session_state.player1_position, int(a))            
        if st.session_state.player1_position == 100:
            st.balloons()
            st.write(f" Congratulations! {p1} wins!")
        else:
            st.session_state.turn = 2 
if button2:
    if st.session_state.turn==2: 
        st.session_state.player2_position = move_player(st.session_state.player2_position, int(b))            
        if st.session_state.player2_position == 100:
            st.balloons()
            st.write(f" Congratulations! {p2} wins!")
        else:
            st.session_state.turn = 1  

if st.session_state.turn == 1:
    with col1:
        st.write("""
    ## Player 1 Move""")
else:
    with col4:
        st.write("""
    ## Player 2 Move""")
with d2:
    st.pyplot(draw_board(st.session_state.player1_position, st.session_state.player2_position))