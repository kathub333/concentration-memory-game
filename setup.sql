CREATE DATABASE IF NOT EXISTS card_game;
USE card_game;
CREATE TABLE IF NOT EXISTS memory (
    sr_no INT,
    player1 VARCHAR(20),
    player2 VARCHAR(20),
    winner VARCHAR(20)
);
