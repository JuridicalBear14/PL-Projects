#include <stdio.h>
#include <stdlib.h>
#include <ncurses.h>
#include <string.h>
#include <unistd.h>
#include <stdbool.h>

#define bg 1
#define set 2
#define cursor 3
#define navbar_off 4
#define navbar_on 5

// Set a square when clicked to either on or off
void flip_square(int y, int x, int** board) {
    if (board[y][x]) {
        attron(COLOR_PAIR(bg));
        mvaddch(y, x, ' ');
        attroff(COLOR_PAIR(bg));
    } else {
        attron(COLOR_PAIR(set));
        mvaddch(y, x, ' ');
        attroff(COLOR_PAIR(set));
    }

    // Invert saved board val
    board[y][x] = !board[y][x];
}

// Draw the navigation bar at the top of the screen
void draw_navbar(int LINES, int COLS, int color) {
    // Text to write
    char* conway = "Conway's Game of Life";
    int conway_len = strlen(conway);

    // Change control text based on mode
    char* controls;
    if (color == navbar_on) {
        controls =
        "([p]->[q]-quit) ([space]/[enter]-advance game) ([p]-pause)";
    } else {
        controls =
        "([q]-quit) ([space]/[enter]-set square) ([p]-play)";
    }
    int control_len = strlen(controls);

    // Draw colored line
    attron(COLOR_PAIR(color));
    mvhline(0, 0, ' ', COLS);

    // Draw strings
    mvaddstr(0, 0, conway);
    mvaddstr(0, COLS - control_len - 1, controls);

    attroff(COLOR_PAIR(color));
}

// Redraw all squares with updates values
void draw_board(int** board) {
    // Start at 1 because of navbar offset
    for (int i = 1; i < LINES; i++) {
        for (int j = 0; j < COLS; j++) {
            // Set to whatever array says it should be
            if (board[i][j]) {
                attron(COLOR_PAIR(set));
                mvaddch(i, j, ' ');
                attroff(COLOR_PAIR(set));
            } else {
                attron(COLOR_PAIR(bg));
                mvaddch(i, j, ' ');
                attroff(COLOR_PAIR(bg));
            }
        }
    }
}

// Returns whether or not square is within valid bounds
bool isvalid(int y, int x) {
    return ((y > 1) && (y < LINES) && (x > 0) && (x < COLS));
}

// Gets the total value of neighbors of a certain square
int neighbor_count(int y, int x, int** board) {
    int count = (board[y][x])? -1 : 0;   // Total count, -1 to offset for self

    // Loop from just before to just after x
    for (int i = y - 1; i <= y + 1; i++) {
        for (int j = x - 1; j <= x + 1; j++) {
            if (isvalid(i, j) && board[i][j]) {
                count++;
            }
        }
    }

    return count;
}

// Update board values based on conway rules
void update_board(int** board) {
    // Temporary copy of board for logic
    int** temp = (int**) calloc(LINES, sizeof(int*));
    for (int i = 0; i < LINES; i++) {
        temp[i] = (int*) calloc(COLS, sizeof(int));
    }

    // Copy vals
    for (int i = 0; i < LINES; i++) {
        for (int j = 0; j < COLS; j++) {
            temp[i][j] = board[i][j];
        }
    }

    // Loop through each val of the board updating them
    for (int i = 1; i < LINES; i++) {
        for (int j = 0; j < COLS; j++) {
            int n = neighbor_count(i, j, temp);

            /* Neat bug
            if (n == 1) {
                flip_square(i, j, board);
            }


            continue;
            /**/

            if (temp[i][j]) {
                // If alive, check if dies
                if (n < 2 || n > 3) {
                    board[i][j] = 0;
                } else {
                    board[i][j] = 1;
                }
            } else {
                // If dead, check if comes alive
                if (n == 3) {
                    board[i][j] = 1;
                } else {
                    board[i][j] = 0;
                }
            }
        }
    }

    // Free temp
    for (int i = 0; i < LINES; i++) {
        free(temp[i]);
    }

    free(temp);

}

// Switch into play mode and update squares in cycles
void play_game(int y, int x, int** board) {
    // Switch into play mode
    draw_navbar(LINES, COLS, navbar_on);
    curs_set(0);
    refresh();

    // Game loop
    int ch;
    while ((ch = getch()) != 'p') {
        // Exit key
        switch (ch) {
            case ' ':
            case '\n':
                // One generation
                update_board(board);
                draw_board(board);
        }
    }

    // Switch back to draw mode
    draw_navbar(LINES, COLS, navbar_off);
    curs_set(1);
}



int main(int argc, char** argv) {
    int delay = 1;   // Default delay of 1

    // Set delay based on command line args
    if (argc == 2) {
        delay = atoi(argv[1]);
    }

    // Set up gui stuff
    initscr();
    cbreak();
    noecho();
    keypad(stdscr, TRUE);
    start_color();

    // Set up color pairs
    init_pair(set, COLOR_WHITE, COLOR_BLACK);
    init_pair(bg, COLOR_BLUE, COLOR_WHITE);
    init_pair(cursor, COLOR_WHITE, COLOR_BLUE);
    init_pair(navbar_off, COLOR_BLACK, COLOR_GREEN);
    init_pair(navbar_on, COLOR_BLACK, COLOR_RED);

    // Draw navbar
    draw_navbar(LINES, COLS, navbar_off);

    // Draw background lines
    attron(COLOR_PAIR(bg));
    for (int i = 1; i < LINES; i++) {
        mvhline(i, 0, ' ', COLS);
    }
    attroff(COLOR_PAIR(bg));

    // Initialize board array
    int** board = (int**) calloc(LINES, sizeof(int*));
    for (int i = 0; i < LINES; i++) {
        board[i] = (int*) calloc(COLS, sizeof(int));
    }

    // Set up starting pos
    int x = COLS / 2;
    int y = LINES / 2;
    move(y, x);

    int ch;

    // Event loop
    while ((ch = getch()) != 'q') {
        switch(ch) {
            case KEY_UP:
                // >1 to account for navbar at top
                y -= (y > 1);   // Equals a bool to decide whether move 1 or 0
                break;
            case KEY_DOWN:
                y += (y < LINES - 1);
                break;
            case KEY_LEFT:
                x -= (x > 0);
                break;
            case KEY_RIGHT:
                x += (x < COLS - 1);
                break;

            case '\n':
            case ' ':
                // Select square
                flip_square(y, x, board);
                break;

            case 'p':
                play_game(y, x, board);
                break;

            default:
                continue;
         }
         move(y, x);
         refresh();
    }

    // Free board
    for (int i = 0; i < LINES; i++) {
        free(board[i]);
    }

    free(board);

    endwin();
    return 0;
}
