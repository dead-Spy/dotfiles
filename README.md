# dead-Spy Dotfiles

<div align="center">

# dead-Spy Dotfiles

Minimal, productivity-focused **Arch Linux** setup powered by **Hyprland**, **Fish**, **Kitty**, and **Waybar**.

![GitHub stars](https://img.shields.io/github/stars/yourusername/dotfiles?style=for-the-badge)
![GitHub forks](https://img.shields.io/github/forks/yourusername/dotfiles?style=for-the-badge)
![Repo Size](https://img.shields.io/github/repo-size/yourusername/dotfiles?style=for-the-badge)
![Last Commit](https://img.shields.io/github/last-commit/yourusername/dotfiles?style=for-the-badge)
![Arch Linux](https://img.shields.io/badge/OS-Arch_Linux-1793D1?style=for-the-badge&logo=arch-linux&logoColor=white)
![Hyprland](https://img.shields.io/badge/WM-Hyprland-58E1FF?style=for-the-badge)

</div>

---

## Preview

> Replace these placeholders with your real screenshots.

```text
assets/
├── desktop.png
├── terminal.png
├── launcher.png
└── notification.png
```

![Desktop](assets/desktop.png)
![Terminal](assets/terminal.png)

---

## About

This repository contains my personal Linux dotfiles used for daily development, workflow optimization, and desktop customization.

The setup is designed to be:

- Fast
- Clean
- Keyboard-driven
- Modular
- Easy to maintain
- Developer focused

---

## Stack

| Component | Tool |
|----------|------|
| OS | Arch Linux |
| Window Manager | Hyprland |
| Shell | Fish |
| Terminal | Kitty |
| Status Bar | Waybar |
| Launcher | Rofi |
| Notifications | SwayNC |
| File Manager | Thunar |
| Prompt | Starship |

---

## Features

- Minimal modern UI
- Fast Wayland workflow
- Keyboard-driven navigation
- Modular config structure
- Symlink-managed dotfiles
- Lightweight performance
- Developer terminal environment
- Consistent theming
- Daily-use optimized

---

## Repository Structure

```bash
.config/
├── hypr/
├── waybar/
├── kitty/
├── fish/
├── rofi/
├── swaync/
├── wlogout/
└── starship.toml
```

---

## Installation

### Clone

```bash
git clone https://github.com/yourusername/dotfiles.git
cd dotfiles
```

### Backup Existing Configs

```bash
mv ~/.config/hypr ~/.config/hypr.backup
mv ~/.config/waybar ~/.config/waybar.backup
mv ~/.config/kitty ~/.config/kitty.backup
mv ~/.config/fish ~/.config/fish.backup
```

### Create Symlinks

```bash
ln -s ~/dotfiles/.config/hypr ~/.config/hypr
ln -s ~/dotfiles/.config/waybar ~/.config/waybar
ln -s ~/dotfiles/.config/kitty ~/.config/kitty
ln -s ~/dotfiles/.config/fish ~/.config/fish
ln -s ~/dotfiles/.config/rofi ~/.config/rofi
ln -s ~/dotfiles/.config/swaync ~/.config/swaync
```

---

## Dependencies

```bash
hyprland
kitty
fish
waybar
rofi
swaync
thunar
starship
wlogout
waypaper
```

Install:

```bash
sudo pacman -S hyprland kitty fish waybar rofi swaync thunar
yay -S starship waypaper wlogout
```

---

## Keybindings

| Key | Action |
|-----|--------|
| SUPER + Enter | Terminal |
| SUPER + Q | Close Window |
| SUPER + D | Launcher |
| SUPER + E | File Manager |
| SUPER + Shift + Q | Logout Menu |
| SUPER + Shift + S | Screenshot |

---

## Workflow Philosophy

Built for speed, focus, simplicity, and professional daily development workflow.

---

## Roadmap

- [ ] Multi-monitor profiles
- [ ] Auto theme switching
- [ ] Install script
- [ ] More shell aliases
- [ ] Better lockscreen

---

## Customization Tips

- Replace screenshots in `assets/`
- Change wallpaper paths
- Edit Waybar modules
- Update Hyprland keybindings
- Modify Fish aliases
- Customize Starship prompt

---

## Credits

Inspired by the Linux ricing and open-source community.

---

## License

MIT License

---

<div align="center">

Made with Arch + Hyprland + Coffee

</div>
