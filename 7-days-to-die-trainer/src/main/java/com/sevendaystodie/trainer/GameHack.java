package com.sevendaystodie.trainer;

public class GameHack {
    private final MemoryEditor editor;

    public GameHack(MemoryEditor editor) {
        this.editor = editor;
    }

    public void activateGodMode() {
        editor.writeInt("0x7D2D001", 1);
        System.out.println("God mode activated.");
    }

    public void setPlayerHealth(float health) {
        editor.writeFloat("0x7D2D010", health);
        System.out.println("Player health set to " + health);
    }

    public void setPlayerStamina(float stamina) {
        editor.writeFloat("0x7D2D020", stamina);
        System.out.println("Player stamina set to " + stamina);
    }
}