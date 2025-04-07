import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.Random;

public class ChessRace {

    private static final int BOARD_SIZE = 8;
    private static final char LIGHT_SQUARE = 'O';
    private static final char DARK_SQUARE = 'X';
    private static final Random random = new Random();

    private static final Map<Character, String> PIECE_NAMES = new HashMap<>();

    static {
        PIECE_NAMES.put('N', "Knight");
        PIECE_NAMES.put('B', "Bishop");
        PIECE_NAMES.put('R', "Rook");
        PIECE_NAMES.put('Q', "Queen");
    }

    private char[][] board;
    private Map<Character, int[]> piecePositions;

    public ChessRace() {
        board = new char[BOARD_SIZE][BOARD_SIZE];
        piecePositions = new HashMap<>();
        initializeBoard();
        placePieces();
    }

    private void initializeBoard() {
        for (int row = 0; row < BOARD_SIZE; row++) {
            for (int col = 0; col < BOARD_SIZE; col++) {
                board[row][col] = (row + col) % 2 == 0 ? LIGHT_SQUARE : DARK_SQUARE;
            }
        }
    }

    private void placePieces() {
        List<Character> pieces = Arrays.asList('N', 'B', 'R', 'Q');
        for (char piece : pieces) {
            int col = random.nextInt(BOARD_SIZE);
            piecePositions.put(piece, new int[] { 0, col });
            board[0][col] = piece;
        }
    }

    public void startRace() {
        while (true) {
            if (movePiece('N') || movePiece('B') || movePiece('R') || movePiece('Q')) {
                break;
            }
        }
    }

    private boolean movePiece(char piece) {
        List<int[]> legalMoves = getLegalMoves(piece);
        if (!legalMoves.isEmpty()) {
            int[] newPosition = legalMoves.get(random.nextInt(legalMoves.size()));
            int[] oldPosition = piecePositions.get(piece);
            board[oldPosition[0]][oldPosition[1]] = (oldPosition[0] + oldPosition[1]) % 2 == 0 ? LIGHT_SQUARE
                    : DARK_SQUARE;
            board[newPosition[0]][newPosition[1]] = piece;
            piecePositions.put(piece, newPosition);
            System.out.println(PIECE_NAMES.get(piece) + " moves to " + getSquareName(newPosition));
            printBoard();
            if (newPosition[0] == BOARD_SIZE - 1) {
                System.out.println(PIECE_NAMES.get(piece) + " wins!");
                return true;
            }
        }
        return false;
    }

    private List<int[]> getLegalMoves(char piece) {
        List<int[]> legalMoves = new ArrayList<>();
        int[] position = piecePositions.get(piece);
        int row = position[0];
        int col = position[1];

        switch (piece) {
            case 'N':
                legalMoves.addAll(getKnightMoves(row, col));
                break;
            case 'B':
                legalMoves.addAll(getBishopMoves(row, col));
                break;
            case 'R':
                legalMoves.addAll(getRookMoves(row, col));
                break;
            case 'Q':
                legalMoves.addAll(getQueenMoves(row, col));
                break;
        }

        return legalMoves;
    }

    private List<int[]> getKnightMoves(int row, int col) {
        List<int[]> moves = new ArrayList<>();
        int[][] offsets = { { 2, 1 }, { 2, -1 }, { -2, 1 }, { -2, -1 }, { 1, 2 }, { 1, -2 }, { -1, 2 }, { -1, -2 } };
        for (int[] offset : offsets) {
            int newRow = row + offset[0];
            int newCol = col + offset[1];
            if (isValidMove(newRow, newCol)) {
                moves.add(new int[] { newRow, newCol });
            }
        }
        return moves;
    }

    private List<int[]> getBishopMoves(int row, int col) {
        List<int[]> moves = new ArrayList<>();
        int[][] directions = { { 1, 1 }, { 1, -1 }, { -1, 1 }, { -1, -1 } };
        for (int[] direction : directions) {
            int newRow = row + direction[0];
            int newCol = col + direction[1];
            while (isValidMove(newRow, newCol)) {
                moves.add(new int[] { newRow, newCol });
                newRow += direction[0];
                newCol += direction[1];
            }
        }
        return moves;
    }

    private List<int[]> getRookMoves(int row, int col) {
        List<int[]> moves = new ArrayList<>();
        int[][] directions = { { 1, 0 }, { -1, 0 }, { 0, 1 }, { 0, -1 } };
        for (int[] direction : directions) {
            int newRow = row + direction[0];
            int newCol = col + direction[1];
            while (isValidMove(newRow, newCol)) {
                moves.add(new int[] { newRow, newCol });
                newRow += direction[0];
                newCol += direction[1];
            }
        }
        return moves;
    }

    private List<int[]> getQueenMoves(int row, int col) {
        List<int[]> moves = new ArrayList<>();
        moves.addAll(getBishopMoves(row, col));
        moves.addAll(getRookMoves(row, col));
        return moves;
    }

    private boolean isValidMove(int row, int col) {
        return row >= 0 && row < BOARD_SIZE && col >= 0 && col < BOARD_SIZE && board[row][col] == LIGHT_SQUARE;
    }

    private String getSquareName(int[] position) {
        return (char) ('a' + position[1]) + "" + (position[0] + 1);
    }

    private void printBoard() {
        for (int row = BOARD_SIZE - 1; row >= 0; row--) {
            System.out.print((row + 1) + " ");
            for (int col = 0; col < BOARD_SIZE; col++) {
                System.out.print(board[row][col] + " ");
            }
            System.out.println();
        }
        System.out.println("  a b c d e f g h");
        System.out.println();
    }

    public static void main(String[] args) {
        ChessRace race = new ChessRace();
        race.printBoard();
        race.startRace();
    }
}