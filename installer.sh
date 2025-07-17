#!/bin/sh

# Destinations
CONFIG_PATH="$HOME/.config/AutoMATE"
SRC_PATH="$HOME/.local/share/AutoMATE"
MAIN_PATH="$HOME/.local/bin"
SERVICE_PATH="$HOME/.config/systemd/user"

# Warn the user not to use sudo or to run as root.
if [ "$(id -u)" -eq 0 ]; then
	echo "Please do not use sudo or run as root!"
	exit 1
fi

# Make the directories.
mkdir -p "$SRC_PATH" "$CONFIG_PATH" "$MAIN_PATH" "$SERVICE_PATH"

# Copy the files.
cp src/* src/.[!.]* src/..?* "$SRC_PATH" 2>/dev/null || true
cp configs/* "$CONFIG_PATH" 2>/dev/null || true
cp run_program.sh "$MAIN_PATH/automate"
cp automate.service "$SERVICE_PATH/"

# Other things it needs to do...
chmod +x "$MAIN_PATH/automate"
if command -v systemctl >/dev/null 2>&1; then
	systemctl --user daemon-reload
	systemctl --user enable --now automate.service
else
	echo "Not able to locate systemctl, skipping service installation."
fi

echo "Installation complete, view installation.md for what to do next."
