{ pkgs ? import <nixpkgs> { } }:

pkgs.mkShell { buildInputs = with pkgs; [
    python38
    poetry

    python38.pkgs.isort
    python38.pkgs.flake8

    postgresql

    # C++ dependency
    python38.pkgs.ujson
    python38.pkgs.argon2_cffi
 ]; }
