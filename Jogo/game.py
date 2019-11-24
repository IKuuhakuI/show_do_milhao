import curses

import actions
import getUser
import menu
import pyrebase
import textPrint

def show_game_menu(stdscr, current_user):
    # Menu com as opcoes para o jogo 
    menu_jogo = ('Jogar', 'Perguntas', 'Scoreboard', 'Logout')

    # Esconde o cursor
    curses.curs_set(0)

    # Opcao atual do menu
    current_row_idx = 0

    # Esquemas de cores
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_BLACK, curses.COLOR_GREEN)

    # Imprime o menu do Jogo
    menu.print_menu(stdscr, current_row_idx, menu_jogo)

    # Imprime o titulo do jogo
    textPrint.print_title(stdscr)

    # Pega os dados do usuario que esta logado
    current_user_data = getUser.get_user_data(current_user)
    current_user_name = current_user_data["Name"] 
    current_user_high_score = current_user_data["Highscore"]

    # Imprime o usuario atual
    textPrint.print_bottom(stdscr, "Usuario: " + current_user_name + " | " + str(current_user_high_score))

    while True:
        key = stdscr.getch()

        stdscr.clear()

        if actions.keyboard(key) == 'up' and current_row_idx > 0:
            textPrint.print_center(stdscr, 'up')
            current_row_idx -= 1

        elif actions.keyboard(key) == 'down' and current_row_idx < len(menu_jogo) - 1:
            textPrint.print_center(stdscr, 'down')
            current_row_idx += 1

        elif actions.keyboard(key) == 'enter':
            stdscr.clear()
            textPrint.print_center(stdscr, 'enter')

            if current_row_idx == len(menu_jogo) - 1:
                break

            elif current_row_idx == 0:
                textPrint.print_center(stdscr, "Jogar")
                stdscr.getch()

            elif current_row_idx == 1:
                textPrint.print_center(stdscr, "Perguntas")
                stdscr.getch()

            elif current_row_idx == 2:
                textPrint.print_center(stdscr, "Scoreboard")
                stdscr.getch()

            stdscr.refresh()

        # Imprime o titulo do jogo
        menu.print_menu(stdscr, current_row_idx, menu_jogo)

        # Imprime o usuario atual
        textPrint.print_bottom(stdscr, "Usuario: " + current_user_name + " | " + str(current_user_high_score))
        
        stdscr.refresh()

        textPrint.print_title(stdscr)

def teste(stdscr):
    user_id = 6
    show_game_menu(stdscr, user_id)

curses.wrapper(teste)